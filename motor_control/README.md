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

### UI operation

Need to do some research here, but want to figure out a way to control it by holding down button to lower raise, we'll see.






