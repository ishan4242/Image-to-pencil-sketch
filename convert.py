

#LetsGrowMore:Data Science Internship
#Beginner Level Task 1: Image to Pencil Sketch with python
#Author: Ishan Jadhav



import cv2
from cv2 import blur
image = cv2.imread("Tree.jpg")
grey_filter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_filter)
blur = cv2.GaussianBlur(invert,(21,21),0)
invertedblur = cv2.bitwise_not(blur)

sketch_filter = cv2.divide(grey_filter, invertedblur,scale=245.0)
cv2.imwrite("out.png",sketch_filter)