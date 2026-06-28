#Here we will discuss how to crop and slice an image in open-cv
#Crope image method use for croping some area from the picture in open cv

import cv2 as cv 

image =cv.imread("photos\mother cat image.jpg")
croped=image[100:200,150:50]
