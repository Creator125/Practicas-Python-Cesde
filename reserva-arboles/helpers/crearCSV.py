import csv

def crearCSVUsuarios(lista,nombreArchivo):
    with open('data/'+nombreArchivo,mode='w',newline='',encoding='utf-8')as archivoCSV:
        writer=csv.writer(archivoCSV)
        writer.writerow(['Nombre','Contraseña','Edad', 'Salario', 'Genero'])
        writer.writerows(lista)

def crearCSVRefrigerios(lista, nombreArchivo):
    with open('data/' + nombreArchivo, mode='w', newline='', encoding='utf-8') as archivoCSV:
        writer = csv.writer(archivoCSV)
        writer.writerow(['Tipo', 'Nombre', 'Precio', 'Cantidad'])
        for refrigerio in lista:
            writer.writerow(refrigerio)

        
        
def crearCSVSiembras(lista, nombreArchivo):
    with open("data/" + nombreArchivo, mode="w", newline="", encoding="utf-8") as archivoCSV:
        writer = csv.writer(archivoCSV)
        writer.writerow(["Alcadía", "Tipo_arbol", "Cantidad", "Presupuesto", "Numero_siembras"])
        for siembra in lista:
            writer.writerow(siembra)