import time

import cv2
from djitellopy import Tello

cam = cv2.VideoCapture(0)
tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()

img = frame_read.frame
#cv2.imshow("drone", img)

save_path = 'C:/Users/aux55555/PycharmProjects/yolo_v5/tello_get_img/img_chair/chair48.jpg'
cv2.imwrite(save_path, img)
time.sleep(3)

img = frame_read.frame
save_path = 'C:/Users/aux55555/PycharmProjects/yolo_v5/tello_get_img/img_chair/chair49.jpg'
cv2.imwrite(save_path, img)
time.sleep(3)

img = frame_read.frame
save_path = 'C:/Users/aux55555/PycharmProjects/yolo_v5/tello_get_img/img_chair/chair42.jpg'
cv2.imwrite(save_path, img)
time.sleep(3)

img = frame_read.frame
save_path = 'C:/Users/aux55555/PycharmProjects/yolo_v5/tello_get_img/img_chair/chair43.jpg'
cv2.imwrite(save_path, img)
time.sleep(3)

tello.land()