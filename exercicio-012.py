produto = float(input('Qual o preço do produto? '))

desconto = produto - (produto * 5 / 100)


print('O produto que custava {}, na promoção com desconto de 5% custa {:.2f}'.format(produto, desconto))