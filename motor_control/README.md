# Motor Control

I control the motors by setting up relays and linking them to the GPIO pins, and then using python to access the pins.

I am starting with the winch operation, but I imagine the code to control the screws will be similar and use the same functions.

### A note on the relay I am using.

Powered by five volts, and an attachment to the *ground* of the circuit closes the relay.  This is kind of weird for the raspberry pi, I would have expected to put voltage on the circuit would close the relay, but it actually opens it.  Not a big deal, just have to keep it in mind.

# Winch control

This code will serve as the basis (gineau pig) for controlling all of the motors.

The down stream system consists of a 4 channel relay linked to a motor

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

Before worrying about interactive operation, going to setup to just run by executing pieces of the script from within the python command line.

Works, but need to understand what happens once I exit the python script.  Based on the behavior of the motor, it seems like it just leaves the pins in their current status when you exit python.

Ok, have it up and running, I am a little bit worried that it's actually faster than I would like, but I am gonna punt that for now and leave it to the UI to control.  Possibly in the future I could do some crazy thing where I try to limit by rotations of winch, we'll see.

### UI operation

Interacting with keys seems pretty straightforward:

 - https://www.python-course.eu/python3_input.php
 
Working with keys that are held down seems like a bit more work, but still doable:

 - https://stackoverflow.com/questions/44903210/how-to-detect-key-press-event-and-key-hold-down-event-without-using-pygame
 









