lista_compras = []

while True:
    opção_usuario = input("Selecione uma opção: [i]nserir " \
    "[a]pagar [l]istar: " )

    if opção_usuario == "i":
       item_add = input("Digite um item para lista de compras: ")
       lista_compras.append(item_add)


    elif opção_usuario == "a":
        try:
            lista_compras.pop() 
        except:
            print("Sua lista esta vazia, adicione algo ao a ela.")
            continue

    elif opção_usuario == "l":
        # lista_enumerada = enumerate(lista_compras)
        for item in enumerate(lista_compras):
            print(item)
       
    
           
        
else:
    print("Por favor digite novamente: ")