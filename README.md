# Object Detection Dataset and Training

This repository contains scripts to convert Pascal VOC format object detection dataset to CNN classification dataset for image classification purposes. The output dataset can used to train a model that classify images. The outputs are, cropped images along with their corresponding labels.

## Dataset
Use any dataset that is labeled using Pascal VOC format for object detection.
### Format

The dataset should be in Pascal VOC format, which includes XML annotation files for each image. The annotation files contain bounding box information and class labels.

### Directory Structure

- `train/`: This directory will contain the training images and corresponding XML annotation files in Pascal VOC format.

### Adding Your Dataset

1. Add your dataset images to the `train/` directory.
2. Ensure that each image has a corresponding XML annotation file in Pascal VOC format.

## Modify Path in `main.py`

The `main.py` file is the main script for executing the object detection process. Before running the script, make sure to modify the dataset path in the `main.py` file.

```python
# main.py

# Update the path to your dataset
dataset_path = "path/to/your/dataset/train"
```
