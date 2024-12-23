import socket
import colorsys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
payload = b''
for i in range(1152):
    r, g, b = colorsys.hsv_to_rgb(i / 1152, 1, 1)
    payload += bytes([int(r * 255), int(g * 255), int(b * 255)])
sock.sendto(payload, ('100.91.88.116', 54321))
sock.close()