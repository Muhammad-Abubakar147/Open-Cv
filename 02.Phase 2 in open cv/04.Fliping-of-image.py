#Here we will disscuss about fliping of image in open cv 

#syntax for flip an image in open cv => cv.flip(image,1=horizontally)
                                    #=> cv.flip(image,0=vertcally)
                                    #=> cv.flip(image,-1=both)
                        
                        
import cv2 as cv  #importing cv

image =cv.imread("C:\Data\Open Cv\Open-Cv\photos\cat iamge.jpg") #loading image

if image is None:
    print("Could not load image")
    exit() #will exit if not opened
else:
    
    fliped_horizontal=cv.flip(image,1) #This syntax flip horizonatal
    fliped_vertically=cv.flip(image,0) #This syntax flip vertical
    fliped_both=cv.flip(image,-1) #this syntax flip both horizontal and vertical
    
    cv.imshow("Orignal",image)
    cv.imshow("Flipped Horizonatally",fliped_horizontal)
    cv.imshow("Fliped Vertically",fliped_vertically)
    cv.imshow("Flipped_both",fliped_both)
    
    cv.waitKey(0)
    cv.destroyAllWindows()