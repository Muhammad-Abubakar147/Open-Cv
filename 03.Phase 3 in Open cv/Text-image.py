#Here we will disscuss how we can text on a picture
#Syntax for texting on a image 

#cv.putText(image,"text",org,font,font scale,color,thickness)
#importing cv 
import cv2 as cv
#Loading image 
image=cv.imread("photos\mother cat image.jpg")
#checking image shape
print(image.shape)
#syntax of image texting
cv.putText(image,"This is mother image",(10,150),
           cv.FONT_HERSHEY_PLAIN,1.2,(255,0,0),1)
#image show
cv.imshow("texting image show",image)
#waitkey
cv.waitKey(0)
#close all windows
cv.destroyAllWindows()