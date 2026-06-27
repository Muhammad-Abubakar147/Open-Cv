#Grayscle conversion method is a method in which we can change color type of image .
#Here we will use method for changing color of image which is => "cvtColor" it will convert color of image .

import cv2
image=cv2.imread("C:\Data\Open Cv\Open-Cv\Phase 1 in Open cv\opencv-.jpg")
if image is not None:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image is showing",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Could not load image")