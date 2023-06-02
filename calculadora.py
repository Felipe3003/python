import math  
import sys

print("Calculadora uninove- Para seguir informe a operação")

print("Digite um numero para operação ")
operador = input()

if operador not in ['1', '2', '3', '4', '5', '6', '7']:
    print("Dados Inconsistentes.")
    sys.exit()

if operador == '6':
   numero = float(input("Digite um numero:"))
   raiz_quadrada = math.sqrt(numero)
   print('O resultado da raiz quadrada é: ',raiz_quadrada)
else:

    print("Digite o primeiro numero:")
    numero1 = int(input())
    print("Digite o segundo numero:")
    numero2 = int(input())

if operador == '1':
    resultado = numero1 + numero2
    print('O resultado da adição é: ',resultado)

elif operador == '2':
    resultado = numero1 - numero2
    print('O resultado da subtração é: ',resultado)

elif operador == '3':
    resultado = numero1 * numero2
    print('O resultado da multiplicação é: ',resultado)

elif operador == '4':
    resultado = numero1 / numero2
    print('O resultado da divisão é: ',resultado)

elif operador == '5':
    resultado = numero1 % numero2
    print('O resultado do resto da divisão é: ',resultado)

elif operador == '7':
    resultado = numero1 ** numero2
    print('O resultado da exponenciação é: ',resultado)


