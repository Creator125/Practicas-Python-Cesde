import random

refrigerios=[]

for _ in range(10):
    tipo=random.choice(['desayuno', 'armuezo', 'cena'])
    nombre=random.choice(['Yogur', 'Barras de granola', 'Delicias de pollo', 'Frutas enlatada'])
    precio=random.randint(50, 30000)
    cantidad = random.randint(1, 1000)
    refrigerio=[tipo, nombre, precio, cantidad]
    refrigerios.append(refrigerio)

