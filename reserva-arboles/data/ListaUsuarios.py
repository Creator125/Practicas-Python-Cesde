import random
usuarios=[]

for _ in range(10):
    nombre=random.choice(['Juan','Andrea','Sara','Jorge'])
    contrasena=random.choice(['admin123','arboles000'])
    edad=random.randint(18,62)
    salario = random.randint(1160, 2000000)
    genero = random.choice(["Masculino", "Femenino", "No binario"])
    usuario=[nombre, contrasena, edad, salario, genero]
    usuarios.append(usuario)

'''
usuarios = []

for _ in range(10):
    nombre = random.choice(["Juan", "Carlos", "Camilo", "Maria"])
    contrasena = random.choice(["Querido", "Perrotemio12", "huevoCalido23"])
    edad = random.randint(18, 62)
    salario = random.randint(1160, 2000000)
    genero = random.choice(["Masculino", "Femenino", "No binario"])
    usuario = [nombre, contrasena, edad, salario, genero]
    usuarios.append(usuario)
print(usuarios)
'''