# custom library mc does background work for GPIO pins
import motor_control as mc
import time


pins = [2,3,4,14, 17, 27, 22, 10]
pins_winch = [15,18,23,24]

pins_forward_hi_lo = [[2,3,17,27], [4,14,22,10]]
pins_reverse_hi_lo = [[4,14,22,10], [2,3,17,27]]
pins_easy_port_hi_lo = [[2,3,17,27, 22, 10], [4,14]]
pins_hard_port_hi_lo = [[2,3,22,10], [4,14,17, 27]]
pins_easy_starboard_hi_lo = [[2,3,4,14,17,27], [22,10]]
pins_hard_starboard_hi_lo = [[4,14,17, 27], [2,3,22,10]]


mc.set_pins_out(pins)
mc.set_pins_out(pins_winch)
mc.act_pins(pins, "high")
mc.act_pins(pins_winch, "low")


while True:
    cmd_in = raw_input("motor_control: ")
    if cmd_in == 'help':
        print('\n'+
              '               f : foward \n'+
              '               r : reverse \n' +
              '               d : easy port \n' +
              '              dd : hard port \n' +
              '               j : easy starboard \n' +
              '              jj : hard starboard \n' +
              '           lower : stop motion and lower camera \n' +
              '           raise : stop motion and raise camera \n' +
              '            exit : exit program \n' +
              '            help : display help \n ' +
              ' <any other key> : stop \n')
    elif cmd_in == 'exit':
        mc.act_pins(pins, 'high')
        break
    #forward
    elif cmd_in == 'f':
        mc.move_direction(pins_forward_hi_lo)
    #reverse
    elif cmd_in == 'r':
        mc.move_direction(pins_reverse_hi_lo)
    #easy port
    elif cmd_in == 'd':
        mc.move_direction(pins_easy_port_hi_lo)
    #hard port
    elif cmd_in == 'dd':
        mc.move_direction(pins_hard_port_hi_lo)
    #easy starboard
    elif cmd_in == 'j':
        mc.move_direction(pins_easy_starboard_hi_lo)
    #hard starboard
    elif cmd_in == 'jj':
        mc.move_direction(pins_hard_starboard_hi_lo)
    elif cmd_in == 'lower':
        mc.act_pins(pins, 'high')
        mc.act_pins([15,18], 'high')
        mc.act_pins([23,24], 'low')
    elif cmd_in == 'raise':
        mc.act_pins(pins, 'high')
        mc.act_pins([15,18], 'low')
        mc.act_pins([23,24], 'high')
        
    else:
        mc.act_pins(pins, 'high')
        mc.act_pins(pins_winch, 'low')

mc.exit_mc()
print('Goodbye')