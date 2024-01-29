import cv2
import numpy as np
import os
from xml.etree import ElementTree as ET

def extract_images(input_folder, output_folder):
    # Create the output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each XML file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".xml"):
            xml_path = os.path.join(input_folder, filename)

            # Parse the XML file to extract bounding box information
            tree = ET.parse(xml_path)
            root = tree.getroot()

            # Read image path and load the image
            image_path = os.path.join(input_folder, root.find("filename").text)
            image = cv2.imread(image_path)

            for obj in root.findall(".//object"):
                class_name = obj.find("name").text
                bbox = obj.find("bndbox")

                xmin = int(bbox.find("xmin").text)
                ymin = int(bbox.find("ymin").text)
                xmax = int(bbox.find("xmax").text)
                ymax = int(bbox.find("ymax").text)

                # Crop and save the image within the bounding box
                cropped_image = image[ymin:ymax, xmin:xmax]

                # Determine the output filename, check for existing files, and increment index if necessary
                base_filename = f"{class_name}.jpg"
                output_path = os.path.join(output_folder, base_filename)

                index = 1
                while os.path.exists(output_path):
                    # If the file already exists, increment the index
                    base_filename = f"{class_name}_{index}.jpg"
                    output_path = os.path.join(output_folder, base_filename)
                    index += 1

                cv2.imwrite(output_path, cropped_image)

if __name__ == "__main__":
    input_folder = "train"
    output_folder = "classification_dataset"

    extract_images(input_folder, output_folder)
