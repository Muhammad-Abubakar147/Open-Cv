import cv2

image=cv2.imread("Open-Cv\Phase 1 in Open cv\opencv-.jpg")
if image is None:
     print("Error image is not found :")
else:
    print("Image is found")
