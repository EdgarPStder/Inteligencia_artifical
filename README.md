# **Python Essencials: Data_Mini_Lab (CLI)**  

**Asignatura:** Inteligencia Artificial  
**Carrera:** Ingeniero en sistemas computacionales(ISC) 8°  
**Lenguaje:** python 3.14.2

## **Descripcion**

```data_mini_lab.py``` un programa en consola que permita gestionar un conjunto de registros relacionados con imágenes (metadatos), aplicando fundamentos de programación como:

- Variables y tipos de datos.
- Estructuras de control.
- Listas.
- Diccionarios.
- Funciones.
- Modulos.
- Manejo de archivos json.

## **Ambiente Virtual**

### ¿Como crear y activar el ambiente virtual?

### **1. Crear un ambiente virtual**

```bash
python -m venv .venv
```

### **2. Activar entorno**

#### **Windows (PoweShell)**

```bash
.venv\Scripts\activate.ps1
```

#### **Windows (cmd)**

```bash
.venv\Scripts\activate.bat
```

#### **Linux/Mac**

```bash
source .venv/bin/activate
```

### **3. Actualizar PIP**

```bash
python -m pip install --upgrade pip
```

### **4.Ejecutar el programa**

```bash
python data_mini_lab.py
```

## **Instalacion**

### **1. Descarga y Descomprime**

Extraer el proyecto.
Entrar a la carpeta:

```bash
cd 2223520216
```

### **2. Activa entorno**

```bash
cd Scripts\activate
2223520216\Scripts>activate
(2223520216) 2223520216\Scripts>
```

### **3. Instalar dependencias**

Si no hay dependeicas instalalas con este comando.

```bash
pip install -r requirements.txt
```

Esto instala automaticamente todo lo necesario.

### **3. Ejecuta el programa**

```bash
python data_mini_lab.py
```

## **Funcionalidades**

- Agregar registro (con validación de tipos y rangos)
- Listar registros (formato legible).
- Buscar registros por nombre o formato.
- Generar estadísticas: promedio de resolución, máximo/mínimo, conteos por formato.
- Eliminar registro por id.
- Salir.

## **Estructura de registros**

Cada registro se almacena como un diccionario con la siguiente estructura:

```python
{
    "id": int,
    "nombre": str,
    "ancho": int,
    "alto": int,
    "canales": int,
    "formato": str
}
```

## **Explicacion de funciones ```utils.py```**

### **```agregar_registros()```**

- Solicita datos al usuario.
- Valida tipos numericos.
- Genera ID automatico.
- Agrega el registro a la lista.

### **```listar_registros()```**

- Muestra todos los registros en formato legible.
- Si no hay registros, muestra un mensaje informativo

### **```buscar()```**

- Permite buscar por nombre o formato.
- Utiliza operadores booleanos e ```in```

### **```estadisticas()```**

Calcula:

- Promedio de resolucion(ancho x alto).
- Resolucion Maxima.
- Resolucion Minima.
- Conteo por formato.

### **```elimiar()```**

- Solicita ID.
- Confirma antes de eliminar.
- Elimina el regitro si existe.

### **```guardar_datos()```**

Guarda los registros en un archivo JSON.

### **```cargar_datos()```**

Carga los registros desde el archivo JSON.

## **Pruebas y Validacion**

El sismeta fue probado y validado con los siguientes puntos.

- [x] Agregado correcto.
- [x] Persistencia en JSON.
- [x] Busqueda por nombre.
- [x] Busqueda por formato.
- [x] Calculo de estadisticas.
- [x] Eliminacion por ID.

## **Evidencia**

Se incluyen captura de pantalla del programa en ejecucion con:

> ### Registros agregados

![Agregar registro de imagen](imgs\agregar.png)
![Registros guardados](imgs\agregado.png)

> ### Estadisticas generadas
  
![Estadisticas](imgs\estadisticas.png)

> ### Eliminacion confimada

![Eliminar registro](imgs\eliminar.png)
![Registro eliminado](imgs\eliminado.png)
  
## **Conclusion**

Este proyecto consolida los fundamentos de Python orientados a la gestión de datos, preparando la base para futuros trabajos con procesamiento de imágenes y visión artificial.
