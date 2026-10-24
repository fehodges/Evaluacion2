import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"
key = "API-KEY"  # Reemplazar con tu clave API de Graphhopper

# MEJORA: palabras para salir del programa
salir = ["s", "salir"]

def geocoding (location, key):
    while location == "":
        location = input("Ingrese la ubicación nuevamente: ")  # MEJORA: traducido
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    # MEJORA: locale=es para que los nombres de lugares vengan en español
    url = geocode_url + urllib.parse.urlencode({"q":location, "limit": "1", "locale": "es", "key":key})

    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    # MEJORA: además se valida que la búsqueda haya entregado resultados
    if json_status == 200 and len(json_data["hits"]) != 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]

        if "country" in json_data["hits"][0]:
            country = json_data["hits"][0]["country"]
        else:
            country=""

        if "state" in json_data["hits"][0]:
            state = json_data["hits"][0]["state"]
        else:
            state=""

        if len(state) !=0 and len(country) !=0:
            new_loc = name + ", " + state + ", " + country
        elif len(country) !=0:
            new_loc = name + ", " + country
        else:
            new_loc = name

        # MEJORA: traducido al español
        print("URL de la API de Geocodificación para " + new_loc + " (Tipo de ubicación: " + value + ")\n" + url)
    else:
        lat="null"
        lng="null"
        new_loc=location
        # MEJORA: mensajes de error en español
        if json_status != 200:
            print("Estado de la API de Geocodificación: " + str(json_status) + "\nMensaje de error: " + json_data["message"])
        else:
            print("No se encontraron resultados para: " + location)
        json_status = 404 if json_status == 200 else json_status
    return json_status,lat,lng,new_loc

print("Bienvenido al planificador de rutas. Escriba 's' o 'salir' para terminar.")

while True:
    loc1 = input("Ubicación de origen: ")  # MEJORA: traducido
    if loc1.strip().lower() in salir:      # MEJORA: salir con "s" o "salir"
        break
    orig = geocoding(loc1, key)

    loc2 = input("Destino: ")              # MEJORA: traducido
    if loc2.strip().lower() in salir:      # MEJORA: salir con "s" o "salir"
        break
    dest = geocoding(loc2, key)

    print("=================================================")
    if orig[0] == 200 and dest[0] == 200:
        op="&point="+str(orig[1])+"%2C"+str(orig[2])
        dp="&point="+str(dest[1])+"%2C"+str(dest[2])
        # MEJORA: locale=es para que la narrativa del viaje venga en español
        paths_url = route_url + urllib.parse.urlencode({"key":key, "locale":"es"}) + op + dp
        paths_status = requests.get(paths_url).status_code
        paths_data = requests.get(paths_url).json()
        print("Estado de la API de Rutas: " + str(paths_status) + "\nURL de la API de Rutas:\n" + paths_url)

        print("=================================================")
        print("Indicaciones desde " + orig[3] + " hasta " + dest[3])
        print("=================================================")
        if paths_status == 200:
            miles = (paths_data["paths"][0]["distance"])/1000/1.61
            km = (paths_data["paths"][0]["distance"])/1000
            minutos_totales = paths_data["paths"][0]["time"]/1000/60
            sec = int(paths_data["paths"][0]["time"]/1000%60)
            min = int(paths_data["paths"][0]["time"]/1000/60%60)
            hr = int(paths_data["paths"][0]["time"]/1000/60/60)
            # MEJORA: traducido y con máximo dos decimales
            print("Distancia recorrida: {0:.2f} millas / {1:.2f} km".format(miles, km))
            print("Duración del viaje: {0:02d}:{1:02d}:{2:02d} ({3:.2f} minutos)".format(hr, min, sec, minutos_totales))
            print("=================================================")
            print("Narrativa del viaje:")
            for each in range(len(paths_data["paths"][0]["instructions"])):
                path = paths_data["paths"][0]["instructions"][each]["text"]
                distance = paths_data["paths"][0]["instructions"][each]["distance"]
                # MEJORA: dos decimales
                print("{0} ( {1:.2f} km / {2:.2f} millas )".format(path, distance/1000, distance/1000/1.61))
            print("=============================================")
        else:
            # MEJORA: mensaje de error de la API de rutas en español
            print("Mensaje de error: " + paths_data["message"])
            print("*************************************************")
    else:
        print("No se pudo calcular la ruta. Revise las ubicaciones ingresadas.")
        print("*************************************************")

print("Programa finalizado. ¡Hasta luego!")
