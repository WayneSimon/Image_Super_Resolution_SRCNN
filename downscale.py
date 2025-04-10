#Basic script for downsclaing HR images to create completed dataset for traing
import os
from PIL import Image
import numpy as np

# Change directories based on where saving training data
HR_PATH = r'SCNN Project\DIV2K_HR'
LR_PATH = r'SCNN Project\DIV2K_LR'
SCALE_FACTOR = 10              #Can change scale factor based on amount choosing to upsacle

os.makedirs(LR_PATH, exist_ok=True)

def downscale_image(image, scale_factor):
    width, height = image.size
    new_width = width // scale_factor
    new_height = height // scale_factor
    return image.resize((new_width, new_height), Image.BICUBIC)

def process_map_images():
    for filename in os.listdir(HR_PATH):
        if filename.endswith('.png') or filename.endswith('.jpg'): #jpg or png based on input images
            hr_image_path = os.path.join(HR_PATH, filename)
            hr_image = Image.open(hr_image_path)
            
            hr_save_path = os.path.join(HR_PATH, filename)
            hr_image.save(hr_save_path)
            
            lr_image = downscale_image(hr_image, SCALE_FACTOR)
            
            lr_save_path = os.path.join(LR_PATH, filename)
            lr_image.save(lr_save_path)
            
            print(f'Processed {filename} -> {filename}')

if __name__ == "__main__":
    process_map_images()
    print("Map dataset preparation completed.")


