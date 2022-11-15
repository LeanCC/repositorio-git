""" Importamos math para usar PI """
import math

PI = math.pi

  #Creamos la clase

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


    def multiplicacion(self):
      n = float(input('Digite el numero por el cual multiplicar el circulo: '))
      try:
        if n <= 0:
          raise Exception('ERROR')
        return self.radio* n
      except Exception:
        print('ERROR EL VALOR QUE DEBES DIGITAR NO PUEDE SER IGUAL O MENOR A 0')


    def __str__(self) -> str:
      return (f'{self.nombre}:\n' +
         f'Es un circulo con un radio de: {self.radio}\n' + 
         f'y un diametro de: {self.diametro}\n')



""" Instanciar """

while True:
  try:

    # Le damos los valores al circulo 

    nombre = input('Ingrese el nombre del circulo: ')
    radio = float(input('Ingrese el valor del radio: '))
    diametro = float(input('ingrese el valor del diametro: '))

    c = Circulo(nombre,radio,diametro)   
 
     # Mostramos el circulo en pantalla en caso de que los datos sean validos

    if radio <= 0:
      raise Exception('EL RADIO DEL CIRCULO NO PUEDE SER MENOR O IGUAL A 0')
    else:
       area = c.calc_area()
       perimetro = c.calc_perimetro()

       print(f'El area del circulo es: {area}')
       print(f'El perimetro del circulo es: {perimetro}')
       print()
       print(c,end=' ')


       op = int(input('Desea modificar el radio del circulo? Digite 1 para SI y 2 para NO: '))

        # Devolvemos el nuevo valor del area en caso de querer modificarlo

       if op == 1:
        try:
          radio = float(input('Ingrese el nuevo valor del radio: '))
          if radio <= 0:
            raise Exception('ERROR')
          area = c.calc_area()
          print(f'El nuevo valor del area es: {area}')

        except Exception:
          print('ERROR: NO SE PUEDE ASIGNAR UN VALOR MENOR O IGUAL A 0 AL RADIO DEL CIRCULO')
          break
        
          # Realizamos la multiplicacion del radio en caso de asi requerirlo

       elif op == 2:
        op_multi = int(input('Desea multiplicar el ciculo anterior? Digite 1 para SI y 2 para NO: '))
        if op_multi == 1:
         n_radio = c.multiplicacion()

         print(f'El nuevo objeto tiene los siguientes valores : \n' + 
              f'Nombre: {c.nombre}\n' +
              f'Diametro: {c.diametro}\n' +
              f'Nuevo Radio: {n_radio}')
         break


        elif op_multi == 2:
          break



  except:
    print('ERROR: EL RADIO DEL CIRCULO NO PUEDE SER MENOR O IGUAL A 0')
    break






    
    




