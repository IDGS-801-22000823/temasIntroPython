
import math

class Distancia:
    #Declaracion de propiedades
    x1=0
    x2=0
    y1=0
    y2=0
    res1=0
    res2=0
    respuesta=0
    #Declaracion del  constructor this
    def __init__(self,x1=0,x2=0,y1=0,y2=0):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        #Declaracion de metodos de clase
        #pedir datos
    def datos(self):
        self.x1 = float(input("Introduce el valor de x1: "))
        self.x2 = float(input("Introduce el valor de x2: "))
        self.y1 = float(input("Introduce el valor de y1: "))
        self.y2 = float(input("Introduce el valor de y2: "))
        #Operacion
    def operacion(self):
        self.res1=((self.x2-self.x1))
        self.res2=((self.y2-self.y1))

        self.res1=math.pow(self.res1,2)
        self.res2=self.res2**2

        self.respuesta=(math.sqrt(self.res1+self.res2))
        print("La distancia es: {}".format(self.respuesta))

def main():
    obj = Distancia()
    obj.datos()
    obj.operacion()

if __name__=='__main__':
    main()