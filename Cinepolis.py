
import os
from io import open

class Cinepolis:

    # Declaracion de propiedades
    nombre = ""
    boletos = 0
    total = 0
    operacion = 0
    descuento_tarj = 0
    descuento = 0
    con_total = 0
    personas = 0

    # Declaracion del constructor
    def __init__(self, nombre="", boletos=0, total=0, descuento_tarj=0, descuento=0, con_total=0, personas=0):
        self.nombre = nombre
        self.boletos = boletos
        self.total = total
        self.descuento_tarj = descuento_tarj
        self.descuento = descuento
        self.con_total = con_total
        self.personas = personas

    # Metodo para pedir el nombre
    def nombres(self):
        os.system("cls")
        self.nombre = input("Introduce tu nombre: ")
        #Preguntar si tambien puedo usar .isalpha() que es solo para texto sin espacio y que no este vacio
        if not self.nombre:
            input("¿Acaso te llamas null? Intenta de nuevo por gracioso.")
            self.nombres()
        else:
            self.pedir_personas()

    # metodo para pedir el numero de personas
    def pedir_personas(self):
        os.system("cls")
        while True:
            self.personas = input("Introduce el numero de personas: ")
            if self.personas.isdigit():
                self.personas = int(self.personas)
                if self.personas > 0:
                    self.boleto()
                    break
                else:
                    print("El numero de personas debe ser mayor que 0.")
            else:
                print("Ingresa un numero valido.")

    # Metodo para pedir el numero de boletos
    def boleto(self):
            os.system("cls")
            while True:
                self.boletos = input("Introduce el numero de boletos: ")
                if self.boletos.isdigit():
                    self.boletos = int(self.boletos)
                    if self.boletos > 0:
                        self.validar_boletos()
                        break
                    else:
                        print("El numero de boletos debe ser mayor que 0.")
                else:
                    print("Ingresa un numero valido.")

#Metodo que valida lo del boleto y persona
    def validar_boletos(self):
        if self.boletos <= self.personas * 7:
            self.costo()
        else:
            print(f"El numero maximo de boletos para {self.personas} personas es {self.personas * 7}")    
            while True:
                print("Que vas a corregir?")
                print("1.- Personas")
                print("2.- Boletos")
                opcion = input("Selecciona una opcion (1 o 2): \n")
                if opcion == "1":
                    self.cambiar_personas()
                    return
                elif opcion == "2":
                    self.boleto()
                    return
                else:
                    print("Que divertido te ganaste otro intento.")

#Cambiar numero de persoas
    def cambiar_personas(self):
            os.system("cls")
            while True:
                self.personas = input("Introduce el numero de personas: ")
                if self.personas.isdigit():
                    self.personas = int(self.personas)
                    if self.personas > 0:
                        self.validar_boletos()
                        break
                    else:
                        print("El numero de personas debe ser mayor que 0.")
                else:
                    print("Don comedias ingresa un numero valido.")

    # Meetodo para calcular el costo
    def costo(self):
        self.operacion = (self.boletos * 12)
        self.descuentos()

    # Metodo para calcular los descuentos
    def descuentos(self):
        if 3 <= self.boletos <= 5:
            self.descuento = (self.operacion * 0.10)
            self.descuento = (self.operacion - self.descuento)
            self.tarjetas()
        elif 6 <= self.boletos:
            self.descuento = (self.operacion * 0.15)
            self.descuento = (self.operacion - self.descuento)
            self.tarjetas()
        elif 1 <= self.boletos <= 2:
            self.descuento = self.operacion
            self.tarjetas()

    # Metodo para calcular el descuento de la tarjeta si se tiene
    def tarjetas(self):
        while True:
            os.system("cls")
            print("¿Tienes tarjeta CINECO?")
            print("1.- Si")
            print("2.- No")
            opcion = input("Selecciona una opción (1 o 2): ")
            if opcion == "1":
                self.descuento_tarj = self.descuento * 0.10
                self.total = self.descuento - self.descuento_tarj
                self.mostrar()
                break
            elif opcion == "2":
                self.total = self.descuento
                self.mostrar()
                break
            else:
                input("Muy gracioso. Presiona enterr para intentar de nuevo.")

    # Metodo que muestra nombre y total
    def mostrar(self):
        os.system("cls")
        print("Nombre: ", self.nombre, " Total: ", self.total)
        self.con_total = (self.con_total + self.total)
        self.archivo()
        input("Presiona enter para continuar")

    # Archivo de texto
    def archivo(self):
        texto = open("archivoCine.text", "a")
        texto.write(f"Nombre: {self.nombre} Total: {self.total}\n")
        texto.close()

    # Leer
    def leer(self):
        os.system("cls")
        texto = open("archivoCine.text", "r")
        lectura = texto.readlines()
        for i in lectura:
            print(i)
        texto.close()
        print("Total del dia: ", self.con_total)
        input("Presiona enter para continuar")
        #self.archivo_total()
        self.borrar()

    # Borrar
    def borrar(self):
        os.system("cls")
        texto = open("archivoCine.text", "w")
        texto.close()

    def run(self):
        while True:
            os.system("cls")
            print("Menu de opciones")
            print("1.- Realizar compra de boletos")
            print("2.- Salir")
            op = int(input("Opción: (1 o 2)\n"))
            if op == 1:
                self.nombres()
            elif op == 2:
                self.leer()
                break
            else:
                print("¿Que no ves que dice hasta el 2?.")
                input("Presiona enter para continuar")

def main():
    obj = Cinepolis()
    obj.run()

if __name__ == '__main__':
    main()
    
'''
    # Archivo de texto total del dia
    def archivo_total(self):
        texto = open("archivoCine.text", "a")
        texto.write(f"Total del dia: {self.con_total}")
        texto.close()
        input("Presiona enter para continuar")
        self.borrar()
'''