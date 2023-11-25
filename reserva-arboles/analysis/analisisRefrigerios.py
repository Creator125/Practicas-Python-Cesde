from data.ListaRefrigerios import refrigerios
from helpers.crearCSV import crearCSVRefrigerios
from helpers.crearHTML import crearTabla
from helpers.crearPDF import crearPDF
import pandas as pd

crearCSVRefrigerios(refrigerios, 'dbRefrigerios.csv')

#creando un dataframe desde una fuente CSV
dataFrameRefrigerios = pd.read_csv('data/dbRefrigerios.csv')

#convertir el DF en TABLA HTML
crearTabla(dataFrameRefrigerios,'refrigerios')

#convertir el DF en PDF
crearPDF(dataFrameRefrigerios, 'refrigerios')

#Realizando filtros
print(" ")
print("-------------- Filtro de Refrigerios --------------")
print(" ")

print("Refrigerios cuyo valor unitario sea mayor a 20.000")
filtroPrecioMayor = dataFrameRefrigerios.query("Precio > 20000")
print(filtroPrecioMayor)

print(" ")

print("Cantidades de refrigerios menores a 1000")
filtroCantidad = dataFrameRefrigerios.query("Cantidad < 1000")
print(filtroCantidad)