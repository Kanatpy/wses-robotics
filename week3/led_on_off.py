from machine import Pin
import time

button = Pin(16, Pin.IN, Pin.PULL_UP)
led_red = Pin(15, Pin.OUT)
# Turn off all LEDs first
led_red.off()
    
led_state = 1
while True:
    # Read the value of button
    # 1: Button is not pressed
    # 0: Button is pressed
    button_state = button.value()
    
    if button_state == 0:  # Button pressed
        if led_state == 1: # LED was already ON
            led_red.off() # Turn OFF LED
            led_state = 0 
        else: # LED was already OFF
            led_red.on() # Turn ON LED
            led_state = 1
        
        # Wait until button is released to avoid repeated toggles
        while button.value() == 0:
            time.sleep(0.01)
