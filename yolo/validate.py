from ultralytics import YOLO

if __name__ == '__main__':      # wrappa dentro main() se no Windows goes ape
    # Load a model
    model = YOLO("runs/detect/train4/weights/best.pt")  # load a custom model

    # Validate the model
    metrics = model.val(split="test")  # no arguments needed, dataset and settings remembered
    metrics.box.map  # map50-95
    metrics.box.map50  # map50
    metrics.box.map75  # map75
    metrics.box.maps  # a list contains map50-95 of each category