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

### Motor Control

This contains the python scripts to control the motors with the GPIO pins.  For now the plan is to basically control everything with relays that switch the various motors from forward to reverse, and the python scripts will control which relays are open vs. shut.

For raising and lowering the winch, this is straightforward, that's what I am working on now.

For controlling the boat, I am planning on doing the same thing, basically putting a screw on starboard and port side, and turning by going forward on one and either off or reverse on the other.

# Changing Gears

I am about to switch to using a custom pi hat for controlling motors, I am saving the work before that to the branch `pre_motor_hat`.



