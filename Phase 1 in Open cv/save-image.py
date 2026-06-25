import cv2
image=cv2.imread("Phase 1 in Open cv\opencv-.jpg")
success=cv2.imwrite("Output.jpeg",image)
print(success)