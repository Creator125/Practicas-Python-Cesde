"""
2. Recibir por teclado N(Cantidad digitada por el usuario) frutas para hacer un salpicón cada 
fruta debe tener id, nombre , precio Unitario y cantidad, el programa debe permitir:

-Mostar el costo total de un salpicón

-Mostrar todas las frutas que se digitaron ordenadas de mayor a menor costo

-Mostrar cual es la fruta más barate y más cara
"""

import random

print("Salpiconeria")
print("0. SALIR")
print("1. Ingresar frutas")
print("2. Mostar costo total del salpicon")
print("3. Mostrar todas las frutas")
print("4. mostrar la fruta más barata")

cantidad = int(input("Ingrese la cantidad de frutas a ingresar: "));
frutas = []
opcion = 10

while opcion != 0:
    opcion = int(input("Ingrese una opcion: "))
    frutaIngresada = {}
    
    if opcion == 1:
        frutaIngresada["id"] = random.randint(1, cantidad)
        frutaIngresada["nombre"] = input("Ingrese el nombre de la fruta: ")
        frutaIngresada["precio"] = float(input("Ingrese el precio de la fruta: "))
        frutaIngresada["cantidad"] = int(input("Ingrese la cantidad: "))
        
        frutas.append(frutaIngresada)
        
        print("Frutas ingresadas correctamente")
    elif opcion == 2:
        valorSalpicon = 0
        
        for fruta in frutas:
            valorSalpicon += fruta["precio"]
            
        print("El valor total del salpicon es: "+ valorSalpicon)
    elif opcion == 3:
        for fruta in frutas:
            print(fruta.sort())
    elif opcion == 4:
        pass
    else:
        print("Opcion invalida")
    