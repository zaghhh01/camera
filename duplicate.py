import os
from PIL import Image, ImageEnhance

# Function to adjust color
def adjust_color(image, factor):
    enhancer = ImageEnhance.Color(image)
    return enhancer.enhance(factor)

# Function to adjust brightness
def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

# Function to adjust orientation
def adjust_orientation(image, orientation):
    return image.transpose(orientation)

# Main function to process images
def process_images(input_folder, output_folder, color_factor=1.0, brightness_factor=1.0, orientation=Image.ROTATE_90, suffix='_modified'):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            # Open an image file
            with Image.open(os.path.join(input_folder, filename)) as img:
                # Apply color adjustment
                img = adjust_color(img, color_factor)

                # Apply brightness adjustment
                img = adjust_brightness(img, brightness_factor)

                # Apply orientation adjustment
                img = adjust_orientation(img, orientation)

                # Create the new filename
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}{suffix}{ext}"

                # Save the processed image to the output folder
                img.save(os.path.join(output_folder, new_filename))

# Example usage
input_folder = 'dataset\\unknown'
output_folder = 'duplicated images'
process_images(input_folder, output_folder, color_factor=1.6, brightness_factor=1.4, orientation=Image.ROTATE_180, suffix='_modified')
