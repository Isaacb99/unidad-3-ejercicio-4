from claseCalefactor import calefactor

class calefactorGas(calefactor):
    __matricula = ''
    __calorias = 0
    def __init__(self, marca, modelo, matricula, calorias):
        super().__init__(marca, modelo)
        self.__matricula = matricula
        self.__calorias = calorias
    def __str__(self):
        v = ''
        v = super().__str__()
        v += ' ' + "matricula: {}, calorias: {}kilocalorias/m³".format(self.__matricula, self.__calorias)
        return v
    def get_calorias(self):
        return self.__calorias
    def __lt__(self, otro):
        return self.__calorias < otro.get_calorias()