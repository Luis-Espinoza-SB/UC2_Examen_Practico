import MAGIC2
import math

def registrar_estudiante(AlCa, LiEs):
  while True:
    ID = int(input("¿Cuál es el número de identificación? "))
    if ID >= 0 and not (math.isinf(ID) or math.isnan(ID)):
      break
    print("Opción inválida, intenta de nuevo.\n")

  while True:
    AL = input("¿Cuál es el nombre del alumno? ").strip().upper()
    if not AL:
      print("Inténtelo de nuevo, hubo un error.\n")
    else:
      break

  CA = MAGIC2.PeNo(1)
  Ca = MAGIC2.PeNo(2)
  ca = MAGIC2.PeNo(3)
  CaTu = (CA, Ca, ca)

  P = MAGIC2.calcular_promedio(CA, Ca, ca)

  es_apro = P >= 70
  if es_apro:
    N = "Aprobado"
  else:
    N = "Reprobado"

  AlCa[AL] = {
      "ID": ID,
      "Calificaciones": CaTu,
      "Promedio": P,
      "Situación Académica": N,
  }

  if AL not in LiEs:
    LiEs.append(AL)

  print(f"-> ¡Se agregaron los datos de {AL} al sistema correctamente!\n")

def mostrar_estudiantes(AlCa, LiEs):
  if not LiEs:
    print("-> No hay alumnos registrados todavía.\n")
  else:
    print("\n--- LISTA DE ALUMNOS Y NOTAS ---")
    for alumn in sorted(LiEs):
      datos = AlCa[alumn]
      print(
          f"- {alumn} -> Notas: {datos['Calificaciones']} | Promedio:"
          f" {datos['Promedio']:.2f} ({datos['Situación Académica']})"
      )
    print("")

def consultar_estudiante(AlCa):
  Alum = input("¿Qué alumno quieres buscar?: ").upper()
  if Alum in AlCa:
    print(f"\n-> ID: {AlCa[Alum]['ID']}")
    n1, n2, n3 = AlCa[Alum]["Calificaciones"]
    print(f"-> Nota 1: {n1}")
    print(f"-> Nota 2: {n2}")
    print(f"-> Nota 3: {n3}")
    print(f"-> Promedio: {AlCa[Alum]['Promedio']:.2f}")
    print(f"-> Situación: {AlCa[Alum]['Situación Académica']}\n")
  else:
    print("-> No se ha encontrado registro.\n")

def eliminar_estudiante(AlCa, LiEs):
  if not AlCa:
    print("-> No hay alumnos registrados para eliminar.\n")
    return

  while True:
    id_busc = int(
        input("Ingrese el número de identificación del estudiante a eliminar: ")
    )
    if id_busc >= 0 and not (math.isinf(id_busc) or math.isnan(id_busc)):
      break
    print("Opción inválida, intenta de nuevo.\n")

  AlEl = None
  for alumn, datos in AlCa.items():
    if datos["ID"] == id_busc:
      AlEl = alumn
      break

  if AlEl:
    del AlCa[AlEl]
    LiEs.remove(AlEl)
    print(
        f"-> El estudiante {AlEl} con ID {id_busc} ha sido"
        " eliminado correctamente.\n"
    )
  else:
    print(
        "-> No se encontró ningún estudiante registrado con ese número de"
        " identificación.\n"
    )

def mostrar_estadisticas(AlCa):
  if not AlCa:
    print("-> No hay alumnos registrados todavía para mostrar estadísticas.\n")
  else:
    ToEs = len(AlCa)
    SuPr = 0
    Apro = 0
    Repr = 0
    PMA = -1
    MeAl = ""

    for alumn, datos in AlCa.items():
      PrAc = datos["Promedio"]
      SuPr += PrAc  # Este es el acumulador de promedios

      if datos["Situación Académica"] == "Aprobado":
        Apro += 1  # acumulador / contador de aprobados
      else:
        Repr += 1  # acumulador / contador de reprobados

      if PrAc > PMA:
        PMA = PrAc
        MeAl = alumn

    PrGe = SuPr / ToEs

    print("\n--- ESTADÍSTICAS GENERALES ---")
    print(f"-> Cantidad total de estudiantes: {ToEs}")
    print(f"-> Promedio general del grupo: {PrGe:.2f}")
    print(f"-> Estudiantes aprobados: {Apro}")
    print(f"-> Estudiantes reprobados: {Repr}")
    print(f"-> Promedio más alto: {PMA:.2f} (Alumno: {MeAl})\n") # (Si se que es.2f)