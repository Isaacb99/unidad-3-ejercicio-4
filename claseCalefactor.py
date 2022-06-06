

class calefactor:
    __marca = ''
    __modelo = ''
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
    def __str__(self):
        return "marca: {}, modelo: {}".format(self.__marca, self.__modelo)
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo