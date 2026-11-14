import math
AlCa = {}
AL = "José"
while True:
     CA = float(input("¿Cuál es la calificación redondeada del estudiante? "))
     if CA < 0 or math.isinf(CA) or math.isnan(CA):
      print("Opción inválida, intenta de nuevo.")
      print("")
     else:
      AlCa[AL] = CA
      print(f"-> ¡Se agregó la calificación de {AL} correctamente!")
      print("")