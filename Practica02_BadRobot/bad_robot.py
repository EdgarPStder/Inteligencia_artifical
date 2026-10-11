"""
Programa: bad_roboy.py
Version: 1.0.0
Fecha: 2026-02-25

Descripción:
Programa que dibuja un robot ("Bad Robot") usando figuras geométricas básicas
con la librería OpenCV. Se utilizan rectángulos, círculos, elipses y polígonos
para construir cada parte del robot: cabeza, cuerpo, ojos, nariz, cuello y antena.

Autor: Edgar Gael Pesina Santander
"""
import numpy as np
import cv2

# Crear el lienzo negro de 512x512 píxeles donde vamos a dibujar todo
canvas = np.zeros((512,512,3), dtype="uint8")

# Nombre de la ventana que se va a mostrar
window_name = 'Bad Robot'

# Dibujamos el fondo gris que simula el cielo
cv2.rectangle(canvas, (0, 0), (512,350), (215, 215, 215), -1)

# Dibujamos el césped con triángulos negros en la línea del horizonte
# Definimos la forma base de un triángulo
puntos_cesped = np.array([
    [0, 350], # 1. Esquina inferior izquierda
    [30, 350], # 2. Esquina inferior derecha
    [15, 320] # 3. Punto central inferior
], np.int32)
num_trangulos = 20 # cuántos triángulos vamos a repetir
separacion_trg = 25 # qué tan separados están
for i in range(num_trangulos):
    # Movemos cada triángulo a la derecha según su posición
    tgr_x = i * separacion_trg
    puntos_triangulo = puntos_cesped + [tgr_x, 0]
    puntos_triangulo = puntos_triangulo.reshape((-1, 1, 2))
    cv2.fillPoly(canvas, [puntos_triangulo], (0, 0, 0), cv2.LINE_AA)

# Dibujamos el resorte (antena) encima de la cabeza
# Usamos elipses inclinadas para que parezca una espiral
inicio_x, inicio_y = 256, 190 
num_aros = 5 
separacion_aro = 10 

for i in range(num_aros):
    aro_y = inicio_y - i * separacion_aro # cada aro va un poco más arriba
    cv2.ellipse(canvas, (inicio_x, aro_y), (10,5), 135, 0, 360, (150, 150, 150), 2)

# Dibujamos el casco encima de la cabeza (solo la mitad superior de la elipse)
cv2.ellipse(canvas, (256, 206), (70, 20), 0, 180, 360, (39, 46, 39), -1)

# Dibujamos la cabeza del robot como un rectángulo rojo
cv2.rectangle(canvas, (156, 206), (356, 306), (0, 0, 255), -1)

# Dibujamos los dos ojos en cian, son de diferente tamaño a propósito
cv2.circle(canvas, (190,255), 10, (0,255,255), -1) # ojo izquierdo
cv2.circle(canvas, (320,255), 12, (0,255,255), -1)  # ojo derecho (más grande)

# Dibujamos el cuello como un triángulo que conecta la cabeza con el cuerpo
puntos_cuello = np.array([
    [206,306], # 1. Superior izquierdo del cuello
    [306,306], # 2. Superior derecho del cuello
    [256,400] # 3. Punto inferior del cuello
    ],np.int32) 
cv2.fillPoly(canvas, [puntos_cuello], (39, 46, 39), cv2.LINE_AA)

# Dibujamos el cuerpo como un trapecio (más ancho abajo que arriba)
puntos_cuerpo = np.array([
    [206, 350], # 1. Superior izquierdo
    [306, 350], # 2. Superior derecho
    [350, 450], # 3. Inferior derecho 
    [162, 450] # 4. Inferior izquierdo 
], np.int32)

puntos_cuerpo = puntos_cuerpo.reshape((-1, 1, 2))
cv2.fillPoly(canvas, [puntos_cuerpo], (0, 0, 255), cv2.LINE_AA)

# Dibujamos la nariz como un triángulo sin relleno
puntos_nariz = np.array([
    [256, 245], # 1. Punta superior 
    [246, 265], # 2. Inferior izquierdo 
    [266, 265]  # 3. Inferior derecho 
    ], np.int32)
puntos_nariz = puntos_nariz.reshape((-1, 1, 2))
cv2.polylines(canvas, [puntos_nariz], isClosed=False, color=(0, 0, 0), thickness=2)

# Escribimos el nombre del robot en la parte de abajo
cv2.putText(canvas,'BAD ROBOT',(128,500), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255,255,255), 1, cv2.LINE_AA)

# Mostramos la ventana con el dibujo final
cv2.imshow(window_name, canvas)

# Esperamos a que el usuario presione cualquier tecla para cerrar
cv2.waitKey(0) # 0 significa que eperara indefinidamente
cv2.destroyAllWindows()

if __name__ == "__main__":
    pass