from io import open
import math

lectura=""
texto=open("archivo.text","r")
#texto.write("Hola, soy un archivo de texto\n")
#texto.write("Hola, Mundo2\n")
lectura=texto.readlines()
print(type(lectura))
print(lectura)
for i in lectura:
    print(i)
texto.close()