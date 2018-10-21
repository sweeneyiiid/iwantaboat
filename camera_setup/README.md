# Camera Work README

***Got a new waterproof camera. Gonna retry all this and see if it still works...***

### Notes on the camera

 - 1.0 Megapixel USB Camera (NOT a raspicam)
 - `ELP-USB100W05MT-DL36`

Some basic docs: https://www.raspberrypi.org/documentation/usage/webcams/

Setting up and basic operation:

***Note, got an error with `fswebcam` when installing new camera, googled the error, and I think its because I already have motion installed and cant use both.***

***So skipping to streaming with the new camera...***

```
sudo apt-get install fswebcam
```

```
fswebcam /home/pi/Pictures/take_a_picture.jpg
```

OK, so the camera definitely works, at least for stills, now onto the next step.

# Setting up streaming

Gonna try to follow the instructions at:

 https://www.instructables.com/id/How-to-Make-Raspberry-Pi-Webcam-Server-and-Stream-/

A lot of this will just be repeating the steps from the link above, but I want to take good notes on exactly what I do.

*Steps 1-5 are basically setting up and then SSH-ing into the pi, I may come back to those, but for now I am just gonna work on the pi itself.*

*So starting with step 6, and I am running a terminal on the pi.*

### Step 6

This will install software called `motion`, I did a quick search, and it appears to be reasonably legit.  Here is the link to the wikipedia page:

https://en.wikipedia.org/wiki/Motion_(surveillance_software)

So back to work:

```
sudo apt-get install motion
```

Hmm, got an error, but in the error suggested running `apt-get update`, and when I ran it with `sudo` it appeared to work.

Next type `lsusb` to check that the system (and apparently `motion` in particular) has detected the camera.

I don't see anything labeled camera, but there is something called `Bus 001 Device 005: ID 05a3:9230 ARC International` that I think is the camera.

Then edit a file called `/etc/motion/motion.conf` ...hmm, cant find it, gonna try to re-install `motion`

OK, nice, worked this time, back to editing. The instructions want you do this within the terminal using the `nano` text editor, but I am gonna navigate to it and use the raspberry pi text editor.

DAMN, I think you need to be a super user to edit the config file, so I am gonna do stupid `sudo nano` after all.

Edits to `/etc/motion/motion.conf`:
 - set `daemon on`
 - set `framerate 100`
 - verified `stream_port 8081`
 - set `stream_quality 100`
 - set `width 640` and `height 480`
 - set `stream_localhost off`
 - set `webcontrol_localhost off`
 - set `post_capture 5`

Exited and saved file

Edited anoter file `sudo nano /etc/default/motion`, just setting from no to yes the only line in the file.

Then restarted `motion`:

```
sudo service motion restart
sudo motion
```

So it's running, to view, get the raspberry pi's IP address, and type it with port 8080 into any web browser.

To get the IP address, type `hostname -I` in the terminal.

***Hmm, seems to work on the machine, but not on the general internet, maybe thats because I am not on the same LAN as the pi...***





