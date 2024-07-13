import os
from ultralytics import YOLO
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(".env",override=True)

if __name__ == '__main__':
    
    model = YOLO("yolov8m.yaml").load("yolov8m.pt")  # build from YAML and transfer weights

    results = model.train(data= Path(os.getenv("PATH_YAML")).resolve().as_posix(), epochs=300, imgsz=640)

    #print(results)
