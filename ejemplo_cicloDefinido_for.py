#Actividad:
# Se requiere ingresar las notas de 10 alumnos y calcular su promedio.

#Inicio de contadores
suma = 0
cantidad = 10

for x in range(cantidad):
    # Se ingresan las notas con range (Secuencia de número), TRUE, se sigue leyendo
    nota = input("Ingrese la nota del alumno: ")
    suma += int(nota)
promedio = suma/cantidad

print("EL promedio de calificaciones es", promedio)
