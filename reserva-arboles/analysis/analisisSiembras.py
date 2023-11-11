from data.ListaSiembras import siembras
from helpers.crearCSV import crearCSVSiembras
from helpers.crearHTML import crearTabla
import pandas as pd

#Usar la funcion crearSCVUsuarios
crearCSVSiembras(siembras, "bdSiembras.csv")

#creando un dataframe desde una fuente CSV
dataFrameSiembras = pd.read_csv('data/bdSiembras.csv')
print(dataFrameSiembras)

#convertir el DF en TABLA HTML
crearTabla(dataFrameSiembras,'siembras')