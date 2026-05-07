''' manipulação de arquivos: pçercorrer os meuis diretórios, encontrar o arquivo, 
passar poor um comando de abertura de arquivo, logo em seguida um comando de ação.

arquivo= open ("arquivo.txt" , "modo")

modos de ação:
- "r": leitura do arquivo
- "w": escrita(sobrescreve o conteúdo antigo)
- "a": adiciona conteúdo
- "x": criar um arquivo
- "b": arquivos binários
- "t": texto
'''
#criando um arquivo
arquivo= open ('primeiro_arquivo.txt', "w")
arquivo.write ('Ola mundo! meu primeiro arquivo')
arquivo.close()

#lendo o arquivo
arquivo= open("prfimeiro_arquivo.txt","r")
conteudo= arquivo.read()
print(conteudo)
arquivo.close()

# aplicando boa prática
with open("primeiro_arquivo.txt," "r")as arquivo:
    conteúdo= arquivo.read()
    print(conteudo)

# arquivo com múltiplas escritas
with open('alunos.txt', 'w') as arquivo:
    arquivo.write('ana\n')
    arquivo.write('bruno\n')
    arquivo.write('lucas\n')
    arquivo.write('felipe\n')

# lendo linha a linha
with open('alunos.txt', "r") as arquivo:
    for linha in arquivo:
        print(linha)

# usando lista para escrever o arquivo
frutas= ['pera','abacaxi','melancia','manga','caju']

with open('frutas.txt', "w")as arquivo:
    for f in frutas:
        arquivo.write(f+ '\n')

# converter o arquivo em uma lista
  with open ('frutas.txt', 'r') as arquivo:
    linhas= arquivo.readlines()

   print(type(linhas))
   print(linhas)

#saída : ['pera\n','abacaxi\n','manga\n','caju\n']

#limpar quebra de linha
with open("frutas.txt" , 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())

#exemplo para cadastro
while true:
    nome=input("Digite seu nome: ").title()

    with open("cadastro.txt", 'a') as arquivo:
        arquivo.write(nome + "\n")

    sair = input("Deseja sair? s/n").lower()
    if sair == 's':
        break
