from PIL import Image
import os

def compress_image(input_path, output_folder, compression_percentage, compress_width):
    with Image.open(input_path) as img:
        if compress_width:
            # Calculate the new width based on the compression percentage
            new_width = int(img.width * (1 - compression_percentage / 100))
            new_size = (new_width, img.height)
        else:
            # Calculate the new height based on the compression percentage
            new_height = int(img.height * (1 - compression_percentage / 100))
            new_size = (img.width, new_height)

        # Resize the image with the new dimensions
        compressed_img = img.resize(new_size, Image.ANTIALIAS)

        # Save the compressed image, overwriting the original
        compressed_img.save(os.path.join(output_folder, os.path.basename(input_path)))

# Replace '/Users/sjohal/Desktop/Python/Z-Game/graphics/weapons/axe' with your input folder path
input_folder = '/Users/sjohal/Desktop/Python/Z-Game/graphics/weapons/rapier'
output_folder = '/Users/sjohal/Desktop/Python/Z-Game/graphics/weapons/rapier'
compression_percentage = 25

# Process each input file in the specified folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('up.png', 'down.png')):
        compress_image(os.path.join(input_folder, filename), output_folder, compression_percentage, compress_width=True)
    elif filename.lower().endswith(('left.png', 'right.png')):
        compress_image(os.path.join(input_folder, filename), output_folder, compression_percentage, compress_width=False)
