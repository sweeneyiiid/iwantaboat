# for accessing and controlling the pins
import RPi.GPIO as gp


#refer to pins by their logical number
#  (eg - pysical pin 8, GPIO14, would be referred to as 14)
gp.setmode(gp.BCM)


#create function to set pins at once
#setup pins for output
def set_pins_out(pins):
    for i in pins:
        try:
            gp.setup(i,gp.OUT)
        except:
            print("pin input " + str(i) + "invalid, skipping")
            

#switch list of pins to high or low
def act_pins(pins, lvl="high"):

    pin_out = False if lvl == "low" else True
    
    for i in pins:
        try:
            gp.output(i, pin_out)
        except:
            print("pin input " + str(i) + "invalid, skipping")
                
#clean up pins on exit
def exit_mc():
    gp.cleanup()






