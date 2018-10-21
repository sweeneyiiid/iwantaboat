# Camera Work README

***Got a new waterproof camera. Gonna retry all this and see if it still works...***

### Notes on the camera

 - 1.0 Megapixel USB Camera (NOT a raspicam)
 - `ELP-USB100W05MT-DL36`

# Setting up streaming

Gonna try to follow the instructions at:

 https://www.instructables.com/id/How-to-Make-Raspberry-Pi-Webcam-Server-and-Stream-/


*Steps 1-5 are basically setting up and then SSH-ing into the pi, so I am starting with step 6.*

### Step 6


This will install software called `motion`, I did a quick search, and it appears to be reasonably legit.  Here is the link to the wikipedia page:

https://en.wikipedia.org/wiki/Motion_(surveillance_software)

So back to work:

```
sudo apt-get update
sudo apt-get install motion
```

Next type `lsusb` to check that the system (and apparently `motion` in particular) has detected the camera, the name is `ARC International` for this .


Then edit a file called `/etc/motion/motion.conf`, note have to be in `sudo` mode.

Edits to `/etc/motion/motion.conf`:
 - set `daemon on`
 - set `framerate 100`
 - verified `stream_port 8081`
 - set `stream_quality 100`
 - set `width 640` and `height 480`
 - set `stream_localhost off`
 - set `webcontrol_localhost off`
 - set `post_capture 5`

Exited and saved file, then edited `/etc/default/motion`, just setting from no to yes the only line in the file, then restarted `motion`:

```
sudo service motion restart
sudo motion
```

So it's running, to view, get the raspberry pi's IP address (`hostname -I`), and type it with port 8080 into any web browser.

Note though, I tried with a machine not on the same LAN as the pi, and it didnt work, maybe the IP is just for your LAN.

So anyway, now going to see if it works when pi is set up as a virtual server...




