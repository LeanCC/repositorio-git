""" Importamos math para usar PI """
import math

PI = math.pi

""" Creamos la clase """

if __name__ == "__main__":

  class Circulo:
    def __init__(self,nombre,radio,diametro) -> None:
      self.nombre = nombre
      self.radio = radio
      self.diametro = diametro

    """ Métodos """
    def calc_area(self):
      try:
        if self.radio <= 0:
          raise Exception('ERROR')
        return (self.radio**2)*PI
      except Exception:
        print('ERROR EL VALOR DEL RADIO DEL CIRCULO NO PUEDE SER IGUAL O MENOR A 0')


    def calc_perimetro(self):
      return self.diametro*PI

    def __str__(self) -> str:
      return (f'{self.nombre}' + f' es un circulo con un radio de: {self.radio}, y un diametro de: {self.diametro}')


""" Pedir el valor del radio y diametro del circulo"""

nombre = input('Ingrese el nombre del circulo: ')
radio = float(input('Ingrese el valor del radio: '))
diametro = float(input('ingrese el valor del diametro: '))   


""" Instanciar """

c = Circulo(nombre,radio,diametro)

""" Llamando a los metodos"""
area = c.calc_area()
perimetro = c.calc_perimetro()

print(f'El area del circulo es: {area}')
print(f'El perimetro del circulo es: {perimetro}')

print(c)