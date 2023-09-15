"""
1. Codificar un programa que le permita a un organizador de un festival de música tener 
un menú de opciones realizado en Python que permita:

-Registrar una agrupación musical, cada una con: id, nombre, genero, hora 
en la que se presenta, pago que se le da a la agrupación, estado (true si ya se presentó/
false si aún no han tocado)

-Buscar y mostrar en consola todas las bandas que no se han presentado

-Cambiar la hora de presentación de una agrupación que no se haya presentado aún

-Retirar una agrupación que no se ha presentado del listado de agrupaciones
"""
import random

print("Festival musical")
print("0. SALIR")
print("1. Registrar una agrupación musical")
print("2. Mostrar bandas que aun no se presentaron")
print("3. Cambiar la hora de presentación de una agrupación")
print("4. Retirar una agrupació")

opcion = 10
grupos = []

while opcion != 0:
    opcion = int(input("Ingrese una opcion: "))
    agrupacionMusical = {}

    if opcion == 1:
        agrupacionMusical["id"] = random.randint(1, 100)
        agrupacionMusical["nombre"] = input("Ingrese el nombre de la agrupacion musical: ")
        agrupacionMusical["genero"] = input("Ingrese el genero: ")
        agrupacionMusical["horaPresentacion"] = input("Ingrese la hora: ")
        agrupacionMusical["pago"] = float(input("Ingrese el pago: "))
        agrupacionMusical["estado"] = int(input("¿Se pesentó? 1(Si) o 0(No): "))
        
        grupos.append(agrupacionMusical)
    elif opcion == 2:
        for banda in grupos:
            if banda["estado"] == 0:
                print(banda)
    elif opcion == 3:
        idAgrupacion = input("Ingrese el id de la agrupación cuya hora de presentación desea cambiar: ")
        
        for banda in grupos:
            if banda["id"] == idAgrupacion and banda["estado"] == 0:
                nueva_hora = input("Ingrese la nueva hora de presentación: ")
                banda["horaPresentacion"] = nueva_hora
                print(f"La hora de presentación de {idAgrupacion} se ha actualizado a {nueva_hora}.")
                break
        else:
            print(f"No se encontró la agrupación con el nombre '{idAgrupacion}' o ya se ha presentado.")
    elif opcion == 4:
        idAgrupacion = int(input("Ingrese el id de la agrupacion a eliminar: "))
        
        for banda in grupos:
            if banda["id"] == idAgrupacion and banda["estado"] == 0:
                grupos.remove(banda)
                
                print(f"Agrupación con ID {idAgrupacion} eliminada.")
            else:
                print(f"No se encontró la agrupación con ID {idAgrupacion} o ya se ha presentado.")
            
    else:
        print("Opcion invalida")