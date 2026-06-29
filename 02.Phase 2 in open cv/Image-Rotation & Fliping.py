#Here we will discuss how to image rotate and flip .
#Syntax for rotation => "rotated = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)"
# Available Rotation Options :
# cv.ROTATE_90_CLOCKWISE => for rotating clockwise
#cv.ROTATE_90_COUNTERCLOCKWISE => for counter clockwis erotation of image 
#cv.ROTATE_180 =>for 180 degree 
#Syntax => rotation=cv.getRotationMatrix2D(center,angle,scale)

import cv2 as cv #importing image

image =cv.imread("photos\cat image 2.jpg") # Load image
(h,w)=image.shape[:2] # Get image dimensions
center=(w//2,h//2) # Find center
M=cv.getRotationMatrix2D(center,167,1.0)
rotated=cv.warpAffine(image, M, (w, h))
cv.imshow("Orignal Image",image)
cv.imshow("Rotated Image",rotated)
cv.waitKey(0)
cv.destroyAllWindows()