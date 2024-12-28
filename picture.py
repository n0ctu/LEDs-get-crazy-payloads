import cv2
import socket

# Configuration
num_pixels = 1152
udp_ip = "ledsgc.luxeria.ch"    # Current IP address of the ledsgc matrix
udp_port = 54321            # Default port
canvas_height = 24
canvas_width = 48

def send_byte_array(byte_array):
    # Send UDP datagram
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(byte_array, (udp_ip, udp_port))
    #print(byte_array)
    sock.close()
    print(f"Sent bytearray to {udp_ip}:{udp_port}")

def send_pic(path):
    # Read and process the image
    image = cv2.imread(path)

    if image is None:
        print(f"Error: Could not open image {path}.")
        return

    # Calculate aspect ratio and resize dimensions
    height, width = image.shape[:2]
    aspect_ratio = width / height

    if aspect_ratio > (canvas_width / canvas_height):
        resize_height = int(canvas_width / aspect_ratio)
        resize_width = canvas_width
    else:
        resize_width = int(canvas_height * aspect_ratio)
        resize_height = canvas_height

    # Resize the image
    resized_image = cv2.resize(image, (resize_width, resize_height))

    # Crop the image to fit the LED matrix
    start_x = max(0, (resize_width - canvas_width) // 2)
    start_y = max(0, (resize_height - canvas_height) // 2)
    cropped_image = resized_image[start_y:start_y + canvas_height, start_x:start_x + canvas_width]

    # Convert to GRB format
    grb_image = cropped_image[:, :, [2, 1, 0]]

    # Convert to byte array
    byte_array = grb_image.tobytes()

    # Send the byte array to the LED matrix
    send_byte_array(byte_array)


# Example usage
send_pic("media/jenna.jpg")
