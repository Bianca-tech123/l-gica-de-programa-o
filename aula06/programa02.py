"""2.crie um programa q o usuarrio possa digitar a quantidade desejada de notas de um aluno (nota minima 0 nota maxima 10)
 e o programa calcule a media desse aluno e ao final imprima se o aluno esta aprovado >== 7, reprovado ou de recuperação"""



import os

os.system("cls")

print("Boletim Escolar")
status = ()
lista_notas = []
nome = input("Digite o nome do aluno: ").title

while True:
    nota = input("Digite uma nota: ")
    nota = float(nota)
    if 0<= nota <=10:
        lista_notas.append(nota)
        print(lista_notas)
        status = 0
    else:
        print("Nota Inválida")
        status = 1
        break
    opcao = input("Deseja adicionar mais notas?(Enter - continua | n - Não)").lower()

    if opcao == "n":
        break

if status <= 0:
   
    media = sum(lista_notas) / len(lista_notas)

    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")
else:
    print("Impossivel calcular a média")
   