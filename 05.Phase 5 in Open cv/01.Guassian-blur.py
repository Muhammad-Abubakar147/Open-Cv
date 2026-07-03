#It reduce sharpness of image in open cv => to remove noise =>image smooth 

#syntax for this method 
#blur image=cv2.GuassianBlur(image,(kernal_size_x,kernal_size_y),sigma)

import cv2
#Loading of image 
image =cv2.imread(r"photos\Nature.jpg") 
#syntax for guassian blur image 
blury =cv2.GaussianBlur(image,(7,7),6)
#image show orignal
cv2.imshow("Orignal image",image)
#image blur show 
cv2.imshow("Blury image",blury)
cv2.waitKey(0)
cv2.destroyAllWindows()