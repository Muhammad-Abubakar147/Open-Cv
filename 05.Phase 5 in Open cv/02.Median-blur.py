#We can clean a image by this method .
#syntax for this method is : cv2.medianBlur(image,kernal size)

import cv2

image =cv2.imread(r"photos\Noisy-image.jpg")

Noisy =cv2.medianBlur(image,9) #here kernal size always " odd "

cv2.imshow("Orignal image",image) #syntax for cleaning and image in open cv 
cv2.imshow("clean image",Noisy)
#close all windows 
cv2.waitKey(0)
cv2.destroyAllWindows()