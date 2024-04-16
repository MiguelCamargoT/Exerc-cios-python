#pedindo valores
numero1 = int(input("Digite o primeiro numero: ")) 
numero2 = int(input("Digite o segundo numero: ")) 
numero3 = int(input("Digite o terceiro numero: ")) 
#comparando valores
if numero1 > numero2 and numero1 > numero3:
    print(numero1)
elif numero2 > numero1 and numero2 > numero3:
    print(numeor2)
elif numero3 > numero1 and numero3 > numero2:
    print(numero3)
else:
    print("Numeros iguais")
