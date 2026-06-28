#Here we will discuss how to crop and slice an image in open-cv
#Crope image method use for croping some area from the picture in open cv

import cv2 as cv 

image =cv.imread("photos\cat iamge.jpg")
if image is not None:
    croped=image[100:500,100:500]
    cv.imshow("ORignal",image)
    cv.imshow("Cropped",croped)
    cv.waitKey(0)
    cv.destroyAllWindows()



