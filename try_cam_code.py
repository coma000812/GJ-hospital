# GJ-hospital
#--pynput을 이용해서 비행하는 동안에 카메라로 영상을 수신하는 코드


import cv2
import os
import time
import numpy as np
from cv2 import aruco
from pynput.keyboard import Key, Controller
import time


class Aruco(object):

    # Initialize ArUco
    def __init__(self):
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
        self.parameters =  aruco.DetectorParameters_create()

    # Do ArUco marker detection
    def detect_markers(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, _ = aruco.detectMarkers(gray, self.aruco_dict, parameters=self.parameters)
        markers = aruco.drawDetectedMarkers(frame, corners, ids)
        return markers

class Camera(object):

    def __init__(self, drone):
        self.cap = None
        self.drone = drone
        self.frame_size = (480, 360)
        self.vudeo_size = (960, 720)
        
        # For recording video
        self.vout = cv2.VideoWriter()

        if self.drone.is_aruco_tracking_enabled is True:
           self.aruco = Aruco()

    def get_video(self):
        self.drone.is_streaming = True
        self.cap = cv2.VideoCapture('udp://127.0.0.1:14501')
        _, self.frame = self.cap.read()

    # Get the image frame
    def get_frame(self):
        _, self.frame = self.cap.read()

        # Write the video frame before we size it down
        if self.drone.is_recording_video is True:
            self.vout.write(self.frame)

        # Resize the frame for display in the web app
        frame = cv2.resize(self.frame, self.frame_size)

        if self.drone.is_aruco_tracking_enabled is True:
            frame = self.aruco.detect_markers(frame)

        _, jpeg = cv2.imencode('image.jpg', frame)

        return jpeg.tostring()

    def take_photo(self):
        
        try:
            filename = time.strftime("%Y%m%d-%H%M%S")
            cv2.imwrite(self.file_path + "/photos/" + filename + ".jpg", self.frame)
        except Exception as e:
            print("Error taking photo: ", e)
            
        return "success"

    def start_recording(self):
        filename = time.strftime("%Y%m%d-%H%M%S")
        self.vout = cv2.VideoWriter(self.file_path + "/videos/" + filename + ".avi", cv2.VideoWriter_fourcc('M','J','P','G'), 30, self.video_size)
        self.drone.is_recording_video = True

    def stop_recording(self):
        self.vout.release()
        self.drone.is_recording_video = False

    def __del__(self):
        if self.vout:
            self.vout.release()
        if self.cap:
            self.cap.release()

def take_photo (Key.backspace):
    if press_backspace:
        print("land")
        arm_and_land(10)
        print("land success")

if keyboard = Controller()

   time.sleep(2)
   for char in "takeoff":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.12)
