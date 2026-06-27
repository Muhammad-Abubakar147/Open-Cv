#Here we will disscus how to resize and reshape an image in open cv .

#syntax for this method => resize=cv2.resize(sorce,width,hieght,)

import cv2
image= cv2.imread("photos\cat image 2.jpg") #Loading an image

if image is None: #if statement
    print("Image not loaded")
    
else:
    print("Image loaded")
    resized=cv2.resize(image,(360,350)) #Syntax of resizing and reshaping an image in open cv
    cv2.imshow(" Orignal Image is showing",image) #for showing  orignal image 
    cv2.imshow("Resized image is showing",resized) #for showing new image 
    cv2.waitKey(0) 
    cv2.destroyAllWindows()