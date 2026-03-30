import cv2
import numpy as np

# Start camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to HSV (better for color detection)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define green color range
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    # Mask for green color
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Count green pixels
    green_pixels = np.sum(mask > 0)

    # Condition (adjust threshold if needed)
    if green_pixels > 5000:
        text = "ID CARD DETECTED"
        color = (0, 255, 0)  # Green
    else:
        text = "NO ID CARD"
        color = (0, 0, 255)  # Red

    # Show result on screen
    cv2.putText(frame, text, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Student ID Detection", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()