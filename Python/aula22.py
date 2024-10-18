variavel = "a"
print(id(variavel))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Executado")

else:
    print("Não executado")

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)




