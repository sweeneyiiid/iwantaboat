# for accessing and controlling the pins
import RPi.GPIO as gp

import sys
#refer to pins by their logical number
#  (eg - pysical pin 8, GPIO14, would be referred to as 14)
gp.setmode(gp.BCM)
print(sys.path)


asdf=input("as")

print(asdf)