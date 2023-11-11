from data.ListaRefrigerios import refrigerios
from helpers.crearCSV import crearCSVRefrigerios
from helpers.crearHTML import crearTabla
import pandas as pd

crearCSVRefrigerios(refrigerios, "dbRefrigerios.csv")

#creando un dataframe desde una fuente CSV
dataFrameRefrigerios = pd.read_csv('data/dbRefrigerios.csv')
print(dataFrameRefrigerios)

#convertir el DF en TABLA HTML
crearTabla(dataFrameRefrigerios,'refrigerios')