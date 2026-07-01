# Syntax of Draw a Rectangle in open cv 
#cv.rectangle(image,pt,pt,color,thickness)

#Importing cv
import cv2 
#Loading image 
image =cv2.imread("photos\cat image 2.jpg")
#Defining part1 (Where xaxis & yaxis shows)
pt1=(50,50)
#Defining part2 (Where xaxis & y axis shows)
pt2=(200,200)
#Define color 
color=(250,0,0)
#How much thickness
thickness=(5)
cv2.rectangle(image,pt1,pt2,color,thickness)
cv2.imshow("Rectangle image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()