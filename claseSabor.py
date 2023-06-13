class Sabor:
    __identificador=''
    __ingredientes=''
    __nombre=''
    __contador=0

    def __init__(self,ident,ingr,nom):
        self.__identificador=ident
        self.__ingredientes=ingr
        self.__nombre=nom
        self.__contador=0

    def getID(self):

        return self.__identificador

    def getIngredientes(self):
        
        return self.__ingredientes

    def getNombre(self):

        return self.__nombre
    
    def aumentaContador(self):

        self.__contador+=1

    def getContador(self):

        return self.__contador
