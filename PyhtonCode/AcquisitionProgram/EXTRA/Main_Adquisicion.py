import cv2
from pylsl import StreamInlet, resolve_stream
import pandas as pd
import random
import time

DatosBEO, DatosLCH, DatosRCH, DatosLDF, DatosLPF, DatosRDF, DatosRPF, DatosDescanso = [], [], [], [], [], [], [], []
BEO, LCH, RCH, LDF, LPF, RDF, RPF, Descanso = "1", "2", "3", "4", "5", "6", "7", "8"
beo, lch, rch, ldf, lpf, rdf, rpf, des = 0, 0, 0, 0, 0, 0, 0, 0
ide = 0


def mainlch():
    name = "S"+Subject+"R"+str(Run)+Tipo+LCH
    im = cv2.imread('C:/Users/HP/Documents/Project_Signals/Imagenes/LCH.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    inicio1=time.time()
    while True:
        sample, t = inlet.pull_sample()
        DatosLCH.append(sample)
        if len(DatosLCH) == 500:
            print("LCH" ,(time.time() - inicio1))
            cv2.waitKey(1)
            df = pd.DataFrame(DatosLCH)
            df.to_csv("C:/Users/HP/Documents/Project_Signals/Recoleccion/" + name + "_" +
                      str(lch) + '.csv')
            DatosLCH.clear()
            break


def mainrch():
    name = "S"+Subject+"R"+str(Run)+Tipo+RCH
    im = cv2.imread('C:/Users/HP/Documents/Project_Signals/Imagenes/RCH.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    inicio2=time.time()
    while True:
        sample, t = inlet.pull_sample()
        DatosRCH.append(sample)
        if len(DatosRCH) == 500:
            print("RCH" , (time.time() - inicio2))
            cv2.waitKey(1)
            df = pd.DataFrame(DatosRCH)
            df.to_csv("C:/Users/HP/Documents/Project_Signals/Recoleccion/" + name+"_" +
                      str(rch) + '.csv')
            DatosRCH.clear()
            break


def mainldf():
    name = "S"+Subject+"R"+str(Run)+Tipo+LDF
    im = cv2.imread('C:/Users/HP/Documents/Project_Signals/Imagenes/LDF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    inicio3=time.time()
    while True:
        sample, t = inlet.pull_sample()
        DatosLDF.append(sample)
        if len(DatosLDF) == 500:
            print("LDF" , (time.time() - inicio3))
            cv2.waitKey(1)
            df = pd.DataFrame(DatosLDF)
            df.to_csv("C:/Users/HP/Documents/Project_Signals/Recoleccion/" + name+"_" +
                      str(ldf) + '.csv')
            DatosLDF.clear()
            break


def mainlpf():
    name = "S"+Subject+"R"+str(Run)+Tipo+LPF
    im = cv2.imread('C:/Users/HP/Documents/Project_Signals/Imagenes/LPF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    inicio4=time.time()
    while True:
        sample, t = inlet.pull_sample()
        DatosLPF.append(sample)
        if len(DatosLPF) == 500:
            print("LPF" , (time.time() - inicio4))
            cv2.waitKey(1)
            df = pd.DataFrame(DatosLPF)
            df.to_csv("C:/Users/HP/Documents/Project_Signals/Recoleccion/" + name + "_" +
                      str(lpf) + '.csv')
            DatosLPF.clear()
            break


def mainrdf():
    name = "S"+Subject+"R"+str(Run)+Tipo+RDF
    im = cv2.imread('C:/Users/HP/Documents/Project_Signals/Imagenes/RDF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    inicio5=time.time()
    while True:
        sample, t = inlet.pull_sample()
        DatosRDF.append(sample)
        if len(DatosRDF) == 500:
            print("RDF" , (time.time() - inicio5))
            cv2.waitKey(1)
            df = pd.DataFrame(DatosRDF)
            df.to_csv("C:/Users/HP/Documents/Project_Signals/Recoleccion/" + name + "_" +
                      str(rdf) + '.csv')
            DatosRDF.clear()
            break


def mainrpf():
    name = "S"+Subject+"R"+str(Run)+Tipo+RPF
    im = cv2.imread('C:/Users/HP/Documents/Project_Signals/Imagenes/RPF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    inicio6=time.time()
    while True:
        sample, t = inlet.pull_sample()
        DatosRPF.append(sample)
        if len(DatosRPF) == 500:
            print("RPF" , (time.time() - inicio6))
            cv2.waitKey(1)
            df = pd.DataFrame(DatosRPF)
            df.to_csv("C:/Users/HP/Documents/Project_Signals/Recoleccion/" + name + "_" +
                      str(rpf) + '.csv')
            DatosRPF.clear()
            break


def mainbeo():
    name = "S"+Subject+"R"+str(Run)+Tipo+BEO
    im = cv2.imread('C:/Users/HP/Documents/Project_Signals/Imagenes/Baseline.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    inicio7=time.time()
    while True:
        sample, t = inlet.pull_sample()
        DatosBEO.append(sample)
        if len(DatosBEO) == 500:
            print("BEO" , (time.time() - inicio7))
            cv2.waitKey(1)
            df = pd.DataFrame(DatosBEO)
            df.to_csv("C:/Users/HP/Documents/Project_Signals/Recoleccion/" + name + "_" +
                      str(beo) + '.csv')
            DatosBEO.clear()
            break


def descanso():
    name = "S"+Subject+"R"+str(Run)+Tipo+Descanso+"_"+ide
    img = cv2.imread('C:/Users/HP/Documents/Project_Signals/Imagenes/Descanso.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Image', img)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    inicio8=time.time()
    while True:
        sample, t = inlet.pull_sample()
        DatosDescanso.append(sample)
        if len(DatosDescanso) == 500:
            print("DESCANSO" , (time.time() - inicio8))
            cv2.waitKey(1)
            df = pd.DataFrame(DatosDescanso)
            df.to_csv("C:/Users/HP/Documents/Project_Signals/Recoleccion/" + name + "_" +
                      str(des) + '.csv')
            DatosDescanso.clear()
            break


operaciones = {'1': mainlch, '2': mainrch, '3': mainldf, '4': mainlpf, '5': mainrdf, '6': mainrpf}

Subject = input('Ingresar identificación del sujeto: ')
Tipo = input('Ingresar el tipo de experimento a realizar (M/I/O): ')   # Tipos posibles M , I , O
Run = int(input('Ingresar el número de serie: '))

print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
# inlet = StreamInlet(streams[0])

valores = 0

while __name__ == '__main__':
    # descanso()
    mainbeo()
    beo += 1
    des = beo
    ide = BEO
    descanso()

    while valores != 30:
        valores = lch + rch + ldf + lpf + rdf + rpf
        print(valores)
        opcion = str(random.randint(1, 6))
        if opcion == '1' and lch != 5:
            operaciones[opcion]()
            lch += 1
            des = lch
            ide = LCH
            descanso()

        elif opcion == '2' and rch != 5:
            operaciones[opcion]()
            rch += 1
            des = rch
            ide = RCH
            descanso()

        elif opcion == '3' and ldf != 5:
            operaciones[opcion]()
            ldf += 1
            des = ldf
            ide = LDF
            descanso()

        elif opcion == '4' and lpf != 5:
            operaciones[opcion]()
            lpf += 1
            des = lpf
            ide = LPF
            descanso()

        elif opcion == '5' and rdf != 5:
            operaciones[opcion]()
            rdf += 1
            des = rdf
            ide = RDF
            descanso()

        elif opcion == '6' and rpf != 5:
            operaciones[opcion]()
            rpf += 1
            des = rpf
            ide = RPF
            descanso()

    valores, lch, rch, ldf, lpf, rdf, rpf = 0, 0, 0, 0, 0, 0, 0
    continuar = input("Desea continuar (S/N) :")
    if continuar == 'N' or continuar == 'n':
        break
    else:
        Run += 1
