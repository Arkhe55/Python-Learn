a = 50
b = 60
c = 70
d = 5.20

#formato = "{} {} {} {:.2f}".format(a, b, c, d) # -> .format com base na ordem
#formato = "{0} {1} {2} {3:.2f}".format(a, b, c, d) # -> .format com base no indice
chaves = "{nome4:.2f} {nome2} {nome1} {nome3}"
formato = chaves.format(nome1=a, nome2=b, nome3=c, nome4=d)# -> .format com base no parametro

print(type(formato))
print(formato)