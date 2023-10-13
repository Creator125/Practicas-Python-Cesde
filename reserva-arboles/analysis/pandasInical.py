import pandas as pd
from fincionSumar import sumarArboles

#Analizar una lisata de datos
ciudades = ["Medellin", "Venecia", "Chigorodó", "Turbo", "La Estrella", "Rionegro", "Andes","Bello", "Guatapé"]

#Analizar una lista de diccionarios
estudiantes = [
    {"id":1, "Nombre:":"Mario", "Promedio":4.2},
    {"id":2, "Nombre:":"Carla", "Promedio":3.0},
    {"id":3, "Nombre:":"Camilo", "Promedio":2.6},
    {"id":4, "Nombre:":"Tomas", "Promedio":5.0},
    {"id":5, "Nombre:":"Alejandra", "Promedio":4.0}
]

arbolesMunicipio = [
    {"id":1, "municipio":"Cáceres", "tipo":"N/A", "cantidad":2736}
]

#Convirtiendo lista y lista de diccionarios en DATAFRAME
dataframe1 = pd.DataFrame(ciudades)
dataframe2 = pd.DataFrame(estudiantes)

print(dataframe1)
print(dataframe2)

numeroArbolesOriente = 1200000
numeroArbolesSuroeste = 3000000
numeroArbolesNorte = 4000000
sumatriaOrienteNorte = sumarArboles(numeroArbolesNorte, numeroArbolesOriente)
sumetoriaSuroesteOriente = sumarArboles(numeroArbolesSuroeste, numeroArbolesOriente)

#Analizar un CSV