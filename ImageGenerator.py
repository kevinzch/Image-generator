from os import listdir, path
from PIL import Image

# Enlarge scale factor
SCALE_FACTOR = 4

# Input folder path
# Put overlay images here
PATH_INPUT_FOLDER = r"D:\01_Dev\image-generator\input"

# Output folder path
# Generated images will be saved here
PATH_OUTPUT_FOLDER = r"D:\01_Dev\image-generator\output"

overlay_image_path_list = []

# Read files from input folder
def read_overlay_images():
    local_overlay_files = listdir(PATH_INPUT_FOLDER)

    for temp_file in local_overlay_files:
        overlay_image_path_list.append(path.join(PATH_INPUT_FOLDER, temp_file))

# Generate images
def generate_images():
    local_cnt = 0

    for temp_path in overlay_image_path_list:
        # Open template image
        img_template = Image.open(r"D:\01_Dev\image-generator\template.jpg")

        # Open overlay image
        img_overlay = Image.open(temp_path)

        # Enlarge header to 400%
        img_overlay_resize = img_overlay.resize((img_overlay.width * SCALE_FACTOR, img_overlay.height * SCALE_FACTOR))

        # Paste header image at the center of template image
        img_template.paste(img_overlay_resize, (img_template.width // 2 - img_overlay_resize.width // 2, img_template.height // 2 - img_overlay_resize.height // 2))

        # Save image
        img_template.save(path.join(PATH_OUTPUT_FOLDER, "image" + str(local_cnt) + ".jpg"))

        local_cnt = local_cnt + 1

if __name__ == "__main__":
    read_overlay_images()
    generate_images()