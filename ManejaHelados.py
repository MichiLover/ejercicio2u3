from claseHelado import Helado
class manHelados:
    __helados=[]

    def __init__(self):
        self.__helados=[]

    def registrarHeladoVendido(self,gramos,precio):

        unHelado=Helado(gramos,precio)
        self.__helados.append(unHelado)

    def getHelados(self):

        return self.__helados

