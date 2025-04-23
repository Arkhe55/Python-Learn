"""Introdução ao desempacotamento"""

# nomes = ["Gabriel", "Rafael", "Miguel"]

# nome1, nome2, nome3 = nomes

# print(nome1)

# nome1, nome2, nome3 = ["Gabriel", "Rafael", "Miguel"]

# print(nome1)

_, nome1, *resto = ["Gabriel", "Rafael", "Miguel"]

print(resto)