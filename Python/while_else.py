string = "valor qualquer"

i = 0
while i < len(string):
    letra = string[i]

    print(letra)

    '''if letra == " ":
        break'''

    i += 1
else:
    print("Fim do while")
print("fora o while")