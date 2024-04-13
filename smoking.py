from ultralytics import YOLO
import glob
import os
import cv2
from ultralytics import YOLO
import cvzone
import numpy as np
import math
import time
import sys
import pyautogui
import smtplib
from email.message import EmailMessage
import cv2 as cv

modelFilename= "D:/Object detection/finalsmoking/runs/detect/train/weights/best.pt"
PPEmodel = YOLO(modelFilename)

classes = ['smoking']
count=0
cam = cv.VideoCapture(0)
cc = cv.VideoWriter_fourcc(*'XVID')
file = cv.VideoWriter('C:/Users/vijay/OneDrive/Desktop/screen_photos/output.avi', cc, 15.0, (640, 480))


with open("C:/Users/vijay/OneDrive/Desktop/names.txt", "r") as f:
    classes = [line.strip() for line in f.readlines()]
def RunYoloModel():

    PPEmodel = YOLO(modelFilename)
    return PPEmodel

def draw_square(img, x1, y1, side_length, mycolor):

    pts = [(x1, y1), (x1 + side_length, y1), (x1 + side_length, y1 + side_length), (x1, y1 + side_length)]
    cv2.polylines(img, [np.array(pts)], isClosed=True, color=mycolor, thickness=3)


def send_email():

    sender_email = "viknsh3@gmail.com"
    receiver_email = "vijaytanz12@gmail.com"
    password = "xibc hwek pcch jvsg"



    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Subject of the email"
    msg.set_content("This is the body of the email.")

    # Attach file - provide the correct file path
    folder_path = "C:/Users/vijay/OneDrive/Desktop/screen_photos"



    for file_name in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'rb') as file:
            file_data = file.read()
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

    print("Email sent successfully.")




def CaptureVideo():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    return cap

cap = CaptureVideo()
mycolor = (255,255,255)
while True:
    success,img = cap.read()
    results = PPEmodel(img, stream=True)
    for r in results:
         boxes = r.boxes




    # Assuming 'classes' is a list of class names
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        w, h = x2 - x1, y2 - y1
        side_length = max(w, h)  # Choose the maximum of width and height as the side length

        # Generate a unique color for each box
        mycolor = (int(x1) % 255, int(y1) % 255, int(x2) % 255)  # Change this line to define your own color logic

        draw_square(img, x1, y1, side_length, mycolor)

        conf = math.ceil((box.conf[0] * 100)) / 100
        print(box)
        cls = int(box.cls[0])

        if classes[cls]=='smoking':
            print("hello")
            count=count+1

        if count==30:

            send_email()
            sys.exit()

        cvzone.putTextRect(img, f'{classes[cls]}',
                           (max(0, x1), max(35, y1)), scale=1, thickness=1, colorB=mycolor,
                           colorT=(0, 0, 0), colorR=mycolor)



    cv2.imshow("using_phone_detection",img)
    file.write(img)
    cv2.waitKey(10)
