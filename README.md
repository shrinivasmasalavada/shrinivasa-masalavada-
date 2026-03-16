import cv2
from ultralytics import YOLO

# 1. YOLOv8 ಮಾಡೆಲ್ ಲೋಡ್ ಮಾಡಿ (ಸಣ್ಣದಾದ ಮತ್ತು ವೇಗವಾದ 'nano' ಮಾಡೆಲ್)
model = YOLO('yolov8n.pt')

# 2. ವೆಬ್‌ಕ್ಯಾಮ್ ಆರಂಭಿಸಿ (0 ಎಂದರೆ ಡಿಫಾಲ್ಟ್ ಕ್ಯಾಮೆರಾ)
cap = cv2.VideoCapture(0)

print("ಕ್ಯಾಮೆರಾ ಆರಂಭವಾಗುತ್ತಿದೆ... ಮುಚ್ಚಲು 'q' ಒತ್ತಿರಿ.")

while cap.isOpened():
    # ಕ್ಯಾಮೆರಾದಿಂದ ಫ್ರೇಮ್ ಓದಿ
    success, frame = cap.read()

    if success:
        # 3. ಆಬ್ಜೆಕ್ಟ್ ಡಿಟೆಕ್ಷನ್ ನಡೆಸಿ
        results = model(frame)

        # 4. ರಿಸಲ್ಟ್ ಅನ್ನು ಫ್ರೇಮ್ ಮೇಲೆ ಬಿಡಿಸಿ (Annotate)
        annotated_frame = results[0].plot()

        # ಪ್ರದರ್ಶಿಸಿ
        cv2.imshow("YOLOv8 Real-Time Detection", annotated_frame)

        # 'q' ಒತ್ತಿದರೆ ಲೂಪ್ ನಿಲ್ಲಿಸಿ
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# ಎಲ್ಲವನ್ನೂ ಕ್ಲೋಸ್ ಮಾಡಿ
cap.release()
cv2.destroyAllWindows()
