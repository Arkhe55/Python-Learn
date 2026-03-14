"""
args argumentos não nomeados

* - * args (empacotamento e desempacotamento)
"""

x, y, *resto = 1, 2, 3, 4, 5
print(x, y, resto)

# def soma (x, y):
#     print(x, y, *resto)

# soma(x, y)

def argumento(*args):
    total = 0
    for numero in args:
        print("Total", total, numero)
        total += numero
        print("Total", total)

argumento(1, 2, 3, 4, 5, 6, 7)


