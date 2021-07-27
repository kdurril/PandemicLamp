# Installation Guide

This is a brief guide to downloading the Micropython firmware for the ESP-32
This guide is for Ubuntu 20.04. Adapt for your OS.


*download*
[Firmware for Generic ESP32 module](https://micropython.org/download/esp32/)

[Firmware for v1.16.bin)](https://micropython.org/resources/firmware/esp32-20210623-v1.16.bin)

[esptool.py](https://github.com/espressif/esptool)


##Flash
1) erase your existing data - this is permanent
```bash
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
```
2) flash the drive
Note in the following example, use the absolute path to your bin file
```bash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000  esp32-20210623-v1.16.bin
```

##Connect serial usb

Connect to a Micropython board via USB serial
find your port, if is often /dev/ttyUSB0
* picocom
  * apt install picocom
  * picocom /dev/ttyUSB -b115200

* rshell
  * create a virtual environment
  * pip install rshell
  * type rshell
  * connect serial /dev/ttyUSB0 115200
  * rshell --help 
  * repl
  * control d to exit
  * git clone https://github.com/dhylands/rshell

## Files
* boot.py
* main.py


## Connect via wifi
see ./demo/boot.py


