import cv2

cam = cv2.VideoCapture(0)

ret, img = cam.read()
vis = img.copy()
cv2.imshow('Camera', vis)
save_path = 'C:/Users/aux55555/PycharmProjects/yolo_v5/yolo_v5/data/images/output.jpg'

cv2.imwrite(save_path, vis)



cam.release()
cv2.destroyAllWindows()