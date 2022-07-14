ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

COPY run.py /
COPY syslog.html /
RUN chmod a+x /run.py
RUN apk add --no-cache python3 py3-aiohttp py3-pip

RUN pip3 install syslog-rfc5424-parser

WORKDIR /

ENTRYPOINT ["/usr/bin/env", "python3", "-u", "/run.py"]
