from PIL import Image
import os
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def resize_images(folder_path="images", width=512, height=512, resized_path="resized"):
    """
    Resizes images in a folder and moves the resized images to a new folder.

    Args:
        folder_path (str): The path to the folder containing the images.
        width (int): The desired width of the resized images.
        height (int): The desired height of the resized images.
        resized_path (str): The path to the folder where resized images will be moved.
    """
    try:
        # Create resized folder if it doesn't exist
        if not os.path.exists(resized_path):
            os.makedirs(resized_path)

        # Resize images
        for file in os.listdir(folder_path):
            if file.endswith((".jpg", ".png")):
                img_path = os.path.join(folder_path, file)
                try:
                    img = Image.open(img_path)
                    img = img.resize((width, height))
                    resized_file = "resized_" + file
                    resized_img_path = os.path.join(folder_path, resized_file)
                    img.save(resized_img_path)
                    logging.info(f"Resized {file} to {width}x{height}")
                except Exception as e:
                    logging.error(f"Error processing {file}: {e}")

        # Move resized images
        for file in os.listdir(folder_path):
            if file.startswith("resized_"):
                try:
                    shutil.move(os.path.join(folder_path, file), resized_path)
                    logging.info(f"Moved {file} to {resized_path}")
                except Exception as e:
                    logging.error(f"Error moving {file}: {e}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    resize_images()