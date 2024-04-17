#aula do dia 02/04
# lista meses
meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

# valor pelo usuario
numero = int(input("Digite um número entre 1 e 12: "))

# Verifica se o numero e valido
if numero >= 1 and numero <= 12:
    # Se sim, esta mensagem e ativada
    print("O mês correspondente ao número", numero, "é", meses[num])
else:
    # Se não, exibe esta mensagem
    print("Não existe mês com este número.")


