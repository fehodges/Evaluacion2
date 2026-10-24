# Evaluacion2 – Software de Geolocalización (Graphhopper)

Proyecto desarrollado para **API Ltda.** en el marco del proyecto con la Biblioteca Nacional
(asignatura CUY6142). Es una aplicación de consola en Python que consume las APIs REST de
**Graphhopper** (Geocoding y Routing) para calcular rutas entre dos ubicaciones y entregar
al visitante la distancia, la duración y la narrativa del viaje paso a paso, todo en español.

## Funcionalidades

- Textos de interacción con el usuario en español.
- Distancias y tiempos mostrados con un máximo de dos decimales.
- Narrativa del viaje (instrucciones paso a paso) en español (`locale=es`).
- Salida del programa ingresando `s` o `salir`.
- Manejo de errores: ubicación vacía, ubicación no encontrada, clave API inválida y rutas imposibles.

## Requisitos

- Python 3
- Librería `requests`
- Una clave API de Graphhopper (https://www.graphhopper.com/)

## Instrucciones de ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/<tu-usuario>/Evaluacion2.git
   cd Evaluacion2
   ```
2. Instalar la dependencia (si no está instalada):
   ```bash
   pip3 install requests
   ```
3. Abrir `EP2_SCRIPT_GEOLOC.py` y reemplazar `API-KEY` por tu clave de Graphhopper.
4. Ejecutar el script:
   ```bash
   python3 EP2_SCRIPT_GEOLOC.py
   ```
5. Ingresar la ubicación de origen y el destino
   (por ejemplo: `Santiago, Chile` y `Valparaíso, Chile`).
6. Para terminar, escribir `s` o `salir`.
