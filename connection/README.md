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

### Configure access point

Ok, I am gonna do a little bit of personalization here.

 - changed `ssid=Pi_AP` to `ssid=fv_nbo`
 - changed `wpa_passphrase=Raspberry` to my standard super-non-secure password

And another very scary thing, from the instructions:

*"If you are not using the Adafruit wifi adapters, you may have to change the driver=rtl871xdrv to say driver=nl80211 or something"*

I do seem to remember something about a driver named something like `nl80211` in my googling around, so gonna go with that.  If this doesnt work, hopefully I can go back to the kball car documentation and see what to do.

 - changed `driver=rtl871xdrv` to `driver=nl80211`

And since I am listing all the changes, might as well remind myself that I also did the 0 to 1 change here.

***Skipping Network Address Translation, because I am not gonna be connecting to other networks***

### Running Network... and troubleshooting

Attempted to bring up network by running:

```
sudo /usr/sbin/hostapd /etc/hostapd/hostapd.conf
```

Got the following error:

```
nl80211: Could not configure driver mode
```

So probably need to figure out if I am using the right driver, using `lsusb` I got the name of the antenna:


```
148f:5370 Ralink Technology, Corp. RT5370 Wireless Adapter
```

According to forums, that is supposed to work out of the box, so gonna try to comment out the driver line (like they said to do for the pi's built in wifi) and see what happens.

...that didnt work either.

Doing a bit more googling, there was another suggestion I am gonna try:

https://askubuntu.com/questions/472794/hostapd-error-nl80211-could-not-configure-driver-mode

```
sudo nmcli nm wifi off
sudo rfkill unblock wlan

sudo ifconfig wlan1 10.15.0.1/24 up
sleep 1
sudo service isc-dhcp-server restart
sudo service hostapd restart
```

I assume this will kill all of my wifi, but I am gonna give it a try anyway.

Also, I am gonna change the `ifconfig` statement to use the ip address from the main instructions:

```
sudo ifconfig wlan1 192.168.42.1 up
```

Lordy, this aint easy... my pi doesnt recognize command `nmcli`, and I am sick of installing stuff, so for right now I am gonna try to go on without it, if that's no good, I'll install it.

instead, gonna try:

```
sudo iwconfig wlan1 txpower off
```

...and then presumably

```
sudo iwconfig wlan1 txpower on
```

Ok, first step worked, but then seemed to get a jumble of errors:

```
pi@raspberrypi:~/Desktop/git_repos/iwantaboat/connection $ sudo iwconfig wlan1 txpower off
pi@raspberrypi:~/Desktop/git_repos/iwantaboat/connection $ sudo ifconfig wlan1 192.168.42.1 up
SIOCSIFFLAGS: Operation not possible due to RF-kill
SIOCSIFFLAGS: Operation not possible due to RF-kill
pi@raspberrypi:~/Desktop/git_repos/iwantaboat/connection $ sudo iwconfig wlan1 txpower on
pi@raspberrypi:~/Desktop/git_repos/iwantaboat/connection $ sudo ifconfig wlan1 192.168.42.1 up
pi@raspberrypi:~/Desktop/git_repos/iwantaboat/connection $ sudo service isc-dhcp-server restart
Job for isc-dhcp-server.service failed because the control process exited with error code.
See "systemctl status isc-dhcp-server.service" and "journalctl -xe" for details.
pi@raspberrypi:~/Desktop/git_repos/iwantaboat/connection $ sudo service hostapd restart
Warning: hostapd.service changed on disk. Run 'systemctl daemon-reload' to reload units.
pi@raspberrypi:~/Desktop/git_repos/iwantaboat/connection $ 
```


I wonder if the problem is that somewhere `wlan1` is still trying to do something automatically...

Man oh man, going back to that weird comment in `/etc/network/interfaces`:

```
# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'
```

So I think what I need to do is setup something for `wlan1` in this file... just not sure exactly what yet.

There is an example in `dhcpcd.conf` for `eth0` (commented out):

```
# Example static IP configuration:
#interface eth0
#static ip_address=192.168.0.10/24
#static ip6_address=fd51:42f8:caae:d92e::ff/64
#static routers=192.168.0.1
#static domain_name_servers=192.168.0.1 8.8.8.8 fd51:42f8:caae:d92e::1
```

I am gonna try to configure it for a static IP address for `wlan1`

```
interface wlan1
static ip_address=192.168.42.1/24
```

I am not gonna do anything with the `static routers` configuration right now, although it seems like it's possible I may have to.

So now gonna try again.

OK, so now when I rollover the wifi icon on the desktop tray, I see that `wlan1` has the IP I want, but is still associated with my internet network, which is weird.

gonna proceed anyway though.

so went back to 'askubuntu' page help, and ran `sudo service isc-dhcp-server restart`, after going to log, saw error:

```
Starting ISC DHCPv4 server: dhcpddhcpd service already running (pid file /var/run/dhcpd.pid currenty exists) ... failed!
```


...maybe that means it's actually already ready, gonna go back to the ***go*** command from main instructions.

Nope, that's no good.

So googled the error, and got to a page with a fairly obscure comment that actually might be what I need.

https://unix.stackexchange.com/questions/347373/dhcp-error-dhcpd-service-already-running

```
So is the dhcpd server already running? Check with ps axu. if it is already running, it should pick up the new config on next restart, so figure out who is starting it, and restart it (or reboot if you can't figure it out). – dirkt Feb 25 '17 at 9:46
```



So it might be that chromium or something else (`wlan0`?) is locking DHCP and preventing the restart.

So I am just gonna restart the machine and see what happens...

Umm, now I dont have any wifi access.

...God help me, so apparently my network is up on the raspberry pi, but I cant access any networks.

So I am here on my windows machine, and I can see the network I set up `fv_nbo`, but on the pi it looks like all the networks are down.

Working on the raspberry pi earlier,  when I tried to run `sudo service isc-dhcp-server restart` I get an error with a bunch of stuff, but notably (maybe):

```
dhcpd[980]: Not configured to listen on any interfaces!
```

But anyway, I am gonna try to SSH into the pi based on the `fv_nbo` network I see on my windows machine, and see what happens.

First though, I need to make sure SSH is enabled on the pi, its disabled by default.

so followed the instructions at: https://www.raspberrypi.org/documentation/remote-access/ssh/

Enabled SSH by following the instructions via the start menu, and actually another option was `remote GPIO`, so I enabled that as well, just in case I need it down the road.

So now gonna disconnect from my windows network, and try to log into the pi...

Ok, I connected through the windows gui, now gonna try SSH via PuTTy...

using the static ip I configured on the pi: 192.168.42.1

***Shit, so this works, but I still have a problem because I cant connect to the internet on the pi.  But anyway, I was able to run the motor control UI from the SSH terminal.***

so what to do next???

I want to be able to use the pi's built in wifi to connect to the internet but use the secondary network to access from my computer / phone, or whatever.

...also, I dont really know why the pi is working in some ways and failing in others, need to figure that out.

OK, googled the error about not configured to listen to any interfaces

https://askubuntu.com/questions/536531/dhcp-server-wont-start-gives-not-configured-to-listen-on-any-interfaces-eve

Then went back to pi and opened `/etc/default/isc-dhcp-server`

added `wlan0` back to `INTERFACESv4`

No changes, gonna restart...

`fv_nbo` come up at restart, but still no networks available

lordy, a lot of stuff going on, commented out `authoritative`, didnt seem to do anything.

***I have all the files on the other pi, should I just grab them and start over???***

BAHHH, so I commented out the `/etc/network/interfaces` file, and that got me back to being able to connect to internet from pi, but killed my `fv_nbo` network...

what to do, how can I have my cake and eat it to?  was there something in the `interfaces` file that I need to put in the dhcpcd file???

or maybe go back to interfaces, and move some of the commands from dhcpcd into the interfaces file???

hmmm... also, looking at the documentation at (https://wiki.archlinux.org/index.php/dhcpcd), it looks like dhcpcd can be called for specific interfaces, is that the solution?

potentially:

 - start of the network with the interfaces file
 - then call dhcpcd from the command line to get `wlan0` up and running
 
 ***MAYBE***
 
 
# Jury Rigged $H1T

Ok, I am struggling here, but able to set up the pi as a virtual router, so lets go from there:

 - I want to SSH into the pi and execute `motor_control_ui.py`
 - to do that, just need to ***uncomment*** the `/etc/network/interfaces`
 - and then SSH into `192.168.42.1`

...so gonna try that

***NOTE: the only thing I uncommented was:***

```
iface wlan1 inet static
  address 192.168.42.1
  netmask 255.255.255.0
```

***Hold on, also uncummented*** `allow-hotplug wlan1`










