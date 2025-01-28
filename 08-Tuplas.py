'''
Las tuplas son immutablas
Se declaran con ()
'''

tupla=("una", "dos", "tres")
print(tupla)

tuplasVariables=(12,True,23.5,"El gato", 12+4j)
print(tuplasVariables)

tuplasConTuplas=(1,2,3,4,(1,2,3))
print(tuplasConTuplas)

print
print(tuplasVariables[3])
print(tuplasVariables[-2])
print(tuplasVariables[0:2])

a,b,c=tupla
print(a,b,c)
