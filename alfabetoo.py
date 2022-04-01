contar=0
texto1=input("digite:   ")
alfabeto=("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
for i in contar:
    if i in alfabeto:
        contar+=1
    
        print("se encontraron caracteres no alfabeticos")
        break
    else:
        contar==len(contar)
        print("se encontraron que todos los caracteres son alfabeticos")
        