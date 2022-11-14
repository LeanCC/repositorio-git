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
