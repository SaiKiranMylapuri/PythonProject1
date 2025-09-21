
import cv2 as c

cap=c.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if not(ret):
        break
    c.imshow("webcam",frame)
    if c.waitKey(69) & 0xFF == ord('A'):
        print("QUITTING")
        print(ord("A"))
        break
cap.release()
c.destroyAllWindows()





