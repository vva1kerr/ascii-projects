from PIL import Image
import os

# Function to convert image to ASCII
def image_to_ascii(image_path, root_path, file_name, save_to_file=True, threshold=50):
    # Step 1: Load the image
    image = Image.open(image_path).convert("RGBA")

    # Step 2: Resize the image
    width, height = image.size
    aspect_ratio = height / width / 1.65  # Adjust this value to correct for the non-square characters
    new_width = 100  # You can change this value
    new_height = int(aspect_ratio * new_width)
    image = image.resize((new_width, new_height))

    # Step 3: Convert to grayscale and handle transparency
    # ASCII_CHARS = "@%#*+=-:. "
    ASCII_CHARS = " .:-=+*#%@"
    ascii_str = ""
    pixels = image.getdata()
    for pixel in pixels:
        r, g, b, a = pixel
        if a == 0:
            ascii_str += " "
        else:
            gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            if gray < threshold:
                ascii_str += " "
            else:
                index = gray * (len(ASCII_CHARS) - 1) // 255
                ascii_str += ASCII_CHARS[index]

    # Organize the string into lines to match the image dimensions
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, new_width):
        ascii_img += ascii_str[i:i + new_width] + "\n"

    # Create the full path for the output file
    full_path = os.path.join(root_path, file_name)

    if save_to_file:
        # Save the ASCII image
        with open(full_path, "w") as f:
            f.write(ascii_img)
    else:
        # Print the ASCII image
        print(ascii_img)

# Example usage
image_path = "/Users/walkerhutchinson/Downloads/IMG_4366 (5).png"
root_path = "/Users/walkerhutchinson/Desktop"  # Replace with the path to your desktop or any other directory
file_name = "ascii_image.txt"

# To save to file
image_to_ascii(image_path, root_path, file_name, save_to_file=True, threshold=0)

# To print to terminal (uncomment the line below if you want to print)
# image_to_ascii(image_path, root_path, file_name, save_to_file=False, threshold=50)
