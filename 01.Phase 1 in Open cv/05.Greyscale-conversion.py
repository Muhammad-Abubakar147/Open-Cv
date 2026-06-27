#Grayscle conversion method is a method in which we can change color type of image .
#Here we will use method for changing color of image which is => "cvtColor" it will convert color of image .


#Here we will discuss how grayscle method works 

import cv2 #importing of cv
image=cv2.imread("C:\Data\Open Cv\Open-Cv\Phase 1 in Open cv\opencv-.jpg") #opening of image 
if image is not None:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #Grayscale converter method 
    
    #Displaying of image 
    cv2.imshow("Image is showing",gray) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Could not load image")