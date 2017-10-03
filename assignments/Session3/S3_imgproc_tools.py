import cv2
import numpy as np 

img_gray = cv2.imread("cat.jpg",0)
img_bgr = cv2.imread("cat.jpg",1)

#display the matrix shapes
print("Gray levels image shape = "+ str(img_gray.shape))
print("BGR image shape = "+ str(img_bgr.shape))

#display the loaded images
cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)

cv2.waitKey(0)
