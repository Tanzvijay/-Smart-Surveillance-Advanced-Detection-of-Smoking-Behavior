# -Smart-Surveillance-Advanced-Detection-of-Smoking-Behavior
Smart Surveillance: Monitoring Public Spaces for Smoking Activity Detection

introduction:
This repository contains code for a smoking detection system built using the YOLO (You Only Look Once) object detection algorithm. The system is capable of detecting instances of smoking behavior in real time using a webcam or recorded video.

Features:

Real-time Smoking Detection: The system employs the YOLO object detection algorithm to detect instances of smoking behavior in real-time.
Email Notification: When smoking behavior is detected, the system sends an email notification to a specified recipient with a snapshot of the detected event.
Customizable: The system is highly customizable, allowing users to adjust parameters such as the model filename, email credentials, and notification thresholds.
Video Recording: The system can also record the video stream along with the detected smoking instances for further analysis or review.
Requirements:

Python 3. x
OpenCV
PyAutoGUI
smtplib
EmailMessage
Ultralytics YOLO

Title: Smoking Detection System using YOLO

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
Installation:

Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/your_username/smoking-detection.git
Install the required dependencies using pip:
Copy code
pip install -r requirements.txt
Download the YOLO model weights and place them in the specified directory.
Usage:


Ensure that your webcam is connected and positioned correctly to capture the desired area.
The system will start detecting smoking instances in the video stream. When smoking is detected, a bounding box will be drawn around the smoker, and the class label will be displayed.
If the specified threshold for smoking instances is reached (e.g., 30 instances), an email notification will be sent with a snapshot of the detected event.
Configuration:

Model Filename: Specify the filename of the pre-trained YOLO model weights in the modelFilename variable.
Email Credentials: Update the sender and receiver email addresses, along with the sender's password, in the send_email() function.
Thresholds: Adjust the threshold for sending email notifications by modifying the count variable in the CaptureVideo() function.
Video Recording: Customize the video recording settings, such as frame rate and resolution, in the file = cv.VideoWriter(...) line.
