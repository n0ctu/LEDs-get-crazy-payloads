# LEDs-get-crazy Demo Payloads
Some demo payloads for the big LED matrix! Make the **1152 LEDs** your own 🎨

## Getting started

The protocol couldn't be simpler. The LED matrix listens for UDP packets on port 54321 and expects simple byte arrays. Each three bytes represent a single pixel (RGB). To illuminate the first pixel in red, simply send a UDP datagram consisting of `\xff\x00\x00`.

Let's turn on the first three pixels in red, green and blue:

```bash
echo -ne '\xff\x00\x00\x00\xff\x00\x00\x00\xff' | nc -u 151.217.233.92 54321
```

Easy, right? Now let's get crazier and create some random noise:

```bash
cat /dev/urandom | nc -u 151.217.233.92 54321
```

That was fun! But much more interesting things can be done with a little bit of structure. Python is the perfect tool for that. Let's start with a minimal example:

```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'\xff\x00\x00\x00\xff\x00\x00\x00\xff', ('151.217.233.92', 54321))
sock.close()
```

What about some more pixels? Let's create a rainbow:

```python
import socket
import colorsys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
payload = b''
for i in range(1152):
    r, g, b = colorsys.hsv_to_rgb(i / 1152, 1, 1)
    payload += bytes([int(r * 255), int(g * 255), int(b * 255)])
sock.sendto(payload, ('151.217.233.92', 54321))
sock.close()
```

Just imagine the possibilities! 🌈

Take a look at some more python examples in this repo to get a hang, then create even cooler things 😎 Feel free to make a pull request with your own payload!

## Offline Simulation

If you want to test your code offline before sending anything to the actual matrix, you may simulate it locally: https://github.com/nickik/ledsim

## Credits for contributions
- **webcam.py**: Stream your webcam to the matrix. Thanks [@rnestler](https://github.com/rnestler)!
- **Simulator:** [Test](https://github.com/nickik/ledsim) your payloads locally. Thanks [@nickik](https://github.com/nickik)