import random

usuarios = []

for _ in range(10):
    nombre = random.choice(["Juan", "Carlos", "Camilo", "Maria"])
    contrasena = random.choice(["Querido", "Perrotemio12", "huevoCalido23"])
    edad = random.randint(18, 62)
    usuario = [nombre, contrasena, edad]
    usuarios.append(usuario)
    
print(usuarios)