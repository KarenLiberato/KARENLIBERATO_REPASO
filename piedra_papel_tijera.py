piedra=3
tijera=2
papel=4

p_1=int(input("digite puntaje de partcipante 1:  "))
p_2=int(input("digite puntaje de participante2:  "))
if p_1==papel and p_2==piedra:
    print("papel envuelve a piedra")
elif p_1==papel and p_2==papel:
    print("empate de papel")
elif p_1==papel and p_2==tijera:
    print("tijera corta papel")
elif p_1==tijera and p_2==tijera:
    print("empate de tijera")
elif p_1==tijera and p_2==papel:
    print("tijera corta a papel")
elif p_1==tijera and p_2==piedra:
    print("piedra mata a tijera")
elif p_1==piedra and p_2==piedra:
    print=("empate de piedra")
elif p_1==piedra and p_2==papel:
    print=("papel envuelve a piedra")
elif p_1==piedra and p_2==tijera:
    print=("piedra le gana a tijera")
    