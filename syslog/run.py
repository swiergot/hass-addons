#!/usr/bin/env python3

import asyncio
import json
import socketserver
import sqlite3
import time

from aiohttp import web

from syslog_rfc5424_parser import SyslogMessage, ParseError

SYSLOG_HOST, SYSLOG_PORT = "0.0.0.0", 1514
WEB_PORT = 8099

con = None

headers = {
    "Cache-Control": "no-cache, no-store, must-revalidate",
    "Pragma": "no-cache",
    "Expires": "0",
}

class SyslogProtocol(asyncio.DatagramProtocol):
    def __init__(self):
        super().__init__()

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        try:
            message = SyslogMessage.parse(data.decode("utf-8"))
            message_dict = message.as_dict()
            row_id = int(time.time() * 1000000)
            date = message_dict["timestamp"][0:10]
            message_dict["row_id"] = row_id
            con.execute("insert into messages values (?, ?, ?)", (row_id, date, json.dumps(message_dict)))
        except Exception as e:
            print(e)

routes = web.RouteTableDef()

@routes.get("/")
async def start(request):
    return web.FileResponse("syslog.html", headers=headers)

@routes.get("/messages")
async def serve_messages(request):
    cur = con.execute("select * from messages order by id;")
    return send_messages(cur)

@routes.get(r"/messages/{date:\d\d\d\d-\d\d-\d\d}/{row_id:\d+}")
async def serve_messages(request):
    date = request.match_info["date"]
    row_id = request.match_info["row_id"]
    cur = con.execute("select * from messages where date = ? and id > ? order by id;", (date, row_id))
    return send_messages(cur)

def send_messages(cur):
    messages = []
    for record in cur:
        messages.append(json.loads(record[2]))
    return web.json_response(messages, headers=headers)

if __name__ == '__main__':
    con = sqlite3.connect(":memory:")
    con.execute("create table messages (id integer primary key, date text, message text)")

    loop = asyncio.get_event_loop()

    syslog_server = loop.create_datagram_endpoint(SyslogProtocol, local_addr=(SYSLOG_HOST, SYSLOG_PORT))
    loop.run_until_complete(syslog_server)

    web_app = web.Application()
    web_app.add_routes(routes)
    web_server = web.AppRunner(web_app)
    loop.run_until_complete(web_server.setup())
    web_server_site = web.TCPSite(web_server, port=WEB_PORT)
    loop.run_until_complete(web_server_site.start())

    loop.run_forever()
