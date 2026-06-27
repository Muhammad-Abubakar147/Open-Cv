#This method is about to know of image hieght,width,color channel etc
#Here method is used (image.shape)

import cv2
image =cv2.imread("Phase 1 in Open cv\opencv-.jpg") #oading of image in open cv 
if image is not None:
    h,w,c=image.shape #Image dimension method
    print(f"Image loaded:\nHieght: {h}\nWidth: {w}\nChannels: {c}")
else:
    print("Image not loaded successfully")
    
#output will be :
# Image loaded:
# Hieght: 405
# Width: 720
# Channels: 3