import time
from machine import Pin
red=Pin(20,Pin.OUT) #red.value(1)
green=Pin(15,Pin.OUT) #green.value(1)

while True:
    green.value(1)
    time.sleep(0.5)
    red.value(1)
    time.sleep(0.5)
    green.value(0)
    time.sleep(0.5)
    red.value(0)
    time.sleep(0.5)
