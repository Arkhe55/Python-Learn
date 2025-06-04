import os
lista_compras = []

while True:
    opção_usuario = input("Selecione uma opção: [i]nserir " \
    "[a]pagar [l]istar: " )

    if opção_usuario == "i":
       os.system('cls')
       item_add = input("Digite um item para lista de compras: ")
       lista_compras.append(item_add)


    elif opção_usuario == "a":
        indice_str = input("Escolha o indice a apagar")
        try:
            indice = int(indice_str)
            del lista_compras[indice]
        except IndexError:
            print("Indice não existe na lista")
        except ValueError:
            print("Digite um número inteiro")
        except Exception:
            print("Erro desconhecido")

    elif opção_usuario == "l":
        # lista_enumerada = enumerate(lista_compras)
        for item in enumerate(lista_compras):
            print(item)
                          
else:
    print("Por favor digite novamente: ")