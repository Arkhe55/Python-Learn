altura = input("Qual sua altura em metros?: ")
peso = input("Peso atual em KG?: ")

try:
    altura_float = float(altura)
    peso_int = int(peso)
    imc = peso_int / altura_float ** 2
    
    print(f"Seu IMC é {imc:.2f}")

    if imc < 18.5:
        print("Magreza")
    elif 18.5 <= imc < 25:
        print("Saudavel")
    elif 25 <= imc < 30:
        print("Sobrepesso")
    elif 30 <= imc < 35:
        print("Obesidade Grau I")
    elif 35 <= imc < 40:
        print("Grau de obesidade II")
    else: ("Obesidade grau III")

except:
    print("O Formato do número digitado esta incorreto")