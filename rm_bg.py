import os
from rembg import remove
from PIL import Image

# Input and output directory paths suraj
input_dir = 'input_images'  # Directory containing jpg images
output_dir = 'output_images'  # Directory to save the output png images

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    /suraj

# Process all jpg images in the input directory
for index, filename in enumerate(os.listdir(input_dir), start=1):
    if filename.endswith('.jpg'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f'image_{index}.png')

        # Open the input image
        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()
            output_data = remove(input_data)  # Remove the background

        # Save the output image as PNG with transparency
        with open(output_path, 'wb') as output_file:
            output_file.write(output_data)

        print(f'Processed {filename} -> {output_path}')
