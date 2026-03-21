import cv2
import mediapipe as mp
import winsound  # Works on Windows. For Mac/Linux, use 'os.system' or 'pygame'

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Capture video from webcam
cap = cv2.VideoCapture(0)

print("System Started... Press 'q' to stop.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Flip and convert to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Points for Upper and Lower Eyelids
            upper_eye = face_landmarks.landmark[159] 
            lower_eye = face_landmarks.landmark[145]
            
            # Calculate the distance between upper and lower eyelids
            distance = lower_eye.y - upper_eye.y

            # If distance is very small, eyes are closed
            if distance < 0.012: 
                cv2.putText(frame, "WAKE UP! UTTO BETA UTTO!", (50, 100), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
                
                # Play a beep sound (Frequency 1000Hz, Duration 200ms)
                winsound.Beep(1000, 200) 
            else:
                cv2.putText(frame, "Status: Awake", (50, 100), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Drowsiness Alert System', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
