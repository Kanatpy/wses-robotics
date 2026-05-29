<!-- Styles for the copy button -->
<style>
  .code-container {
    position: relative;
    background: #f4f4f4;
    padding: 10px;
    border-radius: 4px;
  }
  .copy-btn {
    position: absolute;
    top: 5px;
    right: 5px;
    padding: 5px 10px;
    font-size: 12px;
    cursor: pointer;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 3px;
  }
  .copy-btn:hover {
    background-color: #0056b3;
  }
  pre {
    margin: 0;
    white-space: pre-wrap;
    word-wrap: break-word;
  }
</style>

<a href="https://python.microbit.org/v/3" target="_blank">Click here for the micro:bit Web Programmer to open in a new tab</a>
<p></p>
<a href="https://makecode.microbit.org/" target="_blank">Click here if you want to program using Blocks!</a>

# Circuit Diagram
<a href="https://app.cirkitdesigner.com/project/d3682d71-2df9-41ce-a4b0-2a48508eead1" target="_blank"> Link to cirkidesigner!</a>
<img src="week5/circuit_image.png" alt="Circuit Diagram" style="width:100%;">


# Remote Control!
<table>
  <tr>    
    <td width="50%" valign="top">
      <strong>The Python Code</strong>
      <div class="code-container">
        <button class="copy-btn" onclick="copyCode('code3', this)">Copy</button>
        <pre><code id="code3">
          
from microbit import *
import radio

# Turn on the radio and set a channel (must match the car)**
channel_no = 7
radio.on()
radio.config(channel=channel_no)

# Default values
steering = "center"

while True:
    # 1. Handle Steering Input (Buttons)
    if button_a.is_pressed() and button_b.is_pressed():
        steering = "center"
    elif button_a.is_pressed():
        steering = "left"
    elif button_b.is_pressed():
        steering = "right"
        
    # 2. Handle Speed Input (Tilt Forward/Backward)
    # y-axis gives negative values when tilted forward, positive when backward
    tilt_y = accelerometer.get_y()
    
    # Map the tilt to a speed scale (0 to 100)
    # We only care about tilting forward to go forward for this simple code
    if tilt_y < -200:
        # Convert negative tilt into a positive speed value (max ~100)
        speed = min(100, abs(tilt_y) // 10)
    else:
        speed = 0 # Stop if level or tilted backward
        
    # 3. Send the data as a string (e.g., "left,50")
    command = "{},{}".format(steering, speed)
    radio.send(command)
    
    # Brief pause to keep the radio clear
    sleep(50)
    
    </code></pre>
      </div>
    </td>
  </tr>
</table>


# Car Control!
<table>
  <tr>    
    <td width="50%" valign="top">
      <strong>The Python Code</strong>
      <div class="code-container">
        <button class="copy-btn" onclick="copyCode('code3', this)">Copy</button>
        <pre><code id="code3">
          
from microbit import *
import radio

# Turn on the radio and match the channel
channel_no = 7
radio.on()
radio.config(channel=channel_no)

# Set initial PWM periods
# Servos standardly require a 20ms (20000 microseconds) period
pin1.set_analog_period_microseconds(20000) 

# Helper function to map servo angles (0 to 180 degrees) 
# into MicroPython's 0-1023 duty cycle
def set_servo_angle(pin, angle):
    # Standard servo duty cycle ranges roughly from 50 (0°) to 115 (180°)
    duty = int(50 + (angle / 180) * 65)
    pin.write_analog(duty)

# Initialize car states
set_servo_angle(pin1, 90) # Center the steering
pin0.write_analog(0)      # Stop the motor

while True:
    # Check for incoming radio messages
    message = radio.receive()
    
    if message:
        try:
            # Split the incoming string "steering,speed"
            steering, speed_str = message.split(",")
            speed_pct = int(speed_str)
            
            # 1. Control the Servo (Pin 1)
            if steering == "left":
                set_servo_angle(pin1, 45)  # Turn Left
            elif steering == "right":
                set_servo_angle(pin1, 135) # Turn Right
            else:
                set_servo_angle(pin1, 90)  # Straight
                
            # 2. Control the DC Motor Speed via PWM (Pin 0)
            # Map 0-100% speed to MicroPython's 0-1023 analog range
            pwm_value = int((speed_pct / 100) * 1023)
            pin0.write_analog(pwm_value)
            
        except ValueError:
            # Ignore corrupted or incomplete radio packets
            pass
            
    sleep(20)
    
    </code></pre>
      </div>
    </td>
  </tr>
</table>



<!-- JavaScript for the copy functionality -->
<script>
  function copyCode(id, btn) {
    const code = document.getElementById(id).innerText;
    navigator.clipboard.writeText(code).then(() => {
      const originalText = btn.innerText;
      btn.innerText = "Copied!";
      btn.style.backgroundColor = "#28a745";
      setTimeout(() => {
        btn.innerText = originalText;
        btn.style.backgroundColor = "#007bff";
      }, 2000);
    });
  }
</script>
