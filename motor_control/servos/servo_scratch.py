import RPi.GPIO as g
import time

g.setmode(g.BOARD)
g.setup(7, g.OUT)

try:
    while True:
        
        g.output(7,1)
        time.sleep(0.0015)
        g.output(7,0)
        time.sleep(2)
    
except KeyboardInterrupt:
    g.cleanup()
    
