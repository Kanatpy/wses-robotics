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

# Hello World!
<table>
  <tr>
    <td width="50%" valign="top">
      <strong>Web Editor</strong><br>
      <img src="week4/micropbit_recording_heart.gif" alt="Using a micro:bit" style="width:100%;">
    </td>
    <td width="50%" valign="top">
      <strong>The Python Code</strong>
      <div class="code-container">
        <button class="copy-btn" onclick="copyCode('code1', this)">Copy</button>
        <pre><code id="code1">from microbit import *

while True:
    display.show(Image.HEART)
    sleep(1000)
    display.scroll('Hello')</code></pre>
      </div>
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
      <div class="code-container">
        <button class="copy-btn" onclick="copyCode('code2', this)">Copy</button>
        <pre><code id="code2">from microbit import *

x = 2
y = 2

while True:
    display.clear()
    display.set_pixel(x, y, 9)
    
    if button_a.was_pressed():
        x = x - 1
        if x < 0: x = 4
        y = y - 1
        if y < 0: y = 4
            
    if button_b.was_pressed():
        x = x + 1
        if x > 4: x = 0
        y = y + 1
        if y > 4: y = 0
    
    sleep(10)</code></pre>
      </div>
    </td>
  </tr>
</table>

# Accelerometer!
<table>
  <tr>    
    <td width="50%" valign="top">
      <strong>The Python Code</strong>
      <div class="code-container">
        <button class="copy-btn" onclick="copyCode('code3', this)">Copy</button>
        <pre><code id="code3">from microbit import *

SENSITIVITY = 200
INTERVAL = 100
WINDOW_SIZE = 10
display_history = [0, 0, 0, 0, 0]
avg_buffer = []

while True:
    raw_reading = accelerometer.get_y()
    avg_buffer.append(raw_reading)
    if len(avg_buffer) > WINDOW_SIZE:
        avg_buffer.pop(0)
    
    current_avg = sum(avg_buffer) / len(avg_buffer)
    difference = raw_reading - current_avg
    val = int(difference / SENSITIVITY)
    magnitude = min(max(val, -2), 2)
    
    display_history.pop(0)
    display_history.append(magnitude)
    
    display.clear()
    for x in range(5):
        offset = display_history[x]
        display.set_pixel(x, 2, 5)
        if offset > 0:
            for y in range(2 - offset, 2):
                display.set_pixel(x, y, 9)
        elif offset < 0:
            for y in range(3, 3 - offset):
                display.set_pixel(x, y, 9)
    sleep(INTERVAL)</code></pre>
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