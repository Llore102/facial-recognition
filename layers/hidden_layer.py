import cv2 as cv
import os
import numpy as np
from time import time

data_Train = ("../train/images_banck")
ListData = os.listdir(data_Train)
#print("Data", ListData)

ids = []
faceData = []
id = 0
TiempoInicial = time()
for L in ListData:
    ruta = os.path.join(data_Train, L)
    print("Lectura de Carpetas..")
    for archivo in os.listdir(ruta):
        print("Images: ", L + "/" + archivo )
        ids.append(id)
        #faceData.append(cv.imread(ruta + "/" + archivo, 0))
        faceData.append(cv.imread(os.path.join(ruta, archivo), cv.IMREAD_GRAYSCALE))
        images = cv.imread(ruta + "/" + archivo, 0)
        
    id = id + 1
    TiempoFinal = time()
    TiempoTotal =  TiempoFinal - TiempoInicial
    print("Tiempo Total De Lectura: ", TiempoTotal)

trainingModel1 = cv.face.EigenFaceRecognizer_create()
print("Entrenando modelo...")
trainingModel1.train(faceData, np.array(ids))

tiempoFinalDeEntrenamiento = time()
tiempoFinalDeEntrenamiento = tiempoFinalDeEntrenamiento - TiempoTotal
print("Tiempo Total De Entrenamiento:", tiempoFinalDeEntrenamiento)

trainingModel1.write("../train/model_training/Training_EigenFaceRecognizer.xml")
print("Modelo Entrenado..")