# Add your Python code here. E.g.
from microbit import *
brightness = 100
while True:
    if button_a.is_pressed():
        if brightness <= 1000:
            pin0.write_analog(brightness) 
            brightness += 100
        else:
            brightness = 100
            pin0.write_analog(brightness) 

       

    if button_b.is_pressed():
        brightness = 0
        pin0.write_analog(brightness) 
    sleep(100)
