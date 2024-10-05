numero_str = input("Digite um número: ")

try:
    print("STR: ", numero_str)
    numero_float = float(numero_str)
    print("FLOAT: ", numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2:.0f}")
except:
    print("O valor não é um número")

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f"O dobro de {numero_str} é {numero_float * 2:.0f}")

# else:
#     print("Valor digitado não é um número")