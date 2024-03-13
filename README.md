# Facial Recognition

<div align="center" style="width: 200px;">
  <img alt="GIF" src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2c2M2RoNXc4ZGhucGRkaHBxbDI5MWN1N3RzanZ3c3FxeDZnMjhvaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RTY2fxDkDw2NWIEsLy/giphy.gif" width="50%"/>
</div>

----------------

## Overview

El script proporciona una aplicación de reconocimiento facial en tiempo real utilizando OpenCV, una biblioteca popular de visión por computadora. 
Se compone de tres partes: la detección y captura de rostros, el uso de un modelo previamente entrenado para reconocer rostros y la visualización de los resultados.

### Tecnologías Utilizadas

![Python](https://www.vectorlogo.zone/logos/python/python-ar21.svg) ![Opencv](https://www.vectorlogo.zone/logos/opencv/opencv-ar21.svg)


## Requirements

1. Instala las bibliotecas requeridas:

   ```bash
   pip install -r requirements.txt


## Main Features

  **Face Detection and Capture:** 
  
  * Utiliza la cámara en vivo para capturar imágenes.
  * Emplea un clasificador en cascada de Haar para detectar rostros en la imagen.
  * Una vez detectado un rostro, lo recorta y ajusta su tamaño para prepararlo para el reconocimiento.
  
  **Facial Recognition:**
  
  * Utiliza un modelo de reconocimiento facial previamente entrenado.
  * Lee el modelo desde un archivo XML que contiene los datos de entrenamiento.
  * Aplica el modelo para predecir la identidad de los rostros capturados.
  
  **Viewing Results:**
  
  * Dibuja cuadros delimitadores alrededor de los rostros detectados.
  * Muestra la etiqueta de la identidad predicha encima de cada rostro.
  * Si la confianza de la predicción es alta, muestra el nombre correspondiente a esa identidad.
  * Si la confianza es baja, muestra "No encontrado".

## Usage

   **Ruta de Carpeta Personalizable:**

   * El usuario puede especificar las carpetas donde se recolectaran o guardaran los rostros para el entrenamiento.


## Detection

<div align="center" style="width: 200px;">
  <img alt="GIF" src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmR6eTYzdDA5ZTE3YmhtYm43NzUzczNjY21mNm8xdzA1Z2p0YmQ2diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/I4GqDHPQ3qgHZr7s8E/giphy.gif" width="50%"/>
</div>







