import cv2
from pylsl import StreamInlet, resolve_stream
import pandas as pd
import random
import time
import keyboard
import serial
ser = serial.Serial('COM11', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)  # open serial port

Datos_acumulados,DatosDescansos=[],[]
datos="1"


def Data():
    name = "S"+Subject+Tipo
    im = cv2.imread('D:/GoogleDrive/F_BLOG/GITHUB/OpenBCI/Imagenes/Baseline.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    inicio=time.time()
    while True:
        sample, t = inlet.pull_sample()
        Datos_acumulados.append(sample)
        if len(Datos_acumulados) == 500:
            print("Tiempo de adquisicion:" ,(time.time() - inicio))
            cv2.waitKey(1)
            df = pd.DataFrame(Datos_acumulados)
            df.to_csv("D:/GoogleDrive/F_BLOG/GITHUB/OpenBCI/Recoleccion/" + name + '.csv')
            Datos_acumulados.clear()
            break




Subject = input('Ingresar identificación del sujeto: ')
Tipo = input('Ingresar el tipo de experimento a realizar (M/I/O): ')   # Tipos posibles M , I , O

print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
# inlet = StreamInlet(streams[0])



while __name__ == '__main__':
    if keyboard.is_pressed("r"):
        print("")
        cv2.waitKey(1)
        Data()
    else:
        img = cv2.imread('D:/GoogleDrive/F_BLOG/GITHUB/OpenBCI/Imagenes/Descanso.jpg')
        cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Image', img)
        cv2.waitKey(10)

