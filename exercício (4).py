#atividades do dia 9/04/2024
import math
#atribuindo valores
a = float(input('Digite o valor de a: '))
if a <= 0:
    print('a não pode ser menor ou igual a 0 para uma equação de segundo grau')
else:
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
#aplicando Bhaskara
    if a == 0:
        print("A equação não é do segundo grau.")
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("A equação não possui raízes reais.")
        elif delta == 0:
            raiz = -b / (2*a)
            print("A equação possui uma raiz real:", raiz)
        else:
            r1 = (-b + math.sqrt(delta)) / (2*a)
            r2 = (-b - math.sqrt(delta)) / (2*a)
            print("A equação possui duas raízes reais:", r1, "e", r2)
