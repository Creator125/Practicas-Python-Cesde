from data.ListaSiembras import siembras
from helpers.crearCSV import crearCSVSiembras
from helpers.crearHTML import crearTabla
from helpers.crearPDF import crearPDF
import pandas as pd

#Usar la funcion crearSCVUsuarios
crearCSVSiembras(siembras, "bdSiembras.csv")

#creando un dataframe desde una fuente CSV
dataFrameSiembras = pd.read_csv('data/bdSiembras.csv')

#convertir el DF en TABLA HTML
crearTabla(dataFrameSiembras,'siembras')

#convertir el DF en PDF
crearPDF(dataFrameSiembras, 'siembras')

#Creando filtros
print(" ")
print("-------------- Filtro de Siembras --------------")
print(" ")

print("Municipios que tenga más de 90 arboles")
filtroCantidadMayor = dataFrameSiembras.query("Cantidad > 90")
print(filtroCantidadMayor)

print(" ")

print("Municipios cuyo tipo de arbol es ceiba")
filtroCeibas = dataFrameSiembras.query("Tipo_arbol == 'Ceibas'")
print(filtroCeibas)

print(" ")

print("Municipios con menos de 10 siembras")
filtroSiembrasMenores = dataFrameSiembras.query("Numero_siembras < 10")
print(filtroSiembrasMenores)