import cv2
import socket
import time

# Configuration
num_pixels = 1152
udp_ip = "100.91.88.116"   # Current IP address of the ledsgc matrix
udp_port = 54321           # Default port

def send_byte_array(byte_array):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(byte_array, (udp_ip, udp_port))
    # Close the socket
    sock.close()

def video_to_grb_byte_array(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Read the frame rate and calculate the frame interval
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = 1 / fps  # Frame interval in seconds
    print(f"Frame Rate: {fps} FPS")

    # Process each frame
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Rotate the frame by 90 degrees
        rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

        # Resize frame to 24x48
        resized_frame = cv2.resize(rotated_frame, (24, 48))

        # Convert to GRB format
        grb_frame = resized_frame[:, :, [1, 2, 0]]

        # Convert to byte array
        byte_array = grb_frame.tobytes()

        # Send the byte array to the LED strip
        send_byte_array(byte_array)

        # Wait for the frame interval before processing the next frame
        time.sleep(frame_interval)

    cap.release()

# Example usage
while True:
    video_to_grb_byte_array("media/luxeria.mp4")