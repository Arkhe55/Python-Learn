number = (50,60,70,80,60,40,45,43)

def mult(number):
    total = 2
    for numero in number:
        print(total, "*" ,numero)
        total *= numero
        print("Total", total)
      
mult(number)
