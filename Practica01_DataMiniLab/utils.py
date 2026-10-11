"""
Módulo: utils.py
Descripción:
Contiene las funciones para gestionar registros de imágenes
(metadatos únicamente) del programa Data Mini Lab.

Incluye:
- Agregar registros
- Buscar registros
- Generar estadísticas
- Eliminar registros
- Listar registros
- Guardar y cargar datos en JSON
"""

import json

# Tupla constante que define los formatos permitidos
FORMATOS_VALIDOS = ("jpg", "png", "bmp", "tiff")

# Variable global que controla la asignación incremental de IDs
# Se actualiza automáticamente al cargar datos desde el archivo
contador_id = 1

def agregar_registros(registros):
    """
    Permite agregar nuevos registros de imágenes.

    Parámetros:
        registros (list): Lista donde se almacenan los registros.

    Retorna:
        list: Lista actualizada con los nuevos registros.
    """
    global contador_id

    while True:
        opcion = input("\nPresiona ENTER para agregar imagen o escribe 'salir' para terminar: ")

        # Permite salir del módulo sin perder datos
        if opcion.lower() == "salir":
            print("Saliendo de agregar registros...")
            break
        try:
            # Captura de datos del usuario
            nombre = str(input("Nombre imagen:"))
            ancho = int(input("Ancho imagen:"))
            alto = int(input("Alto imagen:"))
            canal = int(input("Canales imagen:"))
            formt = str(input("Formato imagen:"))
            
            # --------VALIDACIONES--------

            # Validación de dimensiones positivas
            if ancho <= 0 or alto <=0:
                print("ERROR: ancho y alto deben ser mayor a 0")
                continue

            # Validación de canales permitidos
            if canal not in(1,3,4):
                print("ERROR: canales permitidos 1,3,4")
                continue

            # Validación de formato
            if formt not in FORMATOS_VALIDOS:
                print(f"ERROR: Formato inválido. Formatos permitidos:{FORMATOS_VALIDOS}")
                continue

            # ---------- CREACIÓN DEL REGISTRO ----------

            imagen_info = {"id": contador_id, 
                        "nombre": nombre, 
                        "ancho": ancho, 
                        "alto": alto, 
                        "canales": canal, 
                        "formato": formt}
            

            registros.append(imagen_info)
            print(f"Imagen {nombre} registrada con exito con ID {contador_id}")

            # Incrementa el ID para evitar duplicados
            contador_id += 1

        except ValueError:
            # Manejo de error si el usuario ingresa texto donde se espera número
            print("ERROR: Debes ingresar números donde corresponda.") 
    return registros

def buscar(registros, criterio: str):
    """
    Busca registros por nombre (parcial) o por formato exacto.

    Parámetros:
        registros (list): Lista de registros almacenados.
        criterio (str): Texto de búsqueda.
    """
    if not registros:
        print("No hay registros disponibles.")
        return
    
    criterio = criterio.lower()
    encontrados = []

    # Búsqueda flexible por nombre o coincidencia exacta por formato
    for img in registros:
        if (criterio in img["nombre"].lower() or criterio == img["formato"].lower()):
            encontrados.append(img)
    
    if encontrados:
        print("------RESULTADOS ENCONTRADOS------")
        for img in encontrados:
            print(f"ID: {img['id']:06d}")
            print(f"Nombre: {img['nombre']}")
            print(f"Ancho: {img['ancho']}")
            print(f"Alto: {img['alto']}")
            print(f"Canales: {img['canales']}")
            print(f"Formato: {img['formato']}")
            print("------------------------")

    else:
        print("No se encontraron coincidencias.")      

def calcular_min_max(resoluciones):
    """
    Retorna el valor mínimo y máximo de una lista de resoluciones.
    """
    return (min(resoluciones), max(resoluciones)) 
  
def estadisticas(registros):
    """
    Calcula estadísticas generales:
    - Promedio de resolución
    - Resolución mínima y máxima
    - Conteo por formato
    """
    if not registros:
        print("No hay registros a analizar")
        return {}

    resoluciones = []
    conteo_formatos = {}

    for img in registros:
        # Cálculo de resolución (ancho x alto)
        resolucion = img["ancho"] * img["alto"]
        resoluciones.append(resolucion)

        formato = img["formato"]
         # Conteo dinámico por formato
        if formato in conteo_formatos:
            conteo_formatos[formato] += 1
        else:
            conteo_formatos[formato] = 1
            
    # Calculo del promedio, maximo y minio de resolucion
    promedio = sum(resoluciones) / len(resoluciones)
    minimo, maximo = calcular_min_max(resoluciones)

    print("------ESTADISTICAS------")
    print(f"Promedio resolucion: {promedio}")
    print(f"Resolucion Maxima: {maximo}")
    print(f"Resolucion Minima: {minimo}")

    print("\nConteo por formato:")
    for formato, cantidad in conteo_formatos.items():
        print(f"{formato}: {cantidad}")   

def eliminar(registros):
    """
    Elimina un registro buscando por ID.
    Solicita confirmación antes de eliminar.
    """
    if not registros:
        print("No hay registros para eliminar.")
        return

    try:
        id_buscar = int(input("Ingrese ID de imagen a eliminar: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    for img in registros:
        if img["id"] == id_buscar:
            print("\nSe eliminará el siguiente registro:")
            print(f"ID: {img['id']:06d}")
            print(f"Nombre: {img['nombre']}")
            print(f"Ancho: {img['ancho']}")
            print(f"Alto: {img['alto']}")
            print(f"Canales: {img['canales']}")
            print(f"Formato: {img['formato']}")
            print("-----------------------------------")

            confirmacion = input("¿Confirmar eliminación? (s/n): ").lower()

            if confirmacion == "s":
                registros.remove(img)
                print("Registro eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
            return

    print("No se encontró un registro con ese ID.")

def listar_registros(registros):
    """
    Muestra todos los registros en formato legible.
    """
    if not registros:
        print("No hay registros a listar")
        return
    print("------LISTADO------")
    for img in registros:
        print(f"ID: {img['id']:06d}")
        print(f"Nombre: {img['nombre']}")
        print(f"Ancho: {img['ancho']}")
        print(f"Alto: {img['alto']}")
        print(f"Canales: {img['canales']}")
        print(f"Formato: {img['formato']}")
        print("-----------------------------------")

def guardar_datos(registros):
    """
    Guarda los registros en un archivo JSON.
    """
    with open("registros.json", "w", encoding="utf-8") as archivo:
        json.dump(registros, archivo, indent=4)

def cargar_datos():
    """
    Carga los registros desde el archivo JSON.
    También actualiza el contador_id para evitar IDs duplicados.
    """
    global contador_id
    try:
        with open("registros.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            # Continúa la numeración desde el ID más alto encontrado
            if datos:
                contador_id = max(img["id"] for img in datos) + 1
            else:
                contador_id = 1
            return datos
    except FileNotFoundError:
        # Si el archivo no existe, se inicia una lista vacía
        return []
