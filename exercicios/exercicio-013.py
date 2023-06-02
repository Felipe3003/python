salario = float(input('Qual é o salario do funcionario '))

aumento =  salario + (salario * 15 / 100)

print('o funcionario ganhava {}, com 15 % de aumento, passa a receber {:.2f}'.format(salario, aumento))