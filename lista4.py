a=list(range(1,21))
for i in a:
    n=int(input("Digite el numero:  "))
    if n>0:
        print(a.index(n))
    else:
        if n<0:
            print("el numero es invalido,tiene que ser positivo")
        
        



