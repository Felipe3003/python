import math
cateto1 = float(input('Comprimento do cateto oposto '))
cateto2 = float(input('comprimento do cateto adjacente '))

a =  cateto1 ** 2 + cateto2 ** 2
raiz = math.sqrt(a)

print('Sua hipotenusa é: {:.2f}'.format(raiz))