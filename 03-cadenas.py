text1="Hola"
text2="Mundo"

textoFinal=text1+" "+text2
print(textoFinal)

print("El saludo es: %s %s" %(text1,text2))

saludoFinal2="Saludo: {x} {y}".format(x=text1,y=text2)
print(saludoFinal2)

texto="desarrollo web profecional utl"
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title())
print(texto.find("a"))
print(texto.count("e"))

print(texto.replace("e", "a"))

cadenaSeparada=texto.split(" ")
print(cadenaSeparada)

