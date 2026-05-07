import os
os.system("cls")
nome = input("Digite o seu nome: ")
data = input("Digite a sua data de nascimento: ")
peso = input("Digite o seu peso: ")
altura = input("Digite a sua altura: ")

os.system("cls")
print("Olá ",nome,", seja bem-vindo ao sistema Python")
print("Aqui estão as suas informações:")
print("Data de nascimento: ",data)
print("Altura: ",altura)
print("Peso: ", peso,"kg")

print(type(nome))