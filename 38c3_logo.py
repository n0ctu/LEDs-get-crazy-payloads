import cv2
import socket

# Configuration
num_pixels = 1152  # unused, but still true
udp_hostname = "ledsgc.luxeria.ch"  # Current hostname of the ledsgc matrix
udp_port = 54321 # Default port

# Read the image (with already correct dimensions)
im = cv2.imread("./media/38c3_logo.png")

# Reorder to RGB
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

# Convert to bytes (3 bytes per pixel - RGB)
data = im.flatten().tobytes()

# Send UDP datagram
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(data, (udp_hostname, udp_port))
sock.close()

