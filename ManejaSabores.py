from claseSabor import Sabor
from ManejaHelados import manHelados
from claseHelado import Helado
import csv
class manSabores:
    __sabores=[]
    __helados_vendidos = [] 
    __contador_sabores = 0

    def __init__(self):
        self.__sabores=[]
        self.__helados_vendidos = [] 
        self.__contador_sabores = 0
        self.gramos_por_sabor = {}

    def cargaSabores(self):

        archivo=open('sabores.csv')
        reader = csv.reader(archivo, delimiter = ',')
        band=True
        for fila in reader:
            if band:
                band=False
            else:
                unSabor = Sabor(int(fila[0]), fila[1], fila[2])
                self.__sabores.append(unSabor)
        print('Los sabores de helado fueron cargados exitosamente')
        archivo.close()


    def getSabores(self):

        return self.__sabores
    
    def contadorSabores(self):

        return self.__contador_sabores


    def obtenerSaborPorID(self, idSabor):
        sabor_encontrado = None
        sabor_correcto = False
        indice = 0
        while indice < len(self.__sabores) and not sabor_correcto:
            if self.__sabores[indice].getID() == idSabor:
                sabor_encontrado = self.__sabores[indice]
                sabor_correcto = True
            indice += 1

        if sabor_correcto:
            print(f"Sabor encontrado: {sabor_encontrado.getNombre()}")
        else:
            print("Sabor incorrecto")

        return sabor_encontrado

    def registrarHeladoVendido(self):
        # Mostrar opciones de tamaños de helado
        print("Tipos de helado disponibles:")
        print("1. 100 gr")
        print("2. 150 gr")
        print("3. 250 gr")
        print("4. 500 gr")
        print("5. 1000 gr")
        
        # Solicitar los datos del helado al usuario
        gramos = float(input("Ingrese los gramos del helado: "))
        precio = float(input("Ingrese el precio del helado: "))

        helado = Helado(gramos, precio)

  
        tipo_helado = input("Ingrese el tipo de helado (número correspondiente): ")

        # Mapear la opción ingresada al tamaño correspondiente
        if tipo_helado == "1":
            helado.setTipo("100 gr")
        elif tipo_helado == "2":
            helado.setTipo("150 gr")
        elif tipo_helado == "3":
            helado.setTipo("250 gr")
        elif tipo_helado == "4":
            helado.setTipo("500 gr")
        elif tipo_helado == "5":
            helado.setTipo("1000 gr")
        else:
            print("Opción inválida.")


        # Mostrar los sabores disponibles
        print("Sabores disponibles:")
        for sabor in self.getSabores():
            print(f"ID: {sabor.getID()} - Nombre: {sabor.getNombre()}")

        # Solicitar los sabores del helado al usuario
        sabores_elegidos = []
        id_sabor = int(input("Ingrese el ID del sabor (0 para terminar): "))
        while id_sabor != 0:
            sabor_encontrado = None
            for sabor in self.getSabores():
                if sabor.getID() == id_sabor:
                    sabor_encontrado = sabor

            if sabor_encontrado is not None:
                sabor.aumentaContador()
                sabores_elegidos.append(sabor_encontrado)
            else:
                print("ID de sabor inválido.")
            id_sabor = int(input("Ingrese el ID del sabor (0 para terminar): "))

        # Calcular los gramos vendidos por sabor
        gramos_vendidos_sabor = gramos / len(sabores_elegidos)
        for sabor in sabores_elegidos:
            sabor_id = sabor.getID()
            if sabor_id in self.gramos_por_sabor:
                self.gramos_por_sabor[sabor_id] += gramos_vendidos_sabor
            else:
                self.gramos_por_sabor[sabor_id] = gramos_vendidos_sabor

        helado.setSabor(sabores_elegidos)

        # Agregar el helado a la lista de helados vendidos
        self.__helados_vendidos.append(helado)

    def getHeladosVendidos(self):
        return self.__helados_vendidos

    def ordenarSabores(self):
        sabores_ordenados = sorted(self.__sabores, key=lambda sabor: sabor.getContador(), reverse=True)
        return sabores_ordenados

    def consultarGramosVendidosPorSabor(self):
            numero_sabor = int(input("Ingrese el número de sabor para consultar los gramos vendidos: "))
            if numero_sabor in self.gramos_por_sabor:
                gramos_vendidos = self.gramos_por_sabor[numero_sabor]
                sabor = self.obtenerSaborPorID(numero_sabor)
                print(f"Gramos vendidos para el sabor {sabor.getNombre()}: {gramos_vendidos} gramos")
            else:
                print("El número de sabor ingresado no corresponde a ningún sabor vendido.")

    def mostrarSaboresPorTipoHelado(self):
        # Mostrar opciones de tamaños de helado
        print("Tipos de helado disponibles:")
        print("1. 100 gr")
        print("2. 150 gr")
        print("3. 250 gr")
        print("4. 500 gr")
        print("5. 1000 gr")

        tipo_helado = input("Ingrese el tipo de helado (número correspondiente): ")

        # Validar opción ingresada
        if tipo_helado not in ["1", "2", "3", "4", "5"]:
            print("Opción inválida.")
            return

        # Obtener el tipo de helado correspondiente a la opción ingresada
        tipos_helado = ["100 gr", "150 gr", "250 gr", "500 gr", "1000 gr"]
        tipo_seleccionado = tipos_helado[int(tipo_helado) - 1]

        # Filtrar los helados vendidos por el tipo seleccionado
        helados_filtrados = [helado for helado in self.__helados_vendidos if helado.getTipo() == tipo_seleccionado]

        # Mostrar los sabores vendidos en ese tamaño
        if len(helados_filtrados) > 0:
            print(f"Sabores vendidos en el tipo de helado {tipo_seleccionado}:")
            for helado in helados_filtrados:
                sabores = helado.getSabor()
                for sabor in sabores:
                    print(f"Sabor: {sabor.getNombre()}")
        else:
            print(f"No se encontraron helados vendidos en el tipo de helado {tipo_seleccionado}.")

        
    def calcularImporteTotalPorTipo(self):
        importe_por_tipo = {}  # Diccionario para almacenar el importe total por tipo de helado
        #para almacenar el importe total por tipo de helado. Se utiliza un diccionario porque se desea asociar cada tipo de helado con su respectivo importe total.
        # En cada iteración del bucle for, se obtiene el tipo de helado y el precio del helado actual. Luego, se verifica si el tipo de helado ya está presente como una clave en el diccionario importe_por_tipo. Si es así, se incrementa el importe total sumando el precio del helado actual al valor existente en el diccionario. 
        # Si el tipo de helado no está presente, se agrega como una nueva clave en el diccionario con el importe del helado actual como su valor.

        for helado in self.__helados_vendidos:
            tipo_helado = helado.getTipo()
            precio_helado = helado.getPrecio()

            if tipo_helado in importe_por_tipo:
                importe_por_tipo[tipo_helado] += precio_helado
            else:
                importe_por_tipo[tipo_helado] = precio_helado

        return importe_por_tipo


    def mostrarImporteTotalPorTipo(self):
        importe_por_tipo = self.calcularImporteTotalPorTipo()

        print("Importe total recaudado por tipo de helado:")
        for tipo_helado, importe in importe_por_tipo.items():
            print(f"Tipo: {tipo_helado} - Importe total: ${importe}")







