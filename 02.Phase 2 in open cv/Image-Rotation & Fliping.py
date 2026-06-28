#Here we will discuss how to image rotate and flip .
#Syntax for rotation => "rotated = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)"
# Available Rotation Options :
# cv.ROTATE_90_CLOCKWISE => for rotating clockwise
#cv.ROTATE_90_COUNTERCLOCKWISE => for counter clockwis erotation of image 
#cv.ROTATE_180 =>for 180 degree 

import cv2 as cv #importing image

image =cv.imread("photos\cat image 2.jpg")
