# ======================================================
# SISTEMA DE CALIFICACIONES CON ARREGLOS EN PYTHON
# Autor: reyesluismario22-hub
# Fecha: 10 de octubre de 2026
# ======================================================

# Declaración del arreglo para 10 calificaciones
calificaciones = []

# 1. Ingreso y validación de datos
print("=== INGRESO DE CALIFICACIONES ===")
for i in range(10):
    while True:
        try:
            nota = float(input(f"Ingrese la calificación del estudiante {i+1}: "))
            if 0 <= nota <= 100:
                calificaciones.append(nota)
                break
            else:
                print("⚠️  La calificación debe estar entre 0 y 100. Intente nuevamente.")
        except ValueError:
            print("❌ Entrada inválida. Ingrese un número.")

# 2. Cálculos estadísticos
suma = sum(calificaciones)
promedio = suma / len(calificaciones)
mayor = max(calificaciones)
menor = min(calificaciones)

aprobados = 0
reprobados = 0

for nota in calificaciones:
    if nota >= 70:
        aprobados += 1
    else:
        reprobados += 1

# 3. Aplicar ajuste: +5 puntos a menores de 70 (sin pasar de 100)
calificaciones_actualizadas = []
for nota in calificaciones:
    if nota < 70:
        nueva = nota + 5
        if nueva > 100:
            nueva = 100
        calificaciones_actualizadas.append(nueva)
    else:
        calificaciones_actualizadas.append(nota)

# 4. Mostrar resultados
print("\n" + "="*50)
print("          RESUMEN DE CALIFICACIONES")
print("="*50)
print(f"Calificaciones originales: {calificaciones}")
print(f"Promedio del grupo: {promedio:.2f}")
print(f"Calificación más alta: {mayor}")
print(f"Calificación más baja: {menor}")
print(f"Aprobados: {aprobados}  |  Reprobados: {reprobados}")
print(f"\nCalificaciones actualizadas (+5 a reprobados): {calificaciones_actualizadas}")

# 5. Guardar en archivo
with open("calificaciones.txt", "w", encoding="utf-8") as archivo:
    archivo.write("=== SISTEMA DE CALIFICACIONES ===\n")
    archivo.write(f"Calificaciones originales: {calificaciones}\n")
    archivo.write(f"Promedio: {promedio:.2f}\n")
    archivo.write(f"Mayor: {mayor}\n")
    archivo.write(f"Menor: {menor}\n")
    archivo.write(f"Aprobados: {aprobados}\n")
    archivo.write(f"Reprobados: {reprobados}\n")
    archivo.write(f"Calificaciones actualizadas: {calificaciones_actualizadas}\n")

print("\n✅ Los datos han sido guardados en 'calificaciones.txt'")
