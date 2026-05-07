'''
1. Crie um programa que o usuario possa digitar quantos numeros ele quiser
e apos terminar  imprima a lista em ordem crescente.
'''
lista_num=[]
while True:
    num = input("Digite um número: ")
    num = float(num)
    lista_num.append(num)
    opcao = input("Deseja adicionar mais um número?(Enter - continua | n - Não)").lower()

    if opcao == "n":
        break

lista_num.sort()
print(lista_num)