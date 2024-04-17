#aula do dia 02/04
import math
# Lê o número fornecido pelo usuário
num = float(input("Digite um número: "))

# Verifica se o número é positivo
if num >= 0:
    # Calcula a raiz quadrada do número
    raiz_quadrada = math.sqrt(num)
    print("A raiz quadrada de", num, "é", raiz_quadrada)
else:
    # Se o número for negativo, mostra uma mensagem de erro
    print("Número inválido. Por favor, forneça um número positivo.")



