#!/bin/sh

CONFIG_PATH=/data/options.json

PROTOCOLS=$(jq --raw-output .protocols $CONFIG_PATH | egrep -o '[0-9]+')
MQTT_HOST=$(jq --raw-output .mqtt.host $CONFIG_PATH)
MQTT_PORT=$(jq --raw-output .mqtt.port $CONFIG_PATH)
MQTT_TOPIC_DEVICES=$(jq --raw-output .mqtt.devices $CONFIG_PATH)

if [ -n "$PROTOCOLS" ]
then
    for PROTO in $PROTOCOLS
    do
        PROTOCOL_ARGS="$PROTOCOL_ARGS -R $PROTO"
    done
fi

if [ -n "$MQTT_TOPIC_DEVICES" ]
then
    DEVICES_ARG=",devices=$MQTT_TOPIC_DEVICES"
fi

echo "Executing: rtl_433 $PROTOCOL_ARGS -F \"mqtt://$MQTT_HOST:$MQTT_PORT$DEVICES_ARG\""
exec rtl_433 $PROTOCOL_ARGS -F "mqtt://$MQTT_HOST:$MQTT_PORT$DEVICES_ARG"
