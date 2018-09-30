# custom library mc does background work for GPIO pins
import motor_control as mc
import time


pins = [2,3,4,14]

mc.set_pins_out(pins)
mc.act_pins(pins, "high")


while True:
    cmd_in = raw_input("motor_control: ")
    if cmd_in == 'help':
        print('\n               f : foward \n               r : reverse \n            exit : exit program \n            help : display help \n <any other key> : stop \n')
    elif cmd_in == 'exit':
        mc.act_pins([4,14,2,3], 'high')
        break
    elif cmd_in == 'f':
        mc.act_pins([2,3], 'high')
        mc.act_pins([4,14], 'low')
    elif cmd_in == 'r':
        mc.act_pins([4,14], 'high')
        mc.act_pins([2,3], 'low')
    else:
        mc.act_pins([4,14,2,3], 'high')
        
print('Goodbye')