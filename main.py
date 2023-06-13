from claseHelado import Helado
from claseSabor import Sabor
from ManejaHelados import manHelados
from ManejaSabores import manSabores
import csv

if __name__=="__main__":

    MS=manSabores()
    MS.cargaSabores()
    MH=manHelados()
    opcion = -1
    
    while opcion != 0:
        menu=int(input("Elegir opcion: \n 1-Registrar helado vendido \n 2-Mostrar el nombre de los 5 sabores de helado mas pedidos\n 3-Elegir un sabor para estimar los gramos vendidos\n 4-Ingresar un tipo de helado\n 5-Determinar importe total\n"))
        if menu == 1:
                #1.Registrar un helado vendido (instancia de la clase helado).
                print("Actividad 1")
                MS.registrarHeladoVendido()

        elif menu == 2:
            #2.Mostrar el nombre de los 5 sabores de helado más pedidos.
            print("Actividad 2")
            sabores_ordenados = MS.ordenarSabores()
            print("Sabores más pedidos:")
            for sabor in sabores_ordenados[:5]: #indico que quiero mostrar los 5 mas pedidos
                print(f"Nombre: {sabor.getNombre()} - Contador: {sabor.getContador()}")

        elif menu == 3:
            #Primero necesito los gramos de ese helado, y necesito saber cuantos sabores se eligieron
            #Necesito un contador de sabores
            print("Actividad 3")
            MS.consultarGramosVendidosPorSabor()

        elif menu == 4:

            print("Actividad 4")
            MS.mostrarSaboresPorTipoHelado()

        elif menu == 5:
            print("Actividad 5")

            MS.calcularImporteTotalPorTipo()
            MS.mostrarImporteTotalPorTipo()

        elif menu == 0:

            opcion = 0  # Si la opción es cero, salimos del bucle principal
            

        else:

            print("Opción inválida. Elija otra opción válida.")