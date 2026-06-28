#Here we will discuss how to crop and slice an image in open-cv
#Crope image method use for croping some area from the picture in open cv

import cv2 as cv  #importing cv 

image =cv.imread("photos\cat iamge.jpg") #image read

if image is not None:
    croped=image[100:500,100:500] #crope method syntax
    cv.imshow("ORignal",image) #will show orignal image 
    cv.imshow("Cropped",croped) #will show cropped image 
    cv.waitKey(0)
    cv.destroyAllWindows()



