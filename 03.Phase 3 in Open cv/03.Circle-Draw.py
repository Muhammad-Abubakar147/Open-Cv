#Syntax for draw cirle in open cv 
#cv.circle(image,center,radius,color,thickness)
#importing of cv 
import cv2 as cv
#Loading an image 
image=cv.imread("photos\cat image 2.jpg")
#draw circle function
cv.circle(image,(210,150),50,(0,0,250),3)
#image show syntax
cv.imshow("Circle image",image)
cv.waitKey(0)
cv.destroyAllWindows()