#atividade do dia 02/4
cardapio = {
    100: 1.20,
    101: 1.30,
    102: 1.50,
    103: 1.20,
    104: 1.70,
    105: 2.20,
    106: 1.10
}
codigo_produto = int(input('Digite o codigo do produto ae pai:'))
quantidade = int(input('Digita a quntidade que voce quer ae pai:'))

if codigo_produto in cardapio:
     
   preco_unitario = cardapio[codigo_produto]
   valor_total = preco_unitario * quantidade
   print('valor a ser pago: R$', valor_total)
else:
       print("produto não encontrado no cardapio.")

