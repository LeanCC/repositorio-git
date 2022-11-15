""" Importamos math para usar PI """
import math

PI = math.pi

""" Creamos la clase """

if __name__ == "__main__":

  class Circulo:
    def __init__(self,radio,diametro) -> None:
     self.radio = radio
     self.diametro = diametro

    """ Métodos """
    def calc_area(self):
      return (self.radio**2)*PI


    def calc_perimetro(self):
      return self.diametro*PI


""" Pedir el valor del radio y diametro del circulo"""

radio = float(input('Ingrese el valor del radio: '))
diametro = float(input('ingrese el valor del diametro: '))   


""" Instanciar """

c = Circulo(radio,diametro)

""" Llamando a los metodos"""
area = c.calc_area()
perimetro = c.calc_perimetro()

print(f'El area del circulo es: {area}')
print(f'El perimetro del circulo es: {perimetro}')
