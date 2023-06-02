dias = float(input('Quantos dia você ficou com o carro? '))
km = float(input('Quantos km você rodou? '))

resultado = (dias * 60) + (km * 0.15)

print('O total a pagar é {}'.format(resultado))