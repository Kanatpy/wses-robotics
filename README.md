<a href="https://python.microbit.org/v/3" target="_blank">Click here for the micro:bit Web Programmer to open in a new tab</a>
<a href="https://makecode.microbit.org/" target="_blank">Click here if you want to program using Blocks!</a>


# Hello World!
<table>
  <tr>
    <td width="50%" valign="top">
      <strong>Web Editor</strong><br>
      <img src="week4/micropbit_recording_heart.gif" alt="Using a micro:bit" style="width:100%;">
    </td>
    <td width="50%" valign="top">
      <strong>The Python Code</strong>
      <pre><code>
        # Imports go at the top
        from microbit import *


        # Code in a 'while True:' loop repeats forever
        while True:
            display.show(Image.HEART)
            sleep(1000)
            display.scroll('Hello')
          
      </code></pre>
    </td>
  </tr>
</table>


# Using Switches
<table>
  <tr>
    <td width="50%" valign="top">
      <strong>Web Editor</strong><br>
      <img src="week4/micropbit_recording_switch.gif" alt="Using a micro:bit" style="width:100%;">
    </td>
    <td width="50%" valign="top">
      <strong>The Python Code</strong>
      <pre><code>
        # Imports go at the top
        from microbit import *


        # Code in a 'while True:' loop repeats forever
        while True:
            display.show(Image.HEART)
            sleep(1000)
            display.scroll('Hello')
          
      </code></pre>
    </td>
  </tr>
</table>



# Accelerometer!
<table>
  <tr>    
    <td width="50%" valign="top">
      <strong>The Python Code</strong>
      <pre><code>
        from microbit import *

        # Configuration
        SENSITIVITY = 200  # Lowered because differences are often smaller than raw values
        INTERVAL = 100
        WINDOW_SIZE = 10   # Number of samples for the moving average

        # History for the display (5 columns)
        display_history = [0, 0, 0, 0, 0]

        # History for the moving average calculation
        avg_buffer = []

        while True:
            # 1. Sample raw acceleration
            raw_reading = accelerometer.get_y()
            
            # 2. Update moving average buffer
            avg_buffer.append(raw_reading)
            if len(avg_buffer) > WINDOW_SIZE:
                avg_buffer.pop(0)
            
            # 3. Calculate the average and find the difference
            current_avg = sum(avg_buffer) / len(avg_buffer)
            difference = raw_reading - current_avg
            
            # 4. Map the difference to -2 to +2 range
            val = int(difference / SENSITIVITY)
            magnitude = min(max(val, -2), 2)
            
            # 5. Shift display history
            display_history.pop(0)
            display_history.append(magnitude)
            
            # 6. Render the center-zero graph
            display.clear()
            for x in range(5):
                offset = display_history[x]
                
                # Draw center line
                display.set_pixel(x, 2, 5) # Dimmer center line for contrast
                
                # Draw positive bars
                if offset > 0:
                    for y in range(2 - offset, 2):
                        display.set_pixel(x, y, 9)
                
                # Draw negative bars
                elif offset < 0:
                    for y in range(3, 3 - offset):
                        display.set_pixel(x, y, 9)
                        
            sleep(INTERVAL)
          
      </code></pre>
    </td>
  </tr>
</table>




# Servo Control
<table>
  <tr>
    <td width="50%" valign="top">      
      <strong>The Circuit</strong>
      <img src="week3/servo_circuit_image.png" alt="Servo Control" style="width:100%;">      
    </td>
    <td width="50%" valign="top">
      <strong>The Python Code</strong>
      <pre><code>
        from machine import Pin, PWM
        import time
        
        # SER0006 signal on GP28
        servo = PWM(Pin(28))
        servo.freq(50)  # Standard servo frequency: 50 Hz
        
        # Switches (active-low with internal pull-up)
        sw_inc = Pin(16, Pin.IN, Pin.PULL_UP)  # Increase angle
        sw_dec = Pin(15, Pin.IN, Pin.PULL_UP)  # Decrease angle
        
        MIN_ANGLE = 0
        MAX_ANGLE = 180
        STEP = 5
        angle = 90
          
        def angle_to_duty_u16(deg):
            # Map 0..180 deg to 500..2500 us pulse width at 50 Hz.
            min_us = 500
            max_us = 2500
            pulse_us = min_us + (max_us - min_us) * deg // 180
            return int(pulse_us * 65535 / 20000)
        
        def set_angle(deg):
            servo.duty_u16(angle_to_duty_u16(deg))
        set_angle(angle)
        
        while True:
            changed = False
        
            if sw_inc.value() == 0 and angle < MAX_ANGLE:
                angle += STEP
                if angle > MAX_ANGLE:
                    angle = MAX_ANGLE
                changed = True
        
                # Wait for button release (debounce / single step per press)
                while sw_inc.value() == 0:
                    time.sleep_ms(10)
        
            if sw_dec.value() == 0 and angle > MIN_ANGLE:
                angle -= STEP
                if angle < MIN_ANGLE:
                    angle = MIN_ANGLE
                changed = True
        
                # Wait for button release (debounce / single step per press)
                while sw_dec.value() == 0:
                    time.sleep_ms(10)
        
            if changed:
                set_angle(angle)
        
            time.sleep_ms(20)
      </code></pre>
    </td>
  </tr>
</table>

<a href="https://www.flaticon.com/free-icons/robot" title="robot icons">Robot icons created by kliwir art - Flaticon</a>



