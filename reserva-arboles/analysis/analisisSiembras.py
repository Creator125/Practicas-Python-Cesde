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
print("Cargando filtro de Siembras")

# Municipios que tenga más de 90 arboles
filtroCantidadMayor = dataFrameSiembras.query("Cantidad > 90")
#convertir el DF en TABLA HTML
crearTabla(filtroCantidadMayor,'siembras_filtro_1')

# Municipios cuyo tipo de arbol es ceiba
filtroCeibas = dataFrameSiembras.query("Tipo_arbol == 'Ceibas'")
crearTabla(filtroCeibas,'siembras_filtro_2')

# Municipios con menos de 10 siembras
filtroSiembrasMenores = dataFrameSiembras.query("Numero_siembras < 10")
crearTabla(filtroSiembrasMenores,'siembras_filtro_3')