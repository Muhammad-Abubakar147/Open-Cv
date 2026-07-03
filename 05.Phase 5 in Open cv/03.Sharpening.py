#Here we will disscuss about sharpening of image in open cv . It will make sharper ur image .It highlight ur image edges .
#syntax for this method : cv2.filter2D(src,ddept,kernal)

import cv2
import numpy as np

image = cv2.imread(r"photos\Low resolution.jpg")

sharpen_kernal =np.array([[0,-1,0],
                         [0,5,0],
                         [0,-1,0]])

sharped=cv2.filter2D(image,-1,sharpen_kernal)
cv2.imshow("origanl image",image)
cv2.imshow("sharp image",sharped)
cv2.waitKey(0)
cv2.destroyAllWindows()