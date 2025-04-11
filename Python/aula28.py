for i in range(10):
    if i == 2:
        print("i é 2 pulando para o proximo...")
        continue
    if i == 8:
        print("i é 8, esse lanço não executara")
        break

    for j in range(10):
        print(i, j)
else:
    print("For completo")