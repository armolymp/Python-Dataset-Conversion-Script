import os
import cv2
import numpy as np

images = []
labels = []
dataset_folder = "Dataset_conversion_scripts/classification_dataset"

for filename in os.listdir(dataset_folder):
    if filename.endswith(".jpg"):
        image_path = os.path.join(dataset_folder, filename)
        class_name, _ = os.path.splitext(filename)
        label = ''.join(filter(str.isalpha, class_name))  # Remove non-alphabetic characters

        # Load and preprocess the image
        img = cv2.imread(image_path)
        img = cv2.resize(img, (224, 224))  # Adjust size as needed
        img = img / 255.0  # Normalize pixel values to the range [0, 1]

        images.append(img)
        labels.append(label)

print(np.array(labels))
