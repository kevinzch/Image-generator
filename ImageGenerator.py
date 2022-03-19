#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
from os import listdir, path
from PIL import Image

# Enlarge scale factor
SCALE_FACTOR = 4

CONFIG_FILE_NAME = 'config.json'

overlay_image_path_list = []

class Configuration:
    template_file_path = ''
    input_folder_path = ''
    output_folder_path = ''

# Read configurations from config file
def get_configurations():
    # If application is a frozen exe
    if getattr(sys, 'frozen', False):
        app_path = path.dirname(sys.executable)
    # If application is a script file
    else:
        app_path = path.dirname(__file__)

    # Make config file path
    config_file_path = path.join(app_path, CONFIG_FILE_NAME)

    # Load customizable variables from config file
    with open(config_file_path, encoding='utf-8') as tmp_config_file:
        tmp_config_dict = json.load(tmp_config_file)

        Configuration.template_file_path = tmp_config_dict['Template file path']
        Configuration.input_folder_path = tmp_config_dict['Input folder path']
        Configuration.output_folder_path = tmp_config_dict['Output folder path']

# Read files from input folder
def read_overlay_images():
    local_overlay_files = listdir(Configuration.input_folder_path)

    for temp_file in local_overlay_files:
        overlay_image_path_list.append(path.join(Configuration.input_folder_path, temp_file))

# Generate images
def generate_images():
    local_cnt = 0

    for temp_path in overlay_image_path_list:
        # Open template image
        img_template = Image.open(Configuration.template_file_path)

        # Open overlay image
        img_overlay = Image.open(temp_path)

        # Enlarge header to 400%
        img_overlay_resize = img_overlay.resize((img_overlay.width * SCALE_FACTOR, img_overlay.height * SCALE_FACTOR))

        # Paste header image at the center of template image
        img_template.paste(img_overlay_resize, (img_template.width // 2 - img_overlay_resize.width // 2, img_template.height // 2 - img_overlay_resize.height // 2))

        # Save image
        img_template.save(path.join(Configuration.output_folder_path, "image" + str(local_cnt) + ".jpg"))

        local_cnt = local_cnt + 1

if __name__ == "__main__":
    get_configurations()
    read_overlay_images()
    generate_images()