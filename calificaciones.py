# ==============================================
# Sistema de Calificaciones con Arreglos
# ==============================================

# 1. Crear el vector con al menos 5 elementos
calificaciones = [85, 67, 92, 74, 58]
print("=== SISTEMA DE CALIFICACIONES ===")
print("Calificaciones iniciales:", calificaciones)

# 2. Mostrar una calificación por índice
print("\nCalificación en posición 2:", calificaciones[2])

# 3. Recorrer todo el arreglo con un ciclo
print("\nLista completa de calificaciones:")
for nota in calificaciones:
    print("-", nota)

# 4. Cálculos: promedio, mayor, menor
promedio = sum(calificaciones) / len(calificaciones)
mayor = max(calificaciones)
menor = min(calificaciones)

print(f"\nPromedio: {promedio:.2f}")
print("Calificación más alta:", mayor)
print("Calificación más baja:", menor)

# 5. Contar aprobados y reprobados con condición if
aprobados = 0
reprobados = 0
for nota in calificaciones:
    if nota >= 70:
        aprobados += 1
    else:
        reprobados += 1

print("\nEstudiantes aprobados:", aprobados)
print("Estudiantes reprobados:", reprobados)

# 6. Modificar un elemento
calificaciones[1] = 79
print("\nCalificaciones después de modificar la posición 1:")
print(calificaciones)