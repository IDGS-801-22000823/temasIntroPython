range(20) #0,1,2,...19
x=range(10,20)
y=range(1,20, 2)

for i in range(20):
    print(i) #0,1,2,...19

"""
7x1=7
7x2=14
7x3=21
.
.
x10=70
fin
"""
numer=int(input("Numero: "))
for i in range(1,11):
    print(f"{numer}x{i}={numer*i}")