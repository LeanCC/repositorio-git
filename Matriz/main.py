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

"""
Crear función para buscar la secuencia de números de manera vertical

"""

def consecutive_vert():
  if row1[0] == 1 and row2[0] == 2 and row3[0] == 3 and row4[0] == 4:
    print('Posicion Incial: Fila 1,Elemento 1.\n'
          'Posicion Final: Fila 4,Elemento 1\n') 
  
  elif row1[1] == 1 and row2[1] == 2 and row3[1] == 3 and row4[1] == 4:
    print('Posicion Incial: Fila 1,Elemento 2.\n'
          'Posicion Final: Fila 4,Elemento 2\n') 

  elif row1[2] == 1 and row2[2] == 2 and row3[2] == 3 and row4[2] == 4:
    print('Posicion Incial: Fila 1,Elemento 3.\n'
          'Posicion Final: Fila 4,Elemento 3\n') 
  elif row1[3] == 1 and row2[3] == 2 and row3[3] == 3 and row4[3] == 4:
    print('Posicion Incial: Fila 1,Elemento 4.\n'
          'Posicion Final: Fila 4,Elemento 4\n') 

  elif row1[4] == 1 and row2[4] == 2 and row3[4] == 3 and row4[4] == 4:
    print('Posicion Incial: Fila 1,Elemento 5.\n'
          'Posicion Final: Fila 4,Elemento 5\n')
  

""" Ejecutamos la función"""

consecutive_vert()


