#Bitwise method (operator) is use for combine 2 images =>cutout image => flip image

#There are three types of bitwise operation in open cv 
#cv2.bitwise_or(image1,image2)
#cv2.bitwise_and(image1,image2)
#cv2.bitwise_not(image1,)


import cv2
import numpy as np

img1=np.zeros((300,300),dtype="uint8")
img2=np.zeros((300,300),dtype="uint8")

cv2.circle(img1,(150,150),100,255,-1)
cv2.rectangle(img2,(100,100),(250,250),255,-1)

bitwise_and=cv2.bitwise_and(img1,img2)
bitwise_or=cv2.bitwise_or(img1,img2)
bitwise_not=cv2.bitwise_not(img1)

cv2.imshow("Circle image",img1)
cv2.imshow("rectangle image",img2)

cv2.imshow("Bitwise and Image ",bitwise_and)

cv2.imshow("Bitwise or Image",bitwise_or)

cv2.imshow("Bittwise not Image",bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows() 