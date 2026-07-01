#Here we will discus about how to draw a line on image 

import cv2 #Importing cv 

image =cv2.imread("photos\Cat image 3.jpg") #Loading image 
#defining where line start and where line end 
pt1=(100,50)
pt2=(200,50)
#define color of line 
color=(250,0,0)
#How much thickness of line 
thicknes=(4)
#Line draw syntax 
cv2.line(image,pt1,pt2,color,thicknes)
#image show 
cv2.imshow("Image Showing",image)

cv2.waitKey(0)
#destroy all windows
cv2.destroyAllWindows()