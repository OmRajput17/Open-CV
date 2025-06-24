import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # img = cv2.line(frame, (0,0), (width, height), (255, 0, 0), 10)
    # img = cv2.line(frame, (width,0), (0, height), (255, 0, 0), 10)

    img = cv2.rectangle(frame, (0,0), (width, height), (128, 128, 0), 5)
    cv2.circle(frame, (300, 300), 60, (0,0,255), 10)

    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img, 'Hello', (200, height-10), font, 5, (255, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()