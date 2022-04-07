# import the opencv library
import cv2, pyautogui

# load eye tracker
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# load head tracker
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# get video camera
cam = cv2.VideoCapture(0)

def click():
    pyautogui.click()

while True:
    # Read the frame
    _, img = cam.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Loop through faces
    for (x, y, w, h) in faces:
        # draw faces
        cv2.rectangle(img, (x, y+int(round(h*.1))), (x+w, y+int(round(h*.6))), (255, 0, 0), 2)
        # display eye perspective
        cv2.imshow('gray', gray[y+int(round(h*.1)):y+int(round(h*.6)), x:x+w])
        # detect eyes
        eyes = eye_cascade.detectMultiScale(gray[y+int(round(h*.1)):y+int(round(h*.6)), x:x+w], 1.1, 4)
        # loop through each detected eye with diffrent x values
        count = 0
        for (_x, _y, _w, _h) in eyes:
            # draws rectangles around eyes
            cv2.rectangle(img, (_x+x, _y+y), (_x+x+_w, _y+y+_h), (0, 255, 0), 1)
            count += 1
        if count < 2:
            click()



    # displays main window
    cv2.imshow('img', img)

    # exit key
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

# release camera
cam.release()
