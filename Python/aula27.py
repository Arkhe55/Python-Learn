"""

Iteravel -> str, range, etc (__iter__) que pode entregar uma coisa por vez
iterador -> que sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue o seu iterador

"""

# texto = "Gabriel".__iter__() #iter("Gabriel")
# print (texto.__next__()) #(next(texto))
# print (texto.__next__())
# print (texto.__next__())
# print (texto.__next__())
# print (texto.__next__())
# print (texto.__next__())
# print (next(texto))

nome = "Gabriel" #iteravel
#iterador = iter(nome) #Iterador

# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break

for iterador in nome:
    print(iterador)