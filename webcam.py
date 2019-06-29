import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    frame = frame[0:350, 15:540]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)

    dilation = cv2.erode(threshold, kernel, iterations = 1)

    contours,_ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for (i, c) in enumerate(contours): # contorno
        (x, y, w, h) = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cmY = (h*15)/120
        cmX = (h*10)/130
        cv2.putText(frame, str("%.2f" % cmY) + 'cm', (x, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,255, 255), 1)
        cv2.putText(frame, str("%.2f" % cmX) + 'cm', (x+w+15, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,255, 255), 1)



    cv2.imshow("Frame", frame)
    # cv2.imshow("gray", gray)
    # cv2.imshow("threshold", threshold)
    # cv2.imshow("dilation", dilation)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.realease()
cv2.destroyAllWindows()