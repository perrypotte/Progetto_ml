from ultralytics import YOLO
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv(".env",override=True)


if __name__ == '__main__':      # Per evitare problemi di multithreading. fonte: yolo docs

    model = YOLO(os.getenv("PATH_YOLO_BEST"))  # load a custom model

    # Validate the model
    metrics = model.val(data= Path(os.getenv("PATH_YAML")).resolve().as_posix(),split="test")  # no arguments needed, dataset and settings remembered
    metrics.box.map  # map50-95
    metrics.box.map50  # map50
    metrics.box.map75  # map75
    metrics.box.maps  # a list contains map50-95 of each category