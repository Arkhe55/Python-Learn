"""
Listas em python
Tipo List - Mutável
Suporta vários valores de qualquer tipo
"""

string = ("ABCDE")
# print(lista, type(lista))
# print(bool(lista))

lista = [123, 4.3, "Gabriel", False, ["Gabriel", 1234]]
#list Suporta vários valores de qualquer tipo
print(lista[2].upper(),'Tipo:',type(lista[2]))

#Tipo List - Mutável
lista[2] = "Luiz"
print('Nome alterado:',lista[2])
print(lista)
