peluches = ["Perrote", "Gaturrio", "Mangote"]
opcion = 0

print("Pelucheria PELUCHOTES")
print(".......................")
print("1. Agregar producto a la bodega")
print("2. Ver productos en bodega")
print("3. Obtener valor del invetario")
print("4. Ver productos más vendidos")
print("5. SALIR")

while opcion != 5:
    opcion = int(input("Ingrese un numero: "))

    if opcion == 1:
        print("Usted está en la opcion 1")
    elif opcion == 2:
        print("Usted está en la opcion 2")
    elif opcion == 3:
        print("Usted está en la opcion 3")
    elif opcion == 4:
        print("Usted está en la opcion 4")
    else:
        print("Opcion no valida")

print("Sali del ciclo")