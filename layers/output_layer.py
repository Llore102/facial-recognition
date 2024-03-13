import cv2 as cv
import os 

data_train = ("../train/images_banck")
listData = os.listdir(data_train)

TrainingModel1 = cv.face.EigenFaceRecognizer_create()
TrainingModel1.read("../train/model_training/Training_EigenFaceRecognizer.xml")
Ruidos = cv.CascadeClassifier("../train/haarcascades/haarcascade_frontalface_default.xml")
Cam = cv.VideoCapture(1)
while True:
    _,Capture = Cam.read()
    gray = cv.cvtColor(Capture, cv.COLOR_BGR2GRAY)
    idCapture = gray.copy()
    Face = Ruidos.detectMultiScale(gray, 1.3, 5)
    for(x, y, e1, e2) in Face:
        cv.rectangle(Capture, (x, y), (x + e1, y + e2), (0, 0, 255), 2)
        FaceCaptured = idCapture[y:y+e2, x:x+e1]
        FaceCaptured = cv.resize(FaceCaptured, (160,160), interpolation= cv.INTER_CUBIC)
        resultado = TrainingModel1.predict(FaceCaptured)
        cv.putText(Capture, '{}'.format(resultado), (x, y-5), 1,1.1, (0,0,255), 1, cv.LINE_AA)#Etiqueta
        if resultado[1] < 7500:
            cv.putText(Capture, '{}'.format(listData[resultado[0]]), (x, y-40), 2,1.1, (0,255,0), 1, cv.LINE_AA)
            cv.rectangle(Capture, (x, y), (x+e1, y+e2), (255,0,0), 2)
        else: 
            cv.putText(Capture, "No encontrado", (x, y-20), 1,1.6, (255,0,0), 1, cv.LINE_AA)
            cv.rectangle(Capture, (x, y), (x+e1, y+e2), (255,0,0), 2)

    cv.imshow("Resultado", Capture)
    if cv.waitKey(1) == ord('q'):
        break
Cam.release()
cv.destroyAllWindows()
