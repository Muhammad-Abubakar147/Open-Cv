#Here we will disscus how to resize and reshape an image in open cv .

#syntax for this method => resize=cv2.resize(sorce,width,hieght,)

import cv2
image= cv2.imread("photos\cat image 2.jpg")

if image is None:
    print("Image not loaded")
    
