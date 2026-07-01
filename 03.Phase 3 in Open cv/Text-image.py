#Here we will disscuss how we can text on a picture
#Syntax for texting on a image 

#cv.putText(image,"text",org,font,font scale,color,thickness)
#importing cv 
import cv2 as cv
#Loading image 
image=cv.imread("photos\mother cat image.jpg")
#checking image shape
print(image.shape)
cv.putText(image,"This is mother image",(10,150),
           cv.FONT_HERSHEY_PLAIN,1.2,(255,0,0),1)
cv.imshow("texting image show",image)
cv.waitKey(0)
cv.destroyAllWindows()