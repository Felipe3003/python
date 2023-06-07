
import math
angulo = float(input('Digite o angulo '))

seno = math.sin(math.radians(angulo))
print('o angulo de {} tem o seno de {:.2f}'.format(angulo, seno))

cos = math.cos(math.radians(angulo))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cos))

tang = math.tan(math.radians(angulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tang))