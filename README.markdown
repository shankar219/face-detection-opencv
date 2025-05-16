# Face Detection System with OpenCV

This is a real-time face detection project I built using Python and OpenCV to learn computer vision for my internship application. It uses a Haar Cascade classifier to detect faces in a webcam feed, counts the number of faces, and saves detected faces as images.

## How It Works

The script captures video from a webcam, converts frames to grayscale, and uses OpenCV's Haar Cascade to detect faces. It draws blue rectangles around faces, labels them, and shows the total face count on the screen. Detected faces are saved with timestamps in a `detected_faces` folder.

## Setup Instructions

1. Install Python 3.6 or higher.
2. Install OpenCV: `pip install opencv-python`
3. Connect a webcam to your computer.
4. Download or clone this repository.
5. Run the script: `python face_detection.py`
6. Press `q` to quit.

## Features

- Detects faces in real-time using a webcam.
- Displays the number of faces detected on the screen.
- Saves cropped face images with timestamps.
- Supports multiple webcam indices to handle connection issues.

## Challenges

I ran into webcam access errors on my system, so I added a function to try different camera indices and backends (like CAP_V4L2 and CAP_DSHOW). This made the script more robust across different setups.

## What I Learned

- How Haar Cascade classifiers work for object detection.
- Processing video frames with OpenCV.
- Handling webcam compatibility issues programmatically.

## Future Improvements

- Add eye or smile detection using other Haar Cascade files.
- Create a simple GUI to control the detection.
- Integrate with a web app to stream the video feed.

## Why I Built This

I wanted to explore computer vision and build something practical to showcase my Python skills for internship applications. This project helped me understand image processing and real-time applications.

Feel free to try it out or suggest improvements!