import cv2 #importing open cv

#Here we will discuus how to load an image in open cv

image=cv2.imread("Open-Cv\Phase 1 in Open cv\opencv-.jpg") #here imread is function which will load ur picture and chk it
if image is None: #condition statement
     print("Error image is not found :")
else:
    print("Image is found")
