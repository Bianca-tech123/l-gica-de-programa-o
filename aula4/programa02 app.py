import random
import time
import os

lista_nomes = []
lista_sorteados = []
print(30*"=", "Bem vindo ao Sitstema de Sorteio", 30*"=")

while True:
    nome = input("Digite um nome para o Sorteio: ")
    lista_nomes.append(nome)
    opcao = input("Deseja adicionar mais? (s - sim) ou enter para parar!").lower()
    if opcao != 's':
        break

while True:
    if not lista_nomes:
        print('A lista de nomes está vazia!')
    else:
        nome_sorteado = random.choice(lista_nomes)
        lista_nomes.remove(nome_sorteado)
        lista_sorteados.append(nome_sorteado)
        os.system('cls')

    for i in range(5,-1, -1):
        time.sleep(1)
        os.system('cls')
        print(f'Contagem regressiva...{i}')
    
    print(f'O sorteado foi: {nome_sorteado}')

    sortear_novamente = input('Deseja sortear outro nome? (s - Sim | n - Não)').lower()

    if sortear_novamente == 'n':
        break

print(lista_sorteados)
print('Fim do Programa!')