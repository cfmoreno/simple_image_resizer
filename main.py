from PIL import Image
import os
import shutil

# Set desired Width and Height (In Pixels):

width = 512
height = 512

# Set images folder
folder_path = "images"

# Loop through the files in the folder
for file in os.listdir(folder_path):
    # Check if the file is an image
    if file.endswith(".jpg") or file.endswith(".png"):
        # Open the image file
        img = Image.open(os.path.join(folder_path, file))
        # Resize the image to 512 x 512 pixels
        img = img.resize((width, height))
        # Save the resized image as a new file
        img.save(os.path.join(folder_path, "resized_" + file))

# Set Resized images folder        
resized_path = "resized"

# For the resized images, move them to the resized folder:

for file in os.listdir(folder_path):
    # Check if the file starts with resized_
    if file.startswith("resized_"):
        # Copy the file to the resized folder
        shutil.copy(os.path.join(folder_path, file), resized_path)
        # Delete the file from the original folder
        os.remove(os.path.join(folder_path, file)) 