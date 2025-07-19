import cv2
from PIL import Image
import numpy as np
import os

# Function to convert a NumPy array to ASCII
def frame_to_ascii(frame):
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    aspect_ratio = frame.shape[0] / frame.shape[1] / 1.65
    new_width = 100
    new_height = int(aspect_ratio * new_width)
    image = image.resize((new_width, new_height))
    image = image.convert("L")
    
    ASCII_CHARS = "@%#*+=-:. "
    ascii_str = ""
    pixels = np.array(image).flatten()
    for pixel_value in pixels:
        index = pixel_value * (len(ASCII_CHARS) - 1) // 255
        ascii_str += ASCII_CHARS[index]
        
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, new_width):
        ascii_img += ascii_str[i:i + new_width] + "\n"
        
    return ascii_img

# Read video
video_path = "/Users/walkerhutchinson/Desktop/output_video.mp4"
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    ascii_art = frame_to_ascii(frame)
    os.system('clear')  # Clear terminal (this works on macOS and Linux, for Windows use 'cls')
    print(ascii_art)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
