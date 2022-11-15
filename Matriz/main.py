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


"""
Crear función para buscar la secuencia de números de manera horizontal

"""

def consecutive_horizont():
  if row1[0] == 1 and row1[1] == 2 and row1[2] == 3 and row1[3] == 4:
    print('Posicion Incial: Fila 1,Elemento 1.\n'
          'Posicion Final: Fila 1,Elemento 4\n') 

  elif row2[0] == 1 and row2[1] == 2 and row2[2] == 3 and row2[3] == 4:
    print('Posicion Incial: Fila 2,Elemento 1.\n'
          'Posicion Final: Fila 2,Elemento 4\n') 

  elif row3[0] == 1 and row3[1] == 2 and row3[2] == 3 and row3[3] == 4:
    print('Posicion Incial: Fila 3,Elemento 1.\n'
          'Posicion Final: Fila 3,Elemento 4\n') 

  elif row4[0] == 1 and row4[1] == 2 and row4[2] == 3 and row4[3] == 4:
    print('Posicion Incial: Fila 4,Elemento 1.\n'
          'Posicion Final: Fila 4,Elemento 4\n') 

  elif row5[0] == 1 and row5[1] == 2 and row5[2] == 3 and row5[3] == 4:
    print('Posicion Incial: Fila 5,Elemento 1.\n'
          'Posicion Final: Fila 5,Elemento 4\n') 

""" Ejecutamos la función"""

consecutive_horizont()

