# Connection between Pi and Computer (or phone?)

I am really just googling stuff for intructions here.

It seems like there are a lot of different options, but the one I like the most right now is using the pi itself to host a network.  Basically I think that will allow me to access it easily from different computers, phones, etc.

If performance (either pi or battery) becomes and issue, I'll reconsider, but for now, gonna try to follow the instructions at:

https://learn.adafruit.com/setting-up-a-raspberry-pi-as-a-wifi-access-point/overview

And I am using the wifi adaptor that came with my kball car.

# Setting up raspberry pi to host a wifi network

The how-to I am following was designed for connecting to the internet, and I am not doing that so skipping a few steps, hopefully I dont miss anything important.

### Prep Work

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

### Set up DHCP Server

The instructions say to use the in-terminal text editor `nano`, but I hate in-terminal text editors, so I am gonna use thonny instead

```
sudo thonny /etc/dhcp/dhcpd.conf
```

So as I go step by step through this, I dont want to write down everything since I am just following instructions, so I'll just write down when I deviate.  Just in case they take down the instructions though, I added a copy of the webpage into this directory (`WiFi_AdHoc - Debian Wiki.html`)

***Here we go, in the step to setup the interfaces, they reference using `wlan0`, but I am gonna plug my little antenna in and try to use `wlan1`.  So every reference to 1 below is actually 0 in the instructions, unless I note otherwise.***

Hmm, they tell you to run `sudo ifdown wlan1` in case you already have the lan setup.  I clearly do have it setup, but the command throws an error, gonna proceed anyway, cause maybe `ifdown` just isnt configured to care about `wlan1` yet, and hopefully that's what I'll be doing next.

OK, this is super scary, the `/etc/network/interfaces` that they tell you to update basically has nothing in it except comments telling you to use something else for static IPs.  So this could blow up in my face... but gonna proceed anyway, and in adding to adding what they say to add, also gonna add whatever lines they show that are already supposed to be there, as long as I think they should relate to `wlan1` (so basically if they dont appear to reference `wlan0` or `eth0`).

Only good news is that this is all for `wlan1`, so hopefully... hopefully... all I am gonna be doing is screwing up my playground lan, not the main `wlan0`.












