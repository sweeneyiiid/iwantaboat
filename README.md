# iwantaboat
My attempts to set up a raspberry pi based boat
# What I need to do
 - get a camera server up and running
 - get the custom network set up
 - setup raspberry pi with camera
 - get actual motors and boat operation going
 - write the program to put it all together 

# Directories 



### Camera Setup

Got camera server set up on raspberry pi itself, so killed two birds with one stone.  See readme within the directory for details, but basically streams to a website.  So I've punted on getting the custom website set up for now, but am able to stream to the web, so should be fine.  

Note, this directory is just the readme at this point.  All of the setup was a one time thing, and once I then once I get to putting it all together, it'll probably just need a couple `sys` commands executed in python to turn on the camera and start streaming.

Also, a bit concerned about framespeed, so may have to come back to this at some point, but good enough for now.

### Connection

This was a bit of trial and error and brute force, but I have set up the pi to work as a virtual router and setup a LAN, as well as setting up a camera server that streams to a local website accessible from any machine logged onto the LAN.

Like camera setup, this directory is just a readme for what I did.

### Motor Control

I have switched gears to use a pi hat specifically designed to control motors.  This will change up the motor control code quite a bit.

### Wiring

This is a readme describing all of my wiring, like motor control, it will change a lot based on the new pi hat.




