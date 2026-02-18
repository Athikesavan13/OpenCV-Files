import cv2
import numpy
import matplotlib.pyplot as plt



img =cv2.imread("D:\\Python files\\Computer-Vision-with-Python\\DATA\\00-puppy.jpg")
cv2.namedWindow("My Window")
while True:
    key = cv2.waitKey(1) & (0xFF)
    if key == ord("q"):
        break
    if cv2.getWindowProperty("My Sketch", cv2.WND_PROP_VISIBLE) < 1:
        break
    cv2.imshow("My Window",img)
plt.imshow(img)