#This method is about to know of image hieght,width,color channel etc
#Here method is used (image.shape)

import cv2
image =cv2.imread("Open-Cv\Phase 1 in Open cv\opencv-.jpg")
if image is not None:
    h,w,c=image.shape
    print(f"Image loaded:/nHieght: {h}/nWidth: {w}/nChannels: {c}")
else:
    print("Image not loaded successfully")