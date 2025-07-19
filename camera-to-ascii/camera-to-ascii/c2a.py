import cv2
import numpy as np
from PIL import Image
import os

# Function to convert a NumPy array to ASCII
def frame_to_ascii(frame, threshold=50):
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    aspect_ratio = frame.shape[0] / frame.shape[1] / 1.65
    new_width = 200
    new_height = int(aspect_ratio * new_width)
    image = image.resize((new_width, new_height))
    image = image.convert("L")

    # ASCII_CHARS = "@%#*+=-:. " # gpt given
    # ASCII_CHARS = "@#%]/>+-. " # my fav, highlight is 'filled'
    ASCII_CHARS = " .+<\\]%#@" # my fav inverse, highlight is 'unfilled'
    ascii_str = ""
    pixels = np.array(image).flatten()
    for pixel_value in pixels:
        if pixel_value < threshold:
            ascii_str += " "
        else:
            index = pixel_value * (len(ASCII_CHARS) - 1) // 255
            ascii_str += ASCII_CHARS[index]
        
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, new_width):
        ascii_img += ascii_str[i:i + new_width] + "\n"
        
    return ascii_img

# Function to convert ASCII text to an image
# Function to convert ASCII text to an image
def ascii_to_img(ascii_str, frame_shape):
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = np.zeros(frame_shape, dtype=np.uint8)
    
    lines = ascii_str.split('\n')
    line_count = len(lines)
    font_size = 0.25
    font_thickness = 1
    dy = 10  # Line spacing
    
    # Calculate the starting y-coordinate to center the ASCII art vertically
    total_text_height = line_count * dy
    y0 = (frame_shape[0] - total_text_height) // 2

    for i, line in enumerate(lines):
        y = y0 + i * dy
        cv2.putText(img, line, (20, y), font, font_size, (255, 255, 255), font_thickness, cv2.LINE_AA)
        
    return img


# Initialize the camera (0 refers to the default camera)
cap = cv2.VideoCapture(0)
# frame_shape = (480, 640, 3)  # Default shape, you may need to adjust this
frame_shape = None

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Dynamically retrieve the camera dimensions
    if frame_shape is None:
        frame_shape = (frame.shape[0], frame.shape[1], 3)
    
    # Convert frame to ASCII art
    ascii_art = frame_to_ascii(frame, threshold=50)  # You can change the threshold value
    img_frame = ascii_to_img(ascii_art, frame_shape)
    
    # Display the ASCII art frame
    cv2.imshow('ASCII Art Camera Feed', img_frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
