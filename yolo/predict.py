from ultralytics import YOLO

# Load a model
model = YOLO("runs/detect/train4/weights/best.pt")  # pretrained YOLOv8n model

# Run batched inference on a list of images
results = model(["C:/Users/doger/ml_munny/euro/test/images/train_38_33_jpg.rf.71d3f29908539bf2354fd1272f3c3e7e.jpg"], stream=True)  # return a generator of Results objects

# Process results generator
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    # result.save(filename="result.jpg")  # save to disk