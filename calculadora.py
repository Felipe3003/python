
import math  
import sys

print("Calculadora uninove- Para seguir informe a operação")

print("Digite um numero para operador")
operador = input()

if operador >'7':
    print("Dados inconsistentes")
    sys.exit()

if operador == '6':
   numero=float(input("Digite um numero:"))
   raiz_quadrada = math.sqrt(numero)
   print( raiz_quadrada)

else:

    print("Digite o primeiro numero:")
    numero1 = int(input())
    print("Digite o segundo numero:")
    numero2 = int(input())

if operador == '1':
    resultado = numero1 + numero2
    print(resultado)

elif operador == '2':
    resultado = numero1 - numero2
    print(resultado)

elif operador == '3':
    resultado = numero1 * numero2
    print(resultado)

elif operador == '4':
    resultado = numero1 / numero2
    print(resultado)

elif operador == '5':
    resultado = numero1 % numero2
    print(resultado)

elif operador == '7':
    resultado = numero1 ** numero2
    print(resultado)
