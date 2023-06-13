class Helado:
    __gramos=''
    __precio=''
    __xsabor=''
    __tipo=''

    def __init__(self,gr,pr):
        self.__gramos=float(gr)
        self.__precio=float(pr)
        self.__xsabor = []
        self.__tipo = None

    def getGramos(self):
        return self.__gramos

    def getPrecio(self):
        return self.__precio

    #Toma una lista de sabores como argumento y utiliza el método extend() para agregar los elementos de la lista al atributo __sabores del helado.
    def setSabor(self, xs):
        self.__xsabor.extend(xs)

    def getSabor(self):
        return self.__xsabor

    def setTipo(self, tipo):
        self.__tipo = tipo

    def getTipo(self):
        return self.__tipo