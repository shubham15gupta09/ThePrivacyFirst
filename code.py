# the program uses the internal camera of the laptop or you can also use an external webcame for this 
# tha program will minimize the screen on the time when it setect the other face appering in . i.e. no. of face is graeter than 2 
import cv2
from threading import Thread
import pynput
from pynput.keyboard import Key, Controller,Listener
keyboard = Controller()
f_c = cv2.CascadeClassifier('face_cascade.xml')
cap = cv2.VideoCapture(0)
count=0
def on_press(key):
    print("")

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        cap.release()
        cv2.destroyAllWindows()
        # Stop listener
        return False

# Collect events until released
def startListener():
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def detect(img):
    faces = f_c.detectMultiScale(img, 1.3, 5)
    count = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 5)
        count = count + 1
    if count > 1:

        #Steps for minimizing the windows...
        keyboard.press(Key.cmd)
        keyboard.press('m')
        keyboard.release('m')
        keyboard.release(Key.cmd)
    cv2.imshow('frame', img)

def CaptureVideo():
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detect(frame)
        #Stop if the escape key is pressed.
        k = cv2.waitKey(30) & 0xff
        if k==27:
            keyboard.press(Key.alt_l)
            keyboard.press(Key.tab)
            keyboard.release(Key.alt_l)
            break
    cap.release()
    cv2.destroyAllWindows()

Thread(target=startListener).start()
Thread(target=CaptureVideo).start()




