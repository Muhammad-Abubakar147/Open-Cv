import cv2 

cap=cv2.VideoCapture(0) #here 0 will open ur laptop or computer camera

while True :
    ret,frame = cap.read() #ret=True/false or frame image 
    
    if not ret :
        print("Camera not working")
        break
    
    cv2.imshow("webcam feed",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Quiting....")
        break
        
    

cap.release()
cv2.destroyAllWindows()
