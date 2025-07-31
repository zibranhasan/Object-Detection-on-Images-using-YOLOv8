import cv2

from ultralytics import YOLO


# Load the model
model = YOLO('../Yolo-Weights/yolov8n.pt')

# Run detection
results = model("Images/3.png.jpg", show=True)
cv2.waitKey(0)
