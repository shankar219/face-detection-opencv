import cv2
import os
from datetime import datetime

# Create directory for saving faces
if not os.path.exists('detected_faces'):
    os.makedirs('detected_faces')

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print("Error: Couldn't load face cascade classifier")
    exit()

# Try different camera indices and backends
def try_open_camera(indices=[0, 1, 2, 3], backends=[cv2.CAP_ANY, cv2.CAP_V4L2, cv2.CAP_DSHOW]):
    for backend in backends:
        for index in indices:
            cap = cv2.VideoCapture(index, backend)
            if cap.isOpened():
                print(f"Success: Webcam opened with index {index} and backend {backend}")
                return cap
            cap.release()
    return None

# Initialize webcam
cap = try_open_camera()
if cap is None:
    print("Error: Couldn't open any webcam. Please check if a webcam is connected and drivers are installed.")
    exit()

face_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Couldn't read frame")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    face_count = len(faces)
    
    # Draw rectangles and save detected faces
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, f'Face {i+1}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        
        face_img = frame[y:y+h, x:x+w]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        cv2.imwrite(f'detected_faces/face_{timestamp}_{i}.jpg', face_img)
    
    cv2.putText(frame, f'Faces Detected: {face_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Face Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()