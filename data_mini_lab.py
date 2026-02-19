"""
Programa: data_mini_lab.py
Version: 1.0.0
Fecha: 2026-02-18

Descripción:
Sistema de gestión de metadatos de imágenes.
Permite agregar, listar, buscar, generar estadísticas y eliminar registros.

Autor: Edgar Gael Pesina Santander
"""
import utils  # Importamos el módulo que contiene las funciones auxiliares

# Cargamos los registros guardados desde archivo (si existen)
registros_imagenes = utils.cargar_datos()


def menu():
    """
    Muestra el menú principal del sistema y controla
    el flujo de ejecución según la opción elegida.
    """
    while True:
        print("----------MENÚ PRINCIPAL----------")
        print("1.- Agregar registros")
        print("2.- Listar registros")
        print("3.- Buscar de registros")
        print("4.- Estadisticas registros")
        print("5.- Eliminar de registros")
        print("6.- Salir")

        # Capturar opción del usuario
        opcion = input("Seleccione una opcion:")

        # Opción 1: Agregar registro
        if opcion == "1":
            utils.agregar_registros(registros_imagenes)
            utils.guardar_datos(registros_imagenes) # Guardamos cambios

        # Opción 2: Listar registros
        elif opcion == "2":
            utils.listar_registros(registros_imagenes)
        
        # Opción 3: Buscar registros
        elif opcion == "3":
            criterio = input("Criterio (nombre o formato): ")
            utils.buscar(registros_imagenes,criterio)
        
        # Opción 4: Mostrar estadísticas
        elif opcion == "4":
            utils.estadisticas(registros_imagenes)
        
        # Opción 5: Eliminar registro
        elif opcion == "5":
            utils.eliminar(registros_imagenes)
            utils.guardar_datos(registros_imagenes) # Guardamos cambios
        
         # Opción 6: Salir del programa
        elif opcion == "6":
            print("Saliendo del programa...")
            break

         # Manejo de error
        else:
            print("ERROR: Opcion invalida")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()