# wses-robotics
## Adding Switch
### Circuit Diagram
<table>
  <tr>
    <td width="50%" valign="top">
      <h3>The Circuit</h3>
      <img src="week3/switch_circuit_image.png" alt="Using a Switch" style="width:100%;">
    </td>
    <td width="50%" valign="top">
      <h3>The Python Code</h3>

```python
import machine
import time

# Setup the switch on Pin 14
switch = machine.Pin(14, machine.Pin.IN)

while True:
    if switch.value() == 1:
        print("Switch is ON!")
    time.sleep(0.1)
```
</td>
  </tr>
</table>
### Code 

## Servo Control
