import random

primeiro = input('Primeiro Aluno ')
segundo = input('Segundo Aluno ')
terceiro = input('Terceiro Aluno ')
quarto = input('Quarto aluno ')

quadro = [primeiro, segundo, terceiro, quarto]
random.shuffle(quadro)
print('A ordem será')
print(quadro)