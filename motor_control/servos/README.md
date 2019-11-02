# Notes on setting up servo motors

Right now I am using a `MG90S` servo.

Some initial research:
 - https://components101.com/motors/mg90s-metal-gear-servo-motor
 - https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/
 - https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/

# PWM Intro

As described in links above, servos have a cycle, in my case 20 milliseconds.

 - 1ms (5%) and the motor moves towards 0 degrees
 - 1.5ms (7.5%) and the motor moves towards 90 degrees
 - 2ms (10%) and the motor moves towards 180%

The `PWM` library has a function called `ChangeDutyCycle` that accepts percentages (not microseconds) as an input.

The example code I got also has 12.5% and 2.5%, need to play around to figure out what that does.

