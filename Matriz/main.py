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

