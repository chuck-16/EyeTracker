# import the opencv library
import cv2, time

# load eye tracker
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

cam = cv2.VideoCapture(0)
print("loading camera 3 seconds...")
time.sleep(3)
print("loading camera 2 seconds...")
time.sleep(2)
print("loading camera 1 second...")
time.sleep(1)
while True:
    # Read the frame
    _, img = cam.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        eyes = eye_cascade.detectMultiScale(gray[x:x+w, y:y+h], 1.1, 4)
        for (_x, _y, _w, _h) in eyes:
            cv2.rectangle(img, (_x+x, _y+y), (_x+x+_w, _y+y+_h), (0, 255, 0), 1)


    # Display
    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cam.release()
