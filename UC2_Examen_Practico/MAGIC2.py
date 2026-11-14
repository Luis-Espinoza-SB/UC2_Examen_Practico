def mostrar_menu():
  print("------------------ MENÚ ------------------")
  print("1. Registrar estudiante")
  print("2. Mostrar alumnos matriculados registrados")
  print("3. Consultar promedio de un alumno")
  print("4. Mostrar estadísticas generales del grupo")
  print("5. Eliminar estudiante por ID")
  print("6. Salir")
  print("------------------------------------------")
  print("")
  return input("Elige una opción [1], [2], [3], [4], [5] o [6]: ")

def calcular_promedio(nota1, nota2, nota3):
  return (nota1 + nota2 + nota3) / 3

# FUNCIÓN NATURAL MÁS NO ASIGNADA, NO SOY IA POR CIERTO

def PeNo(Num):
  while True:
    nota = int(input(f"¿Cuál es la calificación número {Num}? "))
    if 0 <= nota <= 100:
      return nota
    else:
      print("Opción inválida (debe ser entre 0 y 100), intenta de nuevo.\n")