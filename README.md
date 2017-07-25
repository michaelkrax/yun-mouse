# yun-mouse
Forward USB mouse actions using Arduino Yun

Fowards actions (X/Y movement, wheel, left/middle/right mouse buttons) of a USB mouse connected to an Arduino Yun (on the OpenWRT side) as USB HID actions via the micro USB connection (on the ATmega side). This project can get easily modified to add and/or modify the behavior of the mouse (e.g. adding acceleration by multiplying X/Y movement, inverting axis, etc).

## Preparing your Arduino Yun
- Install latest OpenWRT (OpenWrt-Yun 1.5.3) via https://www.arduino.cc/en/Main/Software
- Setup WLAN. Optionally insert SD Card and expand disk with the DiskSpaceExpander sketch (https://www.arduino.cc/en/Tutorial/ExpandingYunDiskSpace)
- Connect a USB mouse
- Restart and wait until the white USB LED is on (indicates Linux boot completed)
- Connect via SSH (e.g. via Putty)
- Run the following commands
```
opkg update
opkg install kmod-input-core
opkg install kmod-input-evdev
opkg install kmod-usb-hid
cat /dev/input/event1   | hexdump
```

- At this point you should see a hexdump when moving the mouse (leave with CTRL-C)
- Continue with
```
wget https://www.dropbox.com/s/ce44jh9udlubq01/python-evdev_0.4.7-1_ar71xx.ipk --no-check-certificate
opkg install python-evdev_0.4.7-1_ar71xx.ipk 
```

- See https://github.com/gvalkov/python-evdev/issues/34 for details on why to install evdev this way
- Install the mouse.ino sketch via Arduino IDE 
- Transfer mouse.py to the Yun (e.g. via WinSCP)
- Start forwarding via ``` python mouse.py ```



