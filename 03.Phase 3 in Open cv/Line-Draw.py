#Here we will discus about how to draw a line on image 

import cv2 #Importing cv 

image =cv2.imread("photos\Cat image 3.jpg") #Loading image 

pt1=(20,20)
pt2=(200,200)
color=(250,0,0)
thicknes=(4)

cv2.line(image,pt1,pt2,color,thicknes)

cv2.imshow("Image Showing",image)
cv2.waitKey(0)
cv2.destroyAllWindows()