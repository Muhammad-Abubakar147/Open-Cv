#Purpose of this method to detect edges (boundries of image ). => For separation of objects => Features extraction 

#Syntax for this method :  => edge = cv2.Canny(image,thrsehold 1,threshold 2)

import cv2
image = cv2.imread(r"photos\flower image.jpg",cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(image,50,150)
cv2.imwrite("Canny image.jpeg",edges)
cv2.imshow("Orginal image",image)
cv2.imshow("Edges image",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
