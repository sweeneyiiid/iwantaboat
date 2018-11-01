# Motor Control

I have had some issues with the winch control, so I am gonna try some differenct techniques for the motor for the winch.  The motors for the screws are fairly settled.  More detail on how they are wired is in the `wiring` folder.

I control the motors by setting up relays and linking them to the GPIO pins, and then using python to access the pins.

I am starting with the winch operation, but I imagine the code to control the screws will be similar and use the same functions.

### A note on the relays I am using for the screws

Note, this is just for the screws, not the winch.

Powered by five volts, and an attachment to the *ground* of the circuit closes the relay.  This is kind of weird for the raspberry pi, I would have expected to put voltage on the circuit would close the relay, but it actually opens it.  Not a big deal, just have to keep it in mind.

# Winch control

This code will serve as the basis (gineau pig) for controlling all of the motors.


 - channel 1 is the ground for the lowering (call it forward) direction
 - channel 2 is the power for lowering 
 - channel 3 is the ground for raising (reverse)
 - channel 4 is the power for raising

### Pin setup

 - power: physical pin 2
 - ground: pysical pin 6
 - channel 1: pysical pin 3 (`GPIO2`) 
 - channel 2: pysical pin 5 (`GPIO3`) 
 - channel 3: pysical pin 7 (`GPIO4`) 
 - channel 4: pysical pin 8 (`GPIO14`) 

### Basic Script

The down stream system consists of a two 4 channel relays, each linked to a motor linked to a screw.  The relay allows the motor the go from forward to reverse, and a set of four `GPIO` pins, controlled by the `motor_control.py` script, determines which direction the motor rotates.  So the python script basically uses built in libraries for the `GPIO` pins to activate sets of pins, more detail on which pins do what is in the `wiring` folder.

The UI then maps sets of pins to user commands.


### UI Setup

Interacting with keys seems pretty straightforward:

 - https://www.python-course.eu/python3_input.php

***Note though, this is python 3 and I am using python 2, so need to use `raw_input` to get a string.***
 
As I move forward on this, I think I am going to make `motor_control.py` into my own little mini module, and call it from the UI script.  In order to make this work, I want to add the git repo to the `PYTHONPATH`.

 - https://stackoverflow.com/questions/3402168/permanently-add-a-directory-to-pythonpath

Only have to do this once, but including so I dont forget about it if I set this up somewhere else.

### UI Operation

So I turned `motor_control.py` into a library, which is called by `motor_control_ui.py`

It's a very simple program that just looks for keyboard input from the user in an infinite loop until the user types `exit`, then in cleans up the GPIO pins and exits.

It works pretty well though, even making me rethink the need for figuring out how to interpret a key being held down.

### Winch operation

As mentioned above, I had trouble with the standard motor not being powerful enough to raise the winch.  There are several possibilities for how to solve this, but right now I am gonna work on using a stepper motor, which I think may be more powerful and have a slower, hopefully sturdier, pull

Step motors are harder to program because they involve giving sequences of commands on how to turn the motor, rather than just on or off.  These are still controlled kind of like a relay through the `GPIO` pins though, so it shouldn't be too bad.

The reference I am using for how to program the step motor is at:

 - https://42bots.com/tutorials/28byj-48-stepper-motor-with-uln2003-driver-and-arduino-uno/









