# for accessing and controlling the pins
import RPi.GPIO as gp


#refer to pins by their logical number
#  (eg - pysical pin 8, GPIO14, would be referred to as 14)
gp.setmode(gp.BCM)

pins = [2,3,4,14]

for i in pins:
    gp.setup(i,gp.OUT)



gp.output(2, False)
gp.output(3, False)
 
gp.output(2, True)
gp.output(3, True)

gp.output(4, False)
gp.output(14, False)
 

