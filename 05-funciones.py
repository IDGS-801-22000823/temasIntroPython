"""
def run():
    funcion1()
    funcion2()
    

def funcion1():
    print("Hola, soy la funcion 1")

def funcion2():
    print("Hola, soy la funcion 2")

if __name__ == "__main__":
    run()
"""
import os

def funcion1():
    os.system("cls")
    print("Suma")
    num1=int(input("Numero1: "))
    num2=int(input("Numero2: "))
    res=num1+num2
    print(f"Resultado : {res}")
    input("Dale enter para el menu")

def funcion2():
    os.system("cls")
    print("Resta")
    num1=int(input("Numero1: "))
    num2=int(input("Numero2: "))
    res=num1-num2
    print(f"Resultado : {res}")
    input("Dale enter para el menu")

def funcion3():
    os.system("cls")
    print("Multiplicacion")
    num1=int(input("Numero1: "))
    num2=int(input("Numero2: "))
    res=num1*num2
    print(f"Resultado : {res}")
    input("Dale enter para el menu")

def funcion4():
    os.system("cls")
    print("Division")
    num1=int(input("Numero1: "))
    num2=int(input("Numero2: "))
    res=num1/num2
    print(f"Resultado : {res}")
    input("Dale enter para el menu")

def funcion5():
    os.system("cls")
    print("Saliendo del programa")

def run():
    while True:
        os.system("cls")
        print("Menu de opciones")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicacion")
        print("4.- Division")
        print("5.- Salir")
        op = int(input("Opcion: "))
        
        if op == 1:
            funcion1()
        elif op == 2:
            funcion2()
        elif op == 3:
            funcion3()
        elif op == 4:
            funcion4()
        elif op == 5:
            funcion5()
            break
        else:
            print("Que no vez que dice hasta el 5?.")
            input("Presiona enter para continuar")

if __name__ == "__main__":
    run()