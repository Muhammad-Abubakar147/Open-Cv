#Imshow => it will show image on computer screen 
#waitkey => if we are not using it after imshow it will disappear from screen instantly 
#distroyallwindows => will close all open images on computer screen
#There are methods of dispalying methods

import cv2

#Here we will discuss how to display an image in open cv

image=cv2.imread("Open-Cv\Phase 1 in Open cv\opencv-.jpg") 
if image is not None:
     cv2.imshow("Image displaying",image) #open the window
     cv2.waitKey(0) #wait for a key (here 0 means whwnever any key is press close the image)
     cv2.destroyAllWindows()#close the window
else:
    print("Image not found")