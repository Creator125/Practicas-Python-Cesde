from data.ListaUsuarios import usuarios
from helpers.crearCSV import crearCSVUsuarios
from helpers.crearHTML import crearTabla
from helpers.crearPDF import crearPDF
import pandas as pd

#Usar la funcion crearSCVUsuarios
crearCSVUsuarios(usuarios, "bdUsuarios.csv")
#creando un dataframe desde una fuente CSV
dataFrameUsuarios = pd.read_csv('data/bdUsuarios.csv')
#convertir el DF en TABLA HTML
crearTabla(dataFrameUsuarios,'usuarios')
#convertir el DF en PDF
crearPDF(dataFrameUsuarios, 'usuarios')

#Se filtran los datos
#filtroUno = dataFrameUsuarios.query("Edad>30")
#print(filtroUno)

print("Cargando filtos de usuarios...")

# Sembradoras (mujeres) mayores de 40 años y su salario esta entre 1 salario a 2 salarios
filtroSembradoras = dataFrameUsuarios.query("(Genero == 'Femenino') and (Edad > 40) and (Salario >= 10003000 or Salario <= 2000600)")
#convertir el DF en TABLA HTML
crearTabla(filtroSembradoras,'usuarios_filtro_1')

# Sembradores menores de 20 años
filtroMenores20 = dataFrameUsuarios.query("Edad < 20")
crearTabla(filtroMenores20,'usuarios_filtro_2')

# Sembradores hombres mayores de 50 años
filtroHombresMenores50 = dataFrameUsuarios.query("(Genero == 'Masculino') and (Edad > 50)")
crearTabla(filtroHombresMenores50,'usuarios_filtro_3')