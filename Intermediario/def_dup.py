def numero(fator):
    def multiplicador(a):
        return a * fator
    return multiplicador

dup = numero(2)
trip = numero(3)
quad = numero(4)

print(dup(10))
print(trip(20))
print(quad(30))






    
        
        
    

    
    
    


    
    
        


