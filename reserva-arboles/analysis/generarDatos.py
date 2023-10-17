import random

municipio = ["Cáceres", "Caucasia", "El Bagre", "Nechí", "Tarazá", "Zaragoza", "Caracolí", "Maceo",
            "Puerto Berrío", "Puerto Nare", "Puerto Triunfo","Yondó","Amalfi","Anorí", "Cisneros", 
            "Remedios", "San Roque", "Santo Domingo", "Segovia", "Vegachí", "Yalí", "Yolombó", 
            "Angostura", "Belmira", "Briceño", "Campamento", "Carolina del Príncipe", 
            "Donmatías", "Entrerríos", "Gómez Plata", "Guadalupe", "Ituango", "San Andrés de Cuerquia", 
            "San José de la Montaña", "San Pedro de los Milagros", "Santa Rosa de Osos", "Toledo", 
            "Valdivia", "Yarumal", "Abriaquí", "Santa Fe de Antioquia", "Anzá", "Armenia", "Buriticá", 
            "Caicedo", "Cañasgordas", "Dabeiba", "Ebéjico", "Frontino", "Giraldo", "Heliconia", "Liborina", 
            "Olaya", "Peque", "Sabanalarga", "San Jerónimo", "Sopetrán", "Uramita", "Abejorral", "Alejandría",
            "Argelia", "El Carmen de Viboral", "Cocorná", "Concepción", "El Peñol", "El Retiro", "El Santuario",
            "Granada", "Guarne", "Guatapé", "La Ceja", "La Unión", "Marinilla", "Nariño", "Rionegro", "San Carlos",
            "San Francisco", "San Luis", "San Rafael", "San Vicente", "Sonsón", "Amagá", "Andes", "Angelópolis", 
            "Betania", "Betulia", "Caramanta", "Ciudad Bolívar", "Concordia", "Fredonia", "Hispania", "Jardín", 
            "Jericó", "La Pintada", "Montebello", "Pueblorrico", "Salgar", "Santa Bárbara", "Támesis", "Tarso", 
            "Titiribí", "Urrao", "Valparaíso", "Venecia", "Apartadó", "Arboletes", "Carepa", "Chigorodó", "Murindó", 
            "Mutatá", "Necoclí", "San Juan de Urabá", "San Pedro de Urabá", "Turbo", "Vigía del Fuerte", "Barbosa", 
            "Bello", "Caldas", "Copacabana", "Envigado", "Girardota", "Itagüí", "La Estrella", "Medellín", "Sabaneta"]

tipoArboles = ["Cedro americano", "Cocotero", "Mango", "Caimito", "Heno",
                "Arbol de zope", "Arbol Pulpo", "Capulin", "Higuera", "Ceiba", 
                "Papaya", "Aguacate", "Cedro", "Framboyán", "Arbol del pan", 
                "Palma canaria", "Jagua", "Yaca", "Marañón", "Samán", 
                "Chocho", "Ébano", "Acacia amarilla", "Acacias Roja", 
                "Guayabillo", "Caobas", "Yarumo", "Cámbulo", "Caracolí",
                "Casco de vaca", "Búcaro", "Guayacán amarillo", "Balso"]

cantidad = int(input("Ingrese alcantidad de datos a ingresar: "))
i = 1

while i <= cantidad:
    diccionario = "{" + f"\"id\":{i}, \"municipio\":\"{municipio[random.randint(1, 124)]}\", \"tipo\":\"{tipoArboles[random.randint(1, 23)]}\", \"cantidad\":{random.randint(1, 500000)}" + "}"
    
    if cantidad > 1:
        print(diccionario + ",")
    else:
        print(diccionario)
    
    i += 1