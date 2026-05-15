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


# Accelerometer!
<table>
  <tr>    
    <td width="50%" valign="top">
      <strong>The Python Code</strong>
      <div class="code-container">
        <button class="copy-btn" onclick="copyCode('code3', this)">Copy</button>
        <pre><code id="code3">
          
          from microbit import *


# Ensure the pull-down is set so the pin doesn't 'float'
pin0.write_analog(0)
pin0.set_pull(pin0.PULL_DOWN)
display.clear()

while True:
    if button_b.is_pressed():        
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
        # Explicitly write 0 to keep the motor off
        pin0.write_analog(0)
        display.clear()
    
    # Small sleep to keep the processor from running too hot
    sleep(10)
    
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
