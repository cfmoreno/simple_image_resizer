# Image Resizer Script

This script resizes images in a specified folder and moves the resized images to a separate folder.

## Requirements

1.  Python 3.7 or higher.
2.  Install the required Python packages using pip:
    ```bash
    pip install Pillow
    ```

## How to Use

1.  **Clone the Repository:** Clone this repository to your local machine.
2.  **Place Images:** Place the images you want to resize in the `images` folder (create it if it doesn't exist).
3.  **Run the Script:** Execute the `image_resizer.py` script from the root folder:
    ```bash
    python image_resizer.py
    ```
4.  **View Resized Images:** The resized images will be available in the `resized` folder.

## Customization

* **Image Dimensions:** Modify the `width` and `height` variables in the `resize_images` function to change the dimensions of the resized images.
* **Folder Paths:** Change the `folder_path` and `resized_path` variables to specify different input and output folders.
* **Error Handling:** Enhance error handling by catching specific exceptions and providing more informative error messages.
* **Logging:** Implement logging to record script activity and errors.