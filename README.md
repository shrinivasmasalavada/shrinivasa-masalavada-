from ultralytics import YOLO
import cv2

# 1. Load a pre-trained YOLOv8 model (n is for 'nano', which is fast)
model = YOLO('yolov8n.pt')

# 2. Run inference on an image
# Replace 'path/to/your/image.jpg' with your actual file path
results = model('image.jpg')

# 3. Visualize the results
for r in results:
    # This will show the image with bounding boxes and labels
    r.show()

    # Optional: Save the resulting image to disk
    r.save(filename='detected_result.jpg')
