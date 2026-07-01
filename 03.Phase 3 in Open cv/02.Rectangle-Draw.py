# Syntax of Draw a Rectangle in open cv 
#cv.rectangle(image,pt,pt,color,thickness)

import cv2 

image =cv2.imread("photos\cat image 2.jpg")

pt1=(50,50)
pt2=(200,200)
color=(250,0,0)
thickness=(5)
cv2.rectangle(image,pt1,pt2,color,thickness)
cv2.imshow("Rectangle image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()