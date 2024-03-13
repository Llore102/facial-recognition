import cv2 as cv
import os
import imutils

model = "Luis"
ruta_banck = "../train/images_banck"
ruta = ruta_banck + "/" + model
if not os.path.exists(ruta):
    os.makedirs(ruta)

Cam = cv.VideoCapture(1)
#Cam2 = cv.VideoCapture('C:/Users/llore/facial_recognition/train/videos/VID_20230117_150058.mp4')
ruidos = cv.CascadeClassifier("../train/haarcascades/haarcascade_frontalface_default.xml")
print(ruidos)
id = 1
while True:
    respuesta, Capture = Cam.read()
    if respuesta == False:break
    #Capture = imutils.resize(Capture, width =  640) #Reduce resolucion de la imagen

    gray = cv.cvtColor(Capture, cv.COLOR_BGR2GRAY)
    idCapture = Capture.copy()
    Face = ruidos.detectMultiScale(gray, 1.3, 5)

    for(x, y, e1, e2) in Face:
        cv.rectangle(Capture, (x, y), (x + e1, y + e2), (0, 0, 255), 1)
        FaceCaptured = idCapture[y:y+e1, x:x+e2]
        FaceCaptured = cv.resize(FaceCaptured, (160,160), interpolation= cv.INTER_CUBIC)
        cv.imwrite(ruta + "/Image_{}.jpg".format(id), FaceCaptured)
        id = id+1

    cv.imshow("Face", Capture)

    if id == 500:
        break

Cam.release()
cv.destroyAllWindows()