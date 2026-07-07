#syntax of threshlod image : threshold_image=cv2.threshold(image,thresh-value,max_value,method)

import cv2 

image =cv2.imread(r"photos\camerman.jpg",cv2.IMREAD_GRAYSCALE)

ret,thershold_img =cv2.threshold(image,120,255,cv2.THRESH_BINARY)

cv2.imshow("orignal image",image)
cv2.imshow("treshhold image",thershold_img)
cv2.waitKey(0)
cv2.destroyAllWindows()