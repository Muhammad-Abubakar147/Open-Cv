#Here we will discuss how to save video in ur camera which recorded .

#syntax for it : cv2.VideoWriter(filename,codec,fps,frame_size)


import cv2 

camera = cv2.VideoCapture(0)

frame_width =int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)) #It will find caputer width
frame_height =int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)) #it will find capture height
 
codec= cv2.VideoWriter_fourcc(*"XVID") 
recorder = cv2.VideoWriter("My_Video.avi",codec,20,(frame_width,frame_height)) #main syntax 

while True:
    success,image=camera.read()
    
    if not success:
        break
    recorder.write(image)
    cv2.imshow("Recording done",image)
    
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
    

camera.release()
recorder.release()
cv2.destroyAllWindows()