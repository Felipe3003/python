print("Digite sua idade")
idade= int(input())

if idade <= 12:
    print("Você ainda é criança")

elif idade >= 13 and idade <=17:
    print("Adolescente")

elif idade >=18:
    print("Adulto")