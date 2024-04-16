#atividades do dia 9/04/2024
#L = lado
l1 = int (input ('digite o tamanho do primeiro lado do triangulo: '))
l3 = int(input('digite o tamanho do segundo lado do triangulo: '))
l2 = int(input('digite o tamanho do terceiro lado do triangulo: '))
#comoarando lados (l= lado)
if l1 + l2 > l3 or l1 + l3 > l2 or l2 + l3 > l1:
    if l1 == l2 and l2 == l3:
        print('Os lados formam  um triangulo equilatero.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Os lados formam um triangulo isósceles.')
    else:
        print('Os lados formam um triangulo escaleno.')
else:
    print('Os lados não formam um triangulo.')

