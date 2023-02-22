import cv2
import numpy as np

#if there is a camera/webcam
#cap = cv2.VideoCapture(0)

image_name = input("Enter the file path of your image: ")

img = cv2.imread(image_name)
image = cv2.resize(img, (700, 600))

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([(5, 50, 50)])
upper = np.array([15, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

cv2.imshow("Image", image)
cv2.imshow("Mask", mask)


cv2.waitKey(0)
