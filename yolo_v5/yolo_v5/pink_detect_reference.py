# simple example demonstrating how to control a Tello using your keyboard.
# For a more fully featured example see manual-control-pygame.py
#
# Use W, A, S, D for moving, E, Q for rotating and R, F for going up and down.
# When starting the script the Tello will takeoff, pressing ESC makes it land
#  and the script exit.

from djitellopy import Tello
import cv2, math, time
import numpy as np

# 定義紅色物體的HSV色域範圍
red_lower = (145, 11, 188)
red_upper = (179, 63, 255)
#red_lower = (151, 17, 154)
#red_upper = (179, 82, 255)

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()

while True:
    # In reality you want to display frames in a seperate thread. Otherwise
    #  they will freeze while the drone moves.
    img = frame_read.frame
    cv2.imshow("drone", img)

    #裁減圖片
    cropped_img1 = img[0:240, 0:320]#上左
    cropped_img2 = img[0:240, 320:640]#上中
    cropped_img3 = img[0:240, 640:960]#上右
    cropped_img4 = img[240:480, 0:320]#中左
    cropped_img5 = img[240:480, 320:640]#中中
    cropped_img6 = img[240:480, 640:960]#中右
    cropped_img7 = img[480:720, 0:320]#下左
    cropped_img8 = img[480:720, 320:640]#下中
    cropped_img9 = img[480:720, 640:960]#下右

    # 將影像從BGR色彩空間轉換為HSV色彩空間
    # 使用cv2.inRange()函數生成一個掩模，其中的值為在HSV範圍內的像素值
    # 計算紅色像素的數量
    #cv2.imshow("img1", cropped_img1)
    hsv_img1 = cv2.cvtColor(cropped_img1, cv2.COLOR_BGR2HSV)
    red_mask1 = cv2.inRange(hsv_img1, red_lower, red_upper)
    red_pixels1 = cv2.countNonZero(red_mask1)

    #cv2.imshow("img2", cropped_img2)
    hsv_img2 = cv2.cvtColor(cropped_img2, cv2.COLOR_BGR2HSV)
    red_mask2 = cv2.inRange(hsv_img2, red_lower, red_upper)
    red_pixels2 = cv2.countNonZero(red_mask2)

    #cv2.imshow("img3", cropped_img3)
    hsv_img3 = cv2.cvtColor(cropped_img3, cv2.COLOR_BGR2HSV)
    red_mask3 = cv2.inRange(hsv_img3, red_lower, red_upper)
    red_pixels3 = cv2.countNonZero(red_mask3)

    #cv2.imshow("img4", cropped_img4)
    hsv_img4 = cv2.cvtColor(cropped_img4, cv2.COLOR_BGR2HSV)
    red_mask4 = cv2.inRange(hsv_img4, red_lower, red_upper)
    red_pixels4 = cv2.countNonZero(red_mask4)

    #cv2.imshow("img5", cropped_img5)
    hsv_img5 = cv2.cvtColor(cropped_img5, cv2.COLOR_BGR2HSV)
    red_mask5 = cv2.inRange(hsv_img5, red_lower, red_upper)
    red_pixels5 = cv2.countNonZero(red_mask5)

    #cv2.imshow("img6", cropped_img6)
    hsv_img6 = cv2.cvtColor(cropped_img6, cv2.COLOR_BGR2HSV)
    red_mask6 = cv2.inRange(hsv_img6, red_lower, red_upper)
    red_pixels6 = cv2.countNonZero(red_mask6)

    #cv2.imshow("img7", cropped_img7)
    hsv_img7 = cv2.cvtColor(cropped_img7, cv2.COLOR_BGR2HSV)
    red_mask7 = cv2.inRange(hsv_img7, red_lower, red_upper)
    red_pixels7 = cv2.countNonZero(red_mask7)

    #cv2.imshow("img8", cropped_img8)
    hsv_img8 = cv2.cvtColor(cropped_img8, cv2.COLOR_BGR2HSV)
    red_mask8 = cv2.inRange(hsv_img8, red_lower, red_upper)
    red_pixels8 = cv2.countNonZero(red_mask8)

    #cv2.imshow("img9", cropped_img9)
    hsv_img9 = cv2.cvtColor(cropped_img9, cv2.COLOR_BGR2HSV)
    red_mask9 = cv2.inRange(hsv_img9, red_lower, red_upper)
    red_pixels9 = cv2.countNonZero(red_mask9)
    print(red_pixels1 ,red_pixels2 ,red_pixels3 ,red_pixels4 ,red_pixels5 ,red_pixels6 ,red_pixels7 ,red_pixels8 ,red_pixels9 )
    # 如果紅色像素的數量大於閾值（此處為1000），則降落
    red_pixels10 = red_pixels1 + red_pixels2 + red_pixels3 + red_pixels4 + red_pixels5 + red_pixels6 + red_pixels7 + red_pixels8 + red_pixels9

    key = cv2.waitKey(1) & 0xff
    if 80000 >= red_pixels10 >= 1000:
        if red_pixels1 > red_pixels2 and red_pixels1 > red_pixels3 and red_pixels1 > red_pixels4 and red_pixels1 > red_pixels5 and red_pixels1 > red_pixels6 and red_pixels1 > red_pixels7 and red_pixels1 > red_pixels8 and red_pixels1 > red_pixels9:
            tello.move_left(20)
            # time.sleep(0.2)
            tello.move_up(20)
            # time.sleep(0.2)
        elif red_pixels2 > red_pixels1 and red_pixels2 > red_pixels3 and red_pixels2 > red_pixels4 and red_pixels2 > red_pixels5 and red_pixels2 > red_pixels6 and red_pixels2 > red_pixels7 and red_pixels2 > red_pixels8 and red_pixels2 > red_pixels9:
            tello.move_up(20)
            # time.sleep(1)
        elif red_pixels3 > red_pixels1 and red_pixels3 > red_pixels2 and red_pixels3 > red_pixels4 and red_pixels3 > red_pixels5 and red_pixels3 > red_pixels6 and red_pixels3 > red_pixels7 and red_pixels3 > red_pixels8 and red_pixels3 > red_pixels9:
            tello.move_right(20)
            # time.sleep(1)
            tello.move_up(20)
            # time.sleep(1)
        elif red_pixels4 > red_pixels1 and red_pixels4 > red_pixels2 and red_pixels4 > red_pixels3 and red_pixels4 > red_pixels5 and red_pixels4 > red_pixels6 and red_pixels4 > red_pixels7 and red_pixels4 > red_pixels8 and red_pixels4 > red_pixels9:
            tello.move_left(20)
            # time.sleep(1)
        elif red_pixels5 > red_pixels1 and red_pixels5 > red_pixels2 and red_pixels5 > red_pixels3 and red_pixels5 > red_pixels4 and red_pixels5 > red_pixels6 and red_pixels5 > red_pixels7 and red_pixels5 > red_pixels8 and red_pixels5 > red_pixels9:
            if red_pixels5 > 50000 :
                break
            else:
                #tello.move_back(20)
                tello.move_forward(30)
                continue
        elif red_pixels6 > red_pixels1 and red_pixels6 > red_pixels2 and red_pixels6 > red_pixels3 and red_pixels6 > red_pixels4 and red_pixels6 > red_pixels5 and red_pixels6 > red_pixels7 and red_pixels6 > red_pixels8 and red_pixels6 > red_pixels9:
            tello.move_right(20)
            # time.sleep(1)
        elif red_pixels7 > red_pixels1 and red_pixels7 > red_pixels2 and red_pixels7 > red_pixels3 and red_pixels7 > red_pixels4 and red_pixels7 > red_pixels5 and red_pixels7 > red_pixels6 and red_pixels7 > red_pixels8 and red_pixels7 > red_pixels9:
            tello.move_left(20)
            # time.sleep(1)
            tello.move_down(20)
            # time.sleep(1)
        elif red_pixels8 > red_pixels1 and red_pixels8 > red_pixels2 and red_pixels8 > red_pixels3 and red_pixels8 > red_pixels4 and red_pixels8 > red_pixels5 and red_pixels8 > red_pixels6 and red_pixels8 > red_pixels7 and red_pixels8 > red_pixels9:
            tello.move_down(20)
            # time.sleep(1)
        elif red_pixels9 > red_pixels1 and red_pixels9 > red_pixels2 and red_pixels9 > red_pixels3 and red_pixels9 > red_pixels4 and red_pixels9 > red_pixels5 and red_pixels9 > red_pixels6 and red_pixels9 > red_pixels7 and red_pixels9 > red_pixels8:
            tello.move_right(20)
            # time.sleep(1)
            tello.move_down(20)
            # time.sleep(1)
        else:
            continue
    elif red_pixels10 >= 80000:
        break
    elif key == 27:  # ESC
        break
    else:
        #tello.move_up(25)
        tello.rotate_counter_clockwise(90)
        #tello.move_down(25)
    '''         
    key = cv2.waitKey(1) & 0xff
    if key == 27:  # ESC
        break
    elif key == ord('w'):
        tello.move_forward(30)
    elif key == ord('s'):
        tello.move_down(30)
    elif key == ord('a'):
        tello.move_left(30)
    elif key == ord('d'):
        tello.move_right(30)
    elif key == ord('e'):
        tello.rotate_clockwise(30)
    elif key == ord('q'):
        tello.rotate_counter_clockwise(30)
    elif key == ord('r'):
        tello.move_up(30)
    elif key == ord('f'):
        tello.move_down(30)
    #elif red_pixels > 50000:
     #   break
    '''



#cv2.imwrite("picture.png", frame_read.frame)
tello.land()
# LOAD AN IMAGE USING 'IMREAD'
#img = cv2.imread("picture.png")
# DISPLAY
cv2.imshow("picture", img)
cv2.waitKey(0)