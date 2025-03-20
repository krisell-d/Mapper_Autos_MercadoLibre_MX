
# GPT Personalizado: Mapper de Autos MercadoLibre México

import re

class MapperAutosML:
    def __init__(self):
        self.data = {}

    def procesar_descripcion(self, descripcion_textual, descripcion_visual):
        # Procesar ambas descripciones (texto e imágenes)
        self.data['Descripcion_Textual'] = descripcion_textual
        self.data['Descripcion_Visual'] = descripcion_visual

        # Extraer información básica
        self.data['Marca'] = re.search(r'Toyota|Nissan|Chevrolet|Mazda|Honda|Kia|Hyundai|Ford|Volkswagen', descripcion_textual, re.IGNORECASE)
        self.data['Modelo'] = re.search(r'Corolla|Kicks|Onix|CX-5|Civic|Rio|Elantra|Mustang|Jetta', descripcion_textual, re.IGNORECASE)

        # Mejorar detección de año
        self.data['Año'] = re.search(r'(20[1-3][0-9])', descripcion_textual)

        # Mejorar detección de precio (admite decimales)
        self.data['Precio'] = re.search(r'\$\s?[\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?]+', descripcion_textual)

        # Mejorar detección de transmisión
        self.data['Transmisión'] = re.search(r'manual|automática|CVT|Tiptronic|DCT|Dual Clutch|Automatizada', descripcion_textual, re.IGNORECASE)

        # Mejorar detección de motor, características y seguridad
        self.data['Motor'] = re.search(r'motor\s(V?\d+\.?\d*L|Eléctrico|Híbrido)', descripcion_textual, re.IGNORECASE)
        self.data['Equipamiento'] = re.findall(r'pantalla táctil|cámara de retroceso|asientos de cuero|aire acondicionado|bluetooth', descripcion_textual, re.IGNORECASE)
        self.data['Seguridad'] = re.findall(r'airbags|frenos ABS|control de estabilidad|sensor de proximidad', descripcion_textual, re.IGNORECASE)

    def analizar(self):
        # Formatear la salida
        return {
            'Marca': self.data['Marca'].group(0) if self.data['Marca'] else 'Pendiente',
            'Modelo': self.data['Modelo'].group(0) if self.data['Modelo'] else 'Pendiente',
            'Año': self.data['Año'].group(0) if self.data['Año'] else 'Pendiente',
            'Precio': self.data['Precio'].group(0) if self.data['Precio'] else 'Pendiente',
            'Transmisión': self.data['Transmisión'].group(0) if self.data['Transmisión'] else 'Pendiente',
            'Motor': self.data['Motor'].group(0) if self.data['Motor'] else 'Pendiente',
            'Equipamiento': ', '.join(self.data['Equipamiento']) if self.data['Equipamiento'] else 'Pendiente',
            'Seguridad': ', '.join(self.data['Seguridad']) if self.data['Seguridad'] else 'Pendiente',
            'Procedencia': 'MercadoLibre México',
            'Descripción Visual': self.data['Descripcion_Visual'] or 'No proporcionada'
        }


# Ejemplo de uso del GPT personalizado
mapper = MapperAutosML()

# Procesar descripciones
mapper.procesar_descripcion(
    descripcion_textual="Ford Mustang 2022, motor V8 de 5.0L, transmisión manual Tiptronic. Precio: $1,100,000.50 MXN. Pantalla táctil, asientos de cuero, frenos ABS, airbags.",
    descripcion_visual="Auto deportivo color rojo, con llantas deportivas y techo descapotable."
)

mapper.procesar_descripcion(
    descripcion_textual="Toyota Corolla 2023, motor 1.8L Híbrido, transmisión automática CVT. Precio: $450,000.00 MXN. Cámara de retroceso, aire acondicionado, airbags, control de estabilidad.",
    descripcion_visual="Auto sedán color blanco, con faros LED y llantas deportivas."
)

mapper.procesar_descripcion(
    descripcion_textual="Nissan Kicks 2022, motor 1.6L, transmisión manual. Precio: $380,000.00 MXN. Bluetooth, asientos de cuero, frenos ABS, airbags.",
    descripcion_visual="SUV color gris con barras en el techo y rines de aluminio."
)

# Generar resultado
resultado = mapper.analizar()
print(resultado)
