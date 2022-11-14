""" Importar modulo random para generar numeros aleatorios """
import random


def random_list():
  """ Definir lista e indice"""
  list = []
  i = 1

  """ Agregar los valores al diccionario y por ultimo a la lista """
  while i <= 10:
    dictionary = {}
    id = i 
    edad = random.randint(1,100)
    dictionary['id'] = id
    dictionary['edad'] = edad
    list.append(dictionary)
    i += 1

  return list

list_to_order = random_list()
print(f'Lista:{list_to_order}\n')

""" Importar modulo doctest para realizar testeos"""
if __name__ == "__main__":
  import doctest
  doctest.testmod

"""   
Función en donde se va a retornar
la lista de mayor a menor
"""

def order_by_age():
  """ Ordenamos la lista"""
  ordered = sorted(list_to_order, key=lambda e: e['edad'],reverse=True)

  """ Seleccionamos la persona mas joven y la mas vieja"""
  younger_person = ordered[-1]['id']
  elder_person = ordered[0]['id']

  """ Hacemos un print de sus id """
  print(f'El id de la persona mas joven es: {younger_person}\n'
  f'El id de la persona mas vieja es: {elder_person}\n')

  """ Print de la lista ordenada"""
  print(f'La lista ordenada de mayor a menor edad es: {ordered}')

order_by_age()
 
