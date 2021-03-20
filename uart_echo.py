#Micropython ESP32 UART demo
#Any character received by the ESP32 is echoed back
from machine import UART
uart = UART(2, 9600)
uart.init(9600, bits=8, parity=None, stop=1, tx=17, rx=13)
uart.read()

while True:
    if uart.any() != 0:
        uart.write(uart.read())