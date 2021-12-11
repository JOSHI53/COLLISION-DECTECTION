import cv2
cars_cascade = cv2.CascadeClassifier('cars.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect(frame):
    cars = cars_cascade.detectMultiScale(frame, 1.15, 4)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w,y+h), color=(0, 255, 0), thickness=2)
    
    return frame
def people(frame):
    faces=face_cascade.detectMultiScale(frame,1.15,4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w,y+h), color=(0, 0, 255), thickness=2) 
    return frame




def Simulator():
    Video = cv2.VideoCapture('videoplayback.mp4')
    # Video = cv2.VideoCapture(0)   
    while Video.isOpened():
        ret, frame = Video.read()
        controlkey = cv2.waitKey(1)
        if ret:        
            objects = detect(frame)
            bodies = people(frame)
           
            cv2.imshow('frame', objects)
            cv2.imshow('frame2',bodies)
            
        else:
            break
        if controlkey == ord('q'):
            break
    Video.release()
    cv2.destroyAllWindows()


Simulator()
