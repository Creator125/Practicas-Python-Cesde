from data.ListaUsuarios import usuarios
from helpers.crearCSV import crearCSVUsuarios
from helpers.crearHTML import crearTabla
import pandas as pd

#Usar la funcion crearSCVUsuarios
crearCSVUsuarios(usuarios, "bdUsuarios.csv")
#creando un dataframe desde una fuente CSV
dataFrameUsuarios = pd.read_csv('data/bdUsuarios.csv')
#convertir el DF en TABLA HTML
crearTabla(dataFrameUsuarios,'usuarios')

#Se filtran los datos
filtroUno = dataFrameUsuarios.query("Edad>30")
print(filtroUno)

print(" ")
print("-------------- Filtro de Usuarios --------------")
print(" ")

print("Sembradoras (mujeres) mayores de 40 años y su salario esta entre 1 salario a 2 salarios")
filtroSembradoras = dataFrameUsuarios.query("(Genero == 'Femenino') and (Edad > 40) and (Salario >= 10003000 or Salario <= 2000600)")
print(filtroSembradoras)

print("    ")

print("Sembradores menores de 20 años")
filtroMenores20 = dataFrameUsuarios.query("Edad < 20")
print(filtroMenores20)

print("    ")

print("Sembradores hombres mayores de 50 años")
filtroHombresMenores50 =dataFrameUsuarios.query("(Genero == 'Masculino') and (Edad > 50)")
print(filtroHombresMenores50)