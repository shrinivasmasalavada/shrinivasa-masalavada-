import torch
import cv2

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Load image
image_path = 'image.jpg'   # change your image path  
img = cv2.imread(image_path)zz

# Run detection 
results = model(img)

# Print results
results.print()

# Draw boxes on image
results.render()

# Show output
cv2.imshow("Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
