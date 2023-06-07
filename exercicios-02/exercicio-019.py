from random import choice
aluno1 = input('Digite o nome do primeiro aluno ')
aluno2 = input('Digite o nome do segundo ')
aluno3 = input('Digite o nome do terceiro ')
aluno4 = input('Digite o nome do quarto ')

sorte = [aluno1, aluno2, aluno3, aluno4]
sort = choice(sorte)

print('o sorteado foi {}'.format(sort))