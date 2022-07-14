# Home Assistant add-on: Dataplicity

This add-on includes the [Dataplicity](https://www.dataplicity.com/) client as well as NGINX set up as a proxy to make Home Assistant available through the [Wormhole](https://docs.dataplicity.com/docs/host-a-website-from-your-pi).

It is an alternative to [this excellent integration](https://github.com/AlexxIT/Dataplicity). The main difference is that the integration installs the Dataplicity client in the HA container, meaning that the Dataplicity shell opens directly in the HA container. The add-on, on the other hand, runs as a separate container.

With the default configuration, access to the Home Assistant's web interface is limited to specific IP addresses (option `allow`). By default, the list contains addresses used by Google Assistant (note: the list is not maintained and may be incomplete/incorrect). You can turn off access control by setting `access_control` to `false`.

The add-on requires a user code to be provided (option `code`). The code can be found when the "ADD NEW DEVICE" button is pressed on the [devices page](https://www.dataplicity.com/devices/). It's in the installation command:

```
curl -s https://www.dataplicity.com/THIS_IS_THE_CODE.py** | sudo python
```

When the add-on is started for the first time, it will register a new device and write the device's credentials into the add-on's configuration. Thanks to that, when the add-on is restarted in the future, it will not create another device but instead it will connect as the originally created one.
