# Motor Control

After messing around with a few different options, I have settled on what I hope will be a good plan.

 - Two simple motors power the boat, steering by throwing one off or into reverse
 - A larger stepper motor controls the winch, which demands a decent amount of power based on the weight of the camera
 - everything is controlled by a motor board sitting on top of the pi

### Motor board setup

Following instructions from a website run by the board manufacturer:

http://www.raspberrypiwiki.com/index.php/Stepper/Motor/Servo_Robot_Expansion_Board_SKU:418460

First need to enable I2C, following instructions from https://www.androidcentral.com/does-raspberry-pi-3-b-support-i2c

```
sudo raspi-config
```

Then go to interfacing options to turn on, and reboot.

Now downloading some packages:

```
sudo apt-get install python-smbus i2c-tools
sudo apt-get install python-dev
```

Ok, according to pi, I already have those, should be good to go.

Now downloading code... this is kind of dicey, they tell you to clone the git repo, but not what git repo.

found it (I hope) at: https://github.com/Alictronix/Raspi-MotorHat.git

So here we go...

```
pip install git+https://github.com/Alictronix/Raspi-MotorHat.git
```

BAH, the thing isn't set up for pip, but thankfully somebody else on github did that for me.

```
pip install git+https://github.com/orionrobots/Raspi_MotorHAT
```

Ok, looks like this works, now onto testing.

Testing the motor hat:

Also cloning the `orionrobots` version of the repo so I can play around with it and test, as well as the original `Alictronix` version.

OK, at least the basic `DCTest.py` for a single regular motor works.

Now onto getting recreating and expanding the functionality from prior stuff.

### Basic Script

***Need to adjust this for pi hat***

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

As mentioned above, I had trouble with the standard motor not being powerful enough to raise the winch.  There are several possibilities for how to solve this, but I picked up a fairly high power (I hope) bi-polar stepper motor (`17HS16-2004S1`).

I also bought a hat to connect to the motor, I am reading guidance for that at: 


...but I may also go a bit rogue, interestingly, it seems like this may be something you can do with a relay...

According to the spec sheet of the motor (not the hat website above), the motor works as follows:

 - pin 1, black, `A`
 - pin 2, green, `A\`
 - pin 3, red,   `B`
 - pin 4, blue,  `B\`

And the step sequence is:

 - 1: Black, Red: +
 - 2: Red, Green: +
 - 3: Green, Blue: +
 - 4: Black, Blue: + 

Hmm, ok, this worked, but at 12 volts, my connector wires were getting hot, so this is a decent idea, but may need to do a bit more research and pick up some heavier guage wire... or think about running at lower voltage.







