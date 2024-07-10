import os
import yaml
from ultralytics import YOLO
from pathlib import Path

if __name__ == '__main__':
    
    model = YOLO("yolov8m.yaml")  # build a new model from YAML
    model = YOLO("yolov8m.pt")  # load a pretrained model (recommended for training)
    model = YOLO("yolov8m.yaml").load("yolov8m.pt")  # build from YAML and transfer weights

    results = model.train(data= Path("euro/data.yaml").resolve().as_posix(), epochs=1, imgsz=32)

    # Print results
    print(results)
