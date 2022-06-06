from manejadorCalefactores import coleccion

class menu:
    __op = 0
    def __init__(self):
        self.__op = 0
        self.__calefactores = coleccion()
    def opciones(self):
        self.__calefactores.cargarCSV()
        salir = True
        while salir:
            print("menu".center(14,"-"))
            print("opcion 1 : mostrar calefactor a gas de menor consumo")
            print("opcion 2: buscar calefactor electrico de menor consumo")
            print("opcion 3:")
            print("opcion 4 : SALIR")
            self.__op = int(input("ingrese opcion"))
            if self.__op == 1:
                costo = int(input("ingresar costo por m³"))
                cantidad = int(input("ingrese cantidad que se estima consumir"))
                self.__calefactores.menor_consumo()
            elif self.__op == 2:
                costok = int(input("ingrese kilowatt/h"))
                cantidadH = int(input("ingrese la cantidad que se estima a consumir por hora"))
                menorConsumo = self.__calefactores.menor_consumo_elec()
                print(" el costo va a ser de: {} watts".format(menorConsumo.get_potencia() * cantidadH * (costok*100)) )
                print("la marca y modelo del calefactor electrico de menor consumo es: {}  {}". format(menorConsumo.get_marca(), menorConsumo.get_modelo()))
            elif self.__op == 3:
                print()
            elif self.__op == 4:
                salir = not salir
                print("finalizando programa".center(30,"-"))
            else: 
                print("opcion incorrecta")
                self.__op = int(input("vuelva a ingresar opcion"))