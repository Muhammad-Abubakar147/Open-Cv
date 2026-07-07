#syntax of threshlod image : threshold_image=cv2.threshold(image,thresh-value,max_value,method)
#importing cv
import cv2 
#loading image 
image =cv2.imread(r"photos\camerman.jpg",cv2.IMREAD_GRAYSCALE)
#synta for tresherhold image
ret,thershold_img =cv2.threshold(image,120,255,cv2.THRESH_BINARY)
#show orignal image 
cv2.imshow("orignal image",image)
#show thresherhold image
cv2.imshow("treshhold image",thershold_img)
#close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()