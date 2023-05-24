

numero = int(input("Digite um número: "))
tipo = input("Digite 'par' ou 'impar': ")

if tipo == 'par':
    inicio = 0
    incremento = 2
else:
    inicio = 1
    incremento = 2

for i in range(inicio, numero + 1, incremento):
    print(i)
