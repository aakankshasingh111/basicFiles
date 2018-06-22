import cv2
from time import sleep as s
while True:
        cam = cv2.VideoCapture(0)
        img = cam.read()[1]
        cv2.imshow("namw of window",img)
	if cv2.waitKey(10) == ord('q'):
		break
        cam.release()
        s(0.0003)

