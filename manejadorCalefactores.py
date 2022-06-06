import numpy as np
from claseCalefactor import calefactor
from claseCalefactorGas import calefactorGas
from claseCalefactorElectrico import calefactorElectrico
import csv

class coleccion:
    __cantidad = 0
    __dimension = 10
    __incremento = 5
    __calefactores = None

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 5
        self.__incremento = 1
        self.__calefactores = np.empty(self.__dimension, dtype=calefactor)

    
    def agregarCalefactor(self, uncalefactor):
        if isinstance(uncalefactor, calefactor):
            if self.__cantidad == self.__dimension:
                self.__dimension += self.__incremento
                self.__calefactores.resize(self.__dimension)
            self.__calefactores[self.__cantidad] = uncalefactor
            self.__cantidad += 1

    
    def cargarCSV(self):
        archivo = open("calefactor-electrico.csv")
        reader = csv.reader(archivo, delimiter=";")
        archivo2 = open("calefactor-a-gas.csv")
        reader2 = csv.reader(archivo2, delimiter=";")
        for fila in reader:
                uncalefactor = calefactorElectrico(fila[0], fila[1], int(fila[2]))
                self.agregarCalefactor(uncalefactor)
        for fila in reader2:
            uncalefactor = calefactorGas(fila[0], fila[1], fila[2], int(fila[3]))
            self.agregarCalefactor(uncalefactor)
    

    def menor_consumo(self):
        i = 0
        while not isinstance(self.__calefactores[i], calefactorGas) and i < self.__dimension:
            i += 1
        if i == self.__dimension:
            i = -1
        if i != -1:
            minimo = self.__calefactores[i]
            for i in range(len(self.__calefactores)):
                if isinstance(self.__calefactores[i], calefactorGas):
                    if self.__calefactores[i] < minimo:
                        minimo = self.__calefactores[i]
            print("el calefactor a gas de menor consumo es: {}".format(minimo))
        else: print("error de carga de archivos")
    def menor_consumo_elec(self):
        i = 0
        while not isinstance(self.__calefactores[i], calefactorElectrico) and i < self.__dimension:
            i += 1
        if i == self.__dimension:
            i = -1
        if i != -1:
            minimo = self.__calefactores[i]
            for elem in self.__calefactores:
                if isinstance(elem, calefactorElectrico):
                    if elem < minimo:
                        minimo = elem
        return minimo
