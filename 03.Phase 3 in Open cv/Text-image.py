#Here we will disscuss how we can text on a picture
#Syntax for texting on a image 

#cv.putText(image,"text",org,font,font scale,color,thickness)

import cv2 as cv
image=cv.imshow("photos\mother cat image.jpg")
cv.putText(image,"This is mother image",(50,200),cv.FONT_HERSHEY_PLAIN,1.2,(255,0,0),2)
