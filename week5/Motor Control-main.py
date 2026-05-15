from microbit import *

# --- INITIALIZATION ---
# Force Pin 0 to 0 immediately to close the transistor 'gate'
pin0.write_analog(0)
# Ensure the pull-down is set so the pin doesn't 'float'
pin0.set_pull(pin0.PULL_DOWN)
display.clear()

while True:
    if button_b.is_pressed():
        # --- START MOTOR SEQUENCE ---
        count = 0
        # Ramp up from 0 to 1023
        for speed in range(0, 1024, 41): 
            # If user lets go during the ramp, jump to the 'else' (stop)
            if not button_a.is_pressed():
                break
            
            pin0.write_analog(speed)
            
            # LED Progress Bar Logic
            y = count // 5
            x = count % 5
            display.set_pixel(x, y, 9)
            
            count += 1
            sleep(40) 
        
        # Hold full speed as long as button is held
        while button_a.is_pressed():
            pin0.write_analog(1023)
            
    else:
        # --- IDLE STATE (OFF) ---
        # Explicitly write 0 to keep the motor off
        pin0.write_analog(0)
        display.clear()
    
    # Small sleep to keep the processor from running too hot
    sleep(10)