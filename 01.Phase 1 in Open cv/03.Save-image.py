#Here we will discuss how to save an image in open cv
import cv2 #importing open cv

image=cv2.imread("Phase 1 in Open cv\opencv-.jpg") #reading image 
success=cv2.imwrite("Output.jpeg",image) #saving image 
print(success)