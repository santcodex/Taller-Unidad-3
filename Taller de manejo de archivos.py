import os
import csv
import json

# Definición de nombres de archivos
archivo_csv = "contactos.csv"
archivo_json = "contactos.json"

# Si el archivo CSV no existe, lo creamos con una cabecera
if not os.path.exists(archivo_csv):
    try:
        with open(archivo_csv, "w", newline="", encoding="utf-8") as fichero_csv:
            escritor = csv.writer(fichero_csv)
            escritor.writerow(["Nombre", "Telefono"])
        print("Se creó el archivo CSV con la cabecera.")
    except Exception as error:
        print("Error al crear el archivo CSV:", error)

# Si el archivo JSON no existe, lo creamos como una lista vacía
if not os.path.exists(archivo_json):
    try:
        with open(archivo_json, "w", encoding="utf-8") as fichero_json:
            json.dump([], fichero_json, indent=4)
        print("Se creó el archivo JSON.")
    except Exception as error:
        print("Error al crear el archivo JSON:", error)

# Saludo e ingreso de datos por el usuario
print("\nBienvenido a tu Agenda de Contactos")
nombre = input("Ingresa el nombre del contacto: ")
telefono = input("Ingresa el teléfono del contacto: ")

# Crear un contacto con los datos ingresados
contacto_nuevo = {
    "Nombre": nombre,
    "Telefono": telefono
}

# Agregar el contacto al archivo CSV (modo 'append')
try:
    with open(archivo_csv, "a", newline="", encoding="utf-8") as fichero_csv:
        escritor = csv.writer(fichero_csv)
        escritor.writerow([nombre, telefono])
    print("\nContacto guardado en el archivo CSV.")
except Exception as error:
    print("Error al escribir en el archivo CSV:", error)

# Agregar el contacto al archivo JSON
try:
    # Se lee la lista actual de contactos del archivo JSON
    with open(archivo_json, "r", encoding="utf-8") as fichero_json:
        lista_contactos = json.load(fichero_json)
    
    # Se añade el nuevo contacto a la lista
    lista_contactos.append(contacto_nuevo)
    
    # Se guarda la lista actualizada en el archivo JSON
    with open(archivo_json, "w", encoding="utf-8") as fichero_json:
        json.dump(lista_contactos, fichero_json, indent=4)
    print("Contacto guardado en el archivo JSON.")
except Exception as error:
    print("Error al escribir en el archivo JSON:", error)

# Mostrar el contenido del archivo CSV
print("\n--- Contenido del archivo CSV ---")
try:
    with open(archivo_csv, "r", newline="", encoding="utf-8") as fichero_csv:
        lector = csv.reader(fichero_csv)
        for fila in lector:
            print(fila)
except Exception as error:
    print("Error al leer el archivo CSV:", error)

# Mostrar el contenido del archivo JSON
print("\n--- Contenido del archivo JSON ---")
try:
    with open(archivo_json, "r", encoding="utf-8") as fichero_json:
        lista_contactos = json.load(fichero_json)
        for contacto in lista_contactos:
            print(contacto)
except Exception as error:
    print("Error al leer el archivo JSON:", error)
