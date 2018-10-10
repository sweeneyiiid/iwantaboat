# Wiring Notes

In this section I describe the wiring off all of the electonic components.  Currently there are three motors, each is setup to switch from forward to reverse by a block of four relays.
  
 - One motor for each of two screws
 - One motor for the winch to raise/lower the camera

# Connection to Computer

All electronic components are controlled by the GPIO pins on the Raspberry Pi.  Currently I am using a *Pi-EzConnect* hat to interface with the pins, but the numbering is the same whether I go through the hat or directly to the pi.

# Relay block one

Relay block 1 controls with starboard motor.  The four relays work together to control the circuit connecting the DC power source to the motor.  The series of relays closed determines which way current flows through the motor (to control forward or reverse).

***I should really figure out if there is a better way to describe this, but I am going to describe the motor as having positive `(+)` and negative `(-)` terminals as well as the battery, as a way to describe forward and reverse.***

In each case I describe what link exists when the relay is closed:

 - relay 1: `(-)` battery to `(-)` motor
 - relay 2: `(+)` battery to `(+)` motor
 - relay 3: `(-)` battery to `(+)` motor
 - relay 4: `(+)` battery to `(-)` motor

So Closing relays 1 and 2 (with 3 and 4 open) starts the motor in one direction, opening 1 and 2 and closing 3 and 4 reverses the direction. 

In terms of connecting to the computer:

 - relay 1 is controlled by `GPIO14`
 - relay 2 is controlled by `GPIO4`
 - relay 3 is controlled by `GPIO3`
 - relay 4 is controlled by `GPIO2`


