# Connection between Pi and Computer (or phone?)

I am really just googling stuff for intructions here.

It seems like there are a lot of different options, but the one I like the most right now is using the pi itself to host a network.  Basically I think that will allow me to access it easily from different computers, phones, etc.

If performance (either pi or battery) becomes and issue, I'll reconsider, but for now, gonna try to follow the instructions at:

https://learn.adafruit.com/setting-up-a-raspberry-pi-as-a-wifi-access-point/overview

And I am using the wifi adaptor that came with my kball car.

### Setting up ad hoc network on raspberry pi

The how-to I am following was designed for connecting to the internet, and I am not doing that so skipping a few steps, hopefully I dont miss anything important.

Ok, so the instructions make it seem like the pi doesnt already have a wireless connection, so they refer to `wlan0` but I already have one, so the usb adaptor I plugged in is `wlan1` which I think will be convenient.

```
wlan1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.232.232.224  netmask 255.224.0.0  broadcast 10.255.255.255
        inet6 fe80::63a:e3f0:2c14:fdc7  prefixlen 64  scopeid 0x20<link>
        ether 00:0f:00:51:3c:a4  txqueuelen 1000  (Ethernet)
        RX packets 4  bytes 1016 (1016.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 77  bytes 12814 (12.5 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

Now installing hosting software

```
sudo apt-get update
sudo apt-get install hostapd isc-dhcp-server
```

Hmm, busted on `wlan` but when I unplugged and re-ran command, said it was already installed.  Gonna proceed for now and see what happens.

next they ask you to install an `ip tables manager`:

```
sudo apt-get install iptables-persistent
```







