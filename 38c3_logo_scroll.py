import cv2
import socket
import time

# Configuration
udp_hostname_or_ip = "ledsgc.luxeria.ch"  # Current hostname or IP of the ledsgc matrix
udp_port = 54321  # Default port
scroll_horizontally = False  # True => scroll horizontally (from right to left); otherwise vertically (from bottom to top)
wait_time = 0.6  # Sleep time between frames (and hence higher speed the smaller the value)

# Read the image (with already correct dimensions)
im = cv2.imread("./media/38c3_logo.png")

# Get image dimensions (fit the LED matrix size)
im_height, im_width, _ = im.shape

# Reorder to RGB
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

def send_bytes_and_wait(data, wait_time):
    # Send new UDP datagram
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data, (udp_hostname_or_ip, udp_port))

    # Delay
    time.sleep(wait_time)


# Poor man's logo scrolling...
while True:
    if scroll_horizontally:
        for shift in range(0, im_width):
            # Shift the image (take parts and concatenate horizontally)
            im1 = im[0:im_height, 0+shift:im_width+shift]
            im2 = im[0:im_height, 0:shift]
            im_tx = cv2.hconcat([im1, im2])

            # Convert to bytes (3 bytes per pixel - RGB)
            data = im_tx.flatten().tobytes()
        
            send_bytes_and_wait(data, wait_time)
    else:
        for shift in range(0, im_height):
            # Shift the image (take parts and concatenate horizontally)
            im1 = im[0+shift:im_height, 0:im_width]
            im2 = im[0:shift, 0:im_width]
            im_tx = cv2.vconcat([im1, im2])

            # Convert to bytes (3 bytes per pixel - RGB)
            data = im_tx.flatten().tobytes()
        
            send_bytes_and_wait(data, wait_time)

# Clean up (won't happen; maybe should hook the termination)
sock.close()

