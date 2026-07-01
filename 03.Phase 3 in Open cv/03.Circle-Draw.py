#Syntax for draw cirle in open cv 
#cv.circle(image,center,radius,color,thickness)

import cv2 as cv

image=cv.imread("photos\cat image 2.jpg")

cv.circle(image,(210,150),50,(0,0,250),3)

cv.imshow("Circle image",image)
cv.waitKey(0)
cv.destroyAllWindows()