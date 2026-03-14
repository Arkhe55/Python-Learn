'''Primeiro Codigo feito'''
# numeros = (1,2,3,4,5,6,7,8,9,10)
# def par(numeros):
#     for number in numeros:
#         print(number)
#         if number % 2 == 0:
#             print("O numero é Par")
#         else:
#             print("O numero é Impar")
# par(numeros)

"""Segundo codigo Feito limpo"""
def par(numeros):
    multiplos = numeros % 2 == 0

    if multiplos:
        return f'{numeros} é par'
    return f'{numeros} é ímpar'

print(par(1))
print(par(2))
print(par(3))
print(par(4))
print(par(5))
print(par(6))
print(par(7))