#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
from os import listdir, path
from PIL import Image

CONFIG_FILE_NAME = 'config.json'

global_file_info_list = []

class Configuration:
    background_file_path = ''
    input_folder_path = ''
    output_folder_path = ''
    scale_factor = ''

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

        Configuration.background_file_path = tmp_config_dict['Background file path']
        Configuration.input_folder_path = tmp_config_dict['Input folder path']
        Configuration.output_folder_path = tmp_config_dict['Output folder path']
        Configuration.scale_factor = int(tmp_config_dict['Scale factor'])

# Read files from input folder
def read_input_images():
    # Get the list of image file names in the input folder
    local_input_images = [f for f in listdir(Configuration.input_folder_path) if '.jpg' in path.join(Configuration.input_folder_path, f)]

    for temp_input_image in local_input_images:
        tmp_file_info_list = []

        # Add image file name
        tmp_file_info_list.append(temp_input_image)

        # Add image file path
        tmp_file_info_list.append(path.join(Configuration.input_folder_path, temp_input_image))

        # Add image file information to global list: [file name][full file path]
        global_file_info_list.append(tmp_file_info_list)

# Generate images
def generate_images():
    for tmp_file_info_list in global_file_info_list:
        # Open background image
        tmp_background = Image.open(Configuration.background_file_path)

        # Open input image
        tmp_input_image = Image.open(tmp_file_info_list[1])

        # Resize input image
        tmp_input_image_resized = tmp_input_image.resize((tmp_input_image.width * Configuration.scale_factor, tmp_input_image.height * Configuration.scale_factor))

        # Put input image at the center of background image
        tmp_background.paste(tmp_input_image_resized, (tmp_background.width // 2 - tmp_input_image_resized.width // 2, tmp_background.height // 2 - tmp_input_image_resized.height // 2))

        # Save image with input image name
        tmp_background.save(path.join(Configuration.output_folder_path, tmp_file_info_list[0]))

if __name__ == "__main__":
    get_configurations()
    read_input_images()
    generate_images()