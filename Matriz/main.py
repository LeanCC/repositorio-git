""" Importar modulo random para generar números aleatorios """
import random


""" Creando la matriz """
def creating_mtz(n):
  matriz = []

  for r in range(n):
    row = []

    for c in range(n):
      row.append(random.randint(1,5))

    matriz.append(row)

  return matriz

result = creating_mtz(5)

""" Mostrar la matriz(En linea) """
print(result)
print()

""" Separar por lineas """
row1 = result[0]
row2 = result[1]
row3 = result[2]
row4 = result[3]
row5 = result[4]


""" Mostrar la matriz en un formato 5x5"""
for i in result:
  print(i)

print()

