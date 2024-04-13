Smart Surveillance: Advanced Detection of Smoking Behavior
Introduction:
This repository contains code for a smoking detection system built using the YOLO (You Only Look Once) object detection algorithm. The system is capable of detecting instances of smoking behavior in real-time using a webcam or recorded video.

Features:
Real-time Smoking Detection: The system employs the YOLO object detection algorithm to detect instances of smoking behavior in real-time.
Email Notification: When smoking behavior is detected, the system sends an email notification to a specified recipient with a snapshot of the detected event.
Customizable: The system is highly customizable, allowing users to adjust parameters such as the model filename, email credentials, and notification thresholds.
Video Recording: The system can also record the video stream along with the detected smoking instances for further analysis or review.
Requirements:
Python 3.x
OpenCV
PyAutoGUI
smtplib
EmailMessage
Ultralytics YOLO
