# Home Assistant add-on: rtl_433

Receive radio signals from sensors and publish the readings to MQTT.

This [Home Assistant](https://www.home-assistant.io/) [add-on](https://www.home-assistant.io/addons/) runs [rtl_433](https://github.com/merbanan/rtl_433). You need a DVB-T receiver connected to a USB port of the device that hosts your Home Assistant. A dongle based on Realtek RTL2832 is recommended. See [rtl-sdr](https://github.com/osmocom/rtl-sdr/) for details.

## Configuration

First of all, since the add-on needs to access physical USB ports, you will need to disable "Protection mode" on the add-on's Info tab.

By default, all radio protocols are decoded. You can safely leave it as is or, if you know what you are doing, you can use the `protocol` option to specify protocols to decode, for instance:

```yaml
protocols:
  - 19
  - 92
```

The default MQTT broker to connect to is the core add-on [Mosquitto broker](https://github.com/home-assistant/hassio-addons/tree/master/mosquitto). You can easily change it in the configuration.
