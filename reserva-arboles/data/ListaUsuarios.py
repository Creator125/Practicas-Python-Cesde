import random
usuarios=[]

for _ in range(100):
    nombre=random.choice(['Juan','Andrea','Sara','Jorge'])
    contrasena=random.choice(['admin123','arboles000'])
    edad=random.randint(18,62)
    salario = random.randint(1160, 2000000)
    genero = random.choice(["Masculino", "Femenino", "No binario"])
    usuario=[nombre, contrasena, edad, salario, genero]
    usuarios.append(usuario)
