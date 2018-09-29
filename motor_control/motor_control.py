# for accessing and controlling the pins
import RPi.GPIO as gp


#refer to pins by their logical number
#  (eg - pysical pin 8, GPIO14, would be referred to as 14)
gp.setmode(gp.BCM)

pins = [2,3,4,14]

for i in pins:
    gp.setup(i,gp.OUT)



gp.output(2, False)
 
GPIO.output(2, True)

 

