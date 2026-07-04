#Purpose of this method to detect edges (boundries of image ). => For separation of objects => Features extraction 

#Syntax for this method :  => edge = cv2.Canny(image,thrsehold 1,threshold 2)

import cv2
#for loading image and converting in greyscale 
image = cv2.imread(r"photos\flower image.jpg",cv2.IMREAD_GRAYSCALE)
#for canny image (syntax)
edges = cv2.Canny(image,50,150)
#for saving canny image 
cv2.imwrite("Canny image.jpeg",edges)
#for showing image 
cv2.imshow("Orginal image",image) #will show orignal image 
cv2.imshow("Edges image",edges) #will show canny edges image 
#close all windows on pressing any key
cv2.waitKey(0)
cv2.destroyAllWindows()
