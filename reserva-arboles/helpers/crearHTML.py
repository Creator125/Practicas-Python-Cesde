import pandas as pd
from bs4 import BeautifulSoup
def crearTabla(dataframe,nombre):

    archivoHTML=dataframe.to_html()
    rutaArchivo=f"tables/{nombre}.html"

    encabezado=''' 
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="UTF-8">
                    <title>Tablas</title>
                    <link rel="stylesheet" href="../assets/styles/bootstrap.css">
                </head>
            </html>
        '''
    
    sopa=BeautifulSoup(archivoHTML,'html.parser')

    for tr in sopa.find_all('tr'):
        tr.attrs.pop('style',None)

    archivoHTML = str(sopa) 
    archivoHTML = archivoHTML.replace('<table border="1" class="dataframe">','<table class="table table-striped">')

    with open(rutaArchivo,"w") as archivo:
        archivo.write(f"{encabezado}\n{archivoHTML}\n</body>\n</html>")