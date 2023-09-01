print("****Fiesta de comemoracion****")
print("***************")
print("0. SALIR")
print("1. Registrar invitado")
print("2. Ver lista de invitados")
print("3. Ver invitados VIP")
print("4. Combranza")
print("5. Editar información")
print("6. Retirar invitados")
print("***************")

opcion = int(input("Ingrese una opcion: "))
usuarios = []

while opcion != 0:
    invitado = {}
    
    if opcion == 1:
        invitado["nombre"] = input("Ingrese su nombre: ")
        invitado["id"] = int(input("Ingrese su id: "))
        invitado["cedula"] = input("Ingrese su cedula: ")
        invitado["eps"] = input("Ingrese su eps: ")
        invitado["estadoPago"] = bool(input("Ya pagó: "))
        invitado["valorCuota"] = float(input("Ingrese la cuota: "))
        invitado["edad"] = int(input("Ingrese su edad: "))
        
        usuarios.append(invitado)
    elif opcion == 2:
        #Recorriendo una lista
        for persona in usuarios:
            print(f"persona: {persona['nombre']}")
    elif opcion == 3:
        for persona in usuarios:
            if persona["estado"] == True:
                print(persona)
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        pass
    else:
        print("Opcion invalida")