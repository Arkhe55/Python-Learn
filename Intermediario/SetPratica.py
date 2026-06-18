letras = set()

while True:
   letra = input("Digite uma letra: ")
   letras.add(letra.lower())

   if 'l' in letras:
      print("PARABÉNS")
      break
   
   print(letras)
