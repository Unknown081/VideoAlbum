from tkinter import Frame
import cv2
 
vid = cv2.VideoCapture(1) 
if(vid.isOpened()== False):
    print("unabletoreadthefeed") 
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width = int(vid.get(cv2.CAP_PROP_WIDTH))
print(width)


frame = int(vid.get(cv2.CAP_PROP_FPS))
print(frame)

out = cv2.VideoWriter('Boxing.mp4'cv2.VideoWriter_fourcc(*'DIVX'),30, (width,height))

while(True):

    ret, fram = vid.read()

    cv2.imshow("web cam", frame)
    out.write(frame)

    if cv2.waitKey(1) == 32:
         break

vid.release()
out.release()

cv2.destroyallwindows

