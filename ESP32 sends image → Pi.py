import torch
import cv2

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Open camera or image
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)

    # Process results
    for *box, conf, cls in results.xyxy[0]:
        label = model.names[int(cls)]

        # Detect elephant or large animals
        if label in ['elephant', 'cow', 'horse']:
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(frame, f"{label}", (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

            print("⚠️ ALERT: Large animal detected!")

    cv2.imshow("Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()