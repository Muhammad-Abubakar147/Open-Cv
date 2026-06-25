#Imshow
#waitkey
#distroyallwindows
#There are methods of dispalying methods

import cv2

image=cv2.imread("Open-Cv\Phase 1 in Open cv\opencv-.jpg") 
if image is not None:
     cv2.imshow("Image displaying",image) #open the window
     cv2.waitKey(0) #wait for a key
     cv2.destroyAllWindows()#close the window
else:
    print("Image is found")