import MAGIC
import MAGIC2

AlCa = {}
LiEs = []

while True:
  opc = MAGIC2.mostrar_menu()
  print("")

  if opc == "1":
    MAGIC.registrar_estudiante(AlCa, LiEs)
  elif opc == "2":
    MAGIC.mostrar_estudiantes(AlCa, LiEs)
  elif opc == "3":
    MAGIC.consultar_estudiante(AlCa)
  elif opc == "4":
    MAGIC.mostrar_estadisticas(AlCa)
  elif opc == "5":
    MAGIC.eliminar_estudiante(AlCa, LiEs)
  elif opc == "6":
    print("¡Eso es to… eso es to… eso es todo, amigos!")
    break
  else:
    print("Opción inválida, intenta de nuevo.\n")