""" Importar modulo random para generar números aleatorios """
import random


""" Definir la medida de la matriz"""
rows = 5
columns = 5

n = [[random.randint(1,5) for i in range(rows)] for j in range(columns)]


""" Creando la matriz """

def matriz():
  for f in range(rows):
    for c in range(columns):
      print(n[f][c],end=' ')
    print()

matriz()