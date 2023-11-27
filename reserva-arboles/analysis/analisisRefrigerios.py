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
print("Cargando filtro de Refrigerios")

#print("Refrigerios cuyo valor unitario sea mayor a 20.000")
filtroPrecioMayor = dataFrameRefrigerios.query("Precio > 20000")
crearTabla(filtroPrecioMayor,'refrigerios_filtro_1')

#print("Cantidades de refrigerios menores a 1000")
filtroCantidad = dataFrameRefrigerios.query("Cantidad < 1000")
crearTabla(filtroCantidad,'refrigerios_filtro_2')