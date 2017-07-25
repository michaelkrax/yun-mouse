import serial
import struct
from evdev import InputDevice, categorize, ecodes

ttyATH0 = serial.Serial('/dev/ttyATH0', 115200)


def send_serial(command, value):
    print(command+": "+str(value))
    ttyATH0.write(struct.pack('cb', command, value))


dev = InputDevice('/dev/input/event1')

for event in dev.read_loop():
    if event.type == ecodes.EV_REL and event.code == ecodes.REL_X:
        send_serial('X', event.value)

    if event.type == ecodes.EV_REL and event.code == ecodes.REL_Y:
        send_serial('Y', event.value)

    if event.type == ecodes.EV_REL and event.code == ecodes.REL_WHEEL:
        send_serial('W', event.value)

    if event.type == ecodes.EV_KEY and event.code == ecodes.BTN_LEFT:
        send_serial('L', event.value)

    if event.type == ecodes.EV_KEY and event.code == ecodes.BTN_MIDDLE:
        send_serial('M', event.value)

    if event.type == ecodes.EV_KEY and event.code == ecodes.BTN_RIGHT:
        send_serial('R', event.value)

    # dump raw event for debugging
    # print(categorize(event))

ttyATH0.close()
