x=0
while x<10:
    print(x)
    x=x+1

'''operacion de multiplicacion de a x b utilizando sumas
a=3
b=4
salida:3+3+3+3=12

(str= convertir entero a cadena)
'''

a = 3
b = 4
r = 0
con = 0

while con < b:
    r += a
    con += 1

print("Salida: {}+{}+{}+{}={}".format(a, a, a, a, r))