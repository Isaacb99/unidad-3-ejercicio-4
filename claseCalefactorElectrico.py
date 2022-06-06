from claseCalefactor import calefactor

class calefactorElectrico(calefactor):
    __potencia_maxima = 0
    def __init__(self, marca, modelo, potencia):
        super().__init__(marca, modelo)
        self.__potencia_maxima = potencia
    def __str__(self):
        v = ''
        v = super().__str__()
        v += ' ' + "potencia maxima: {}watts". format(self.__potencia_maxima)
        return v
    def get_marca(self):
        return super().get_marca()
    def get_modelo(self):
        return super().get_modelo()
    def get_potencia(self):
        return self.__potencia_maxima
    def __lt__(self, otro):
        return self.__potencia_maxima < otro.get_potencia()