# Add your Python code here. E.g.
from microbit import *
brightness = 10
while True:
    if button_a.is_pressed():
       
        brightness += 10
        pin0.write_analog(brightness) 
        if brightness == 1020:
            brightness = 0

    if button_b.is_pressed():
        brightness = 0
        pin0.write_analog(brightness) 
    sleep(100)
