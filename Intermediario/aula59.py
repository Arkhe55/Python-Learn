# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1,2,3,4,5}
s2 = {1,2,7,5,6}

# s3 = s1 | s2 # - União |
# s3 = s1 & s2
# s3 = s1 - s2 # Diferença de itens no set da esquerda
s3 = s1 ^ s2

print(s3)