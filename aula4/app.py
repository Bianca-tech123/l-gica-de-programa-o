#for

# laço de for, ele é finito: quando eu sei o numero de repetições

#frutas = ['melancia', 'abacaxi','melão','pera']
#fruta = 'melancia'
#for f in frutas:
 #   print(f)

#for range(inicio, fim, salto)

#for i in range(1,20,2):
 #   print("Repeti")

'''
num = int(input('Digite um numero para saber a sua tabuada: '))
for i in range(1,11):
    print(f"{i} X {num} = {i * num}")'''

lista_nomes = ['Arthur Cintra', 'Pietro','Davi','Jose','Jhonny','Bianca','Vitor','Pedro','Nayara','Gustavo','Matheus','Felipe','Erick','Gabriel','Lucas','Victor','Rodrigo','Miguel','Maria','Augusto']
for i,nome in enumerate(lista_nomes):
    print(f'{i+1} {nome}')

nome_buscar = input('Digite um nome para buscar: ').title()
if nome_buscar in lista_nomes:
    print('Usuario encontrado!')

