import cv2 
face_cascade=cv2.CascadeClassifier(r"XML files folder\haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray,1.1,5)
    
    """
    detectMultiScale is function which detect face and scan it  
    
    1.1 is balance which is for zooming at face  
    minNeighbours=5 =>5 test 
    """
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Webcam face detection",frame )
        
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
        
cap.release()
cv2.destroyAllWindows()