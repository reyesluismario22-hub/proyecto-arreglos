# Sistema de Calificaciones con Arreglos en Python

Proyecto desarrollado por: **reyesluismario22-hub**
Fecha: 10 de octubre de 2026

## Descripción
Programa que utiliza **arreglos (listas unidimensionales)** para gestionar, calcular y actualizar las calificaciones de 10 estudiantes. Realiza operaciones estadísticas y guarda los resultados en un archivo de texto.

## Objetivos
- Aplicar el uso de arreglos para almacenar datos
- Calcular promedio, nota mayor y nota menor
- Contar aprobados y reprobados
- Actualizar calificaciones con estímulo de +5 puntos
- Guardar información en archivo externo

## Estructura de Archivos
| Archivo | Descripción |
|---|---|
| calificaciones.py | Código fuente del programa |
| README.md.txt | Documentación del proyecto |
| calificaciones.txt | Archivo generado con resultados |

## Funcionalidades
1. **Ingreso de datos**: Solicita 10 calificaciones con validación (0–100)
2. **Cálculos**:
   - Promedio general del grupo
   - Calificación más alta y más baja
   - Cantidad de aprobados (≥70) y reprobados (<70)
3. **Actualización**: Suma 5 puntos a notas menores de 70, sin exceder 100
4. **Almacenamiento**: Guarda todos los resultados en `calificaciones.txt`

## Ejecución
```bash
python calificaciones.py
