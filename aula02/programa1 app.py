"""
 Calculos e manipulação de variaveis
"""

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
peso = input("Digite o seu peso: ")
altura = input("Digite a sua altura: ")

# tratamento de exceção
try:
    idade = int(idade)
    peso = float(peso)
    altura = float(altura)
except ValueError as e:
    print(e)
    ValueError = e
    

imc = peso / altura**2
print("Seu IMC é: ",imc)