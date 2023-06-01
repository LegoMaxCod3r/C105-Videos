import cv2

#usar "0" para la camara web

vid = cv2.VideoCapture(0)
if(vid.isOpened()==False):
    print("No es posible leer la entrada.")


height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(height)
print(width)

out = cv2.VideoWriter("fsag.mp4",cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))

while(True):
    #Captura el video
    ret, frame = vid.read()
    cv2.imshow("Camara Web", frame)
    out.write(frame)
    if cv2.waitKey(25)== 32:
        break

vid.release()
out.release()

cv2.destroyAllWindows()
