import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Sends three pixels, red, green, and blue
sock.sendto(b'\xff\x00\x00\x00\xff\x00\x00\x00\xff', ('100.91.88.116', 54321))
sock.close()
