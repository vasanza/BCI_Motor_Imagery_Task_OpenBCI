import cv2
from pylsl import StreamInlet, resolve_stream
import pandas as pd
import random
import time
import keyboard
import serial
ser = serial.Serial('COM13', 9600, timeout=0, parity=serial.PARITY_NONE, rtscts=1)  # open serial port

Datos_acumulados,DatosDescansos=[],[]
datos="1"


def Data():
    name = "DATO"
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
            df.to_csv("D:/GoogleDrive/F_BLOG/GITHUB/OpenBCI/BCI_AWARD/" + name + '.csv')
            Datos_acumulados.clear()
            break




#Subject = input('Ingresar identificación del sujeto: ')
#Tipo = input('Ingresar el tipo de experimento a realizar (M/I/O): ')   # Tipos posibles M , I , O

print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
# inlet = StreamInlet(streams[0])


Inicio=True
while __name__ == '__main__':
    if Inicio or ser.inWaiting():
        packet = ser.readline()
        senal=packet.decode('utf')
        print(packet.decode('utf'))
        if Inicio or senal == "A":
            cv2.waitKey(1)
            Data()
            ser.write(b'B')  # write a string
    else:
        img = cv2.imread('D:/GoogleDrive/F_BLOG/GITHUB/OpenBCI/Imagenes/Descanso.jpg')
        cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Image', img)
        cv2.waitKey(10)
    Inicio=False
