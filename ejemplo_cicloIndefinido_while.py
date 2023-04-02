# Ejemplo: 
# Se deben ingresar por teclado las notas de los alumnos en una determinada asignatura, o un 99 si el alumno estuvo ausente.
# Preparar un algoritmo para calcular e imprimir la nota promedio, recordando que el alumno ausente no se promedia.
# El algoritmo debe terminar cuando se ingrese un valor negativo."""

#Se inicia leyendo la primer nota
suma = 0
cantidad = 0
nota = int (input("Ingrese la primer nota "))

while nota >= 0:
    #Si la nota es mayor o igual a 0 y distintas de 99, entonces True, se sigue leyendo 
    if nota != 99:
        suma = suma + nota
        cantidad = cantidad + 1
    nota = int( input("Ingrese la siguiente nota "))
if cantidad > 0:
    #Si la nota es menor a cero, los resultados (Promedio)  
    promedio = suma/cantidad
    print("EL promedio de calificaciones es", round (promedio, 2))
