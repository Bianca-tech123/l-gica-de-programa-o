"""
[] Lista --> inteiros/textuais/logicos --> array
{} --> dicionário --> objeto
() --> tupla -> constante --> const
"""

lista = ['gomes','fulano' ,'ciclano','beltrano', 'cintra']

#imprimindo apenas valor especifico da lista 
print(lista[0])

#imprimindo o ultimo valor 
print(lista[-1])

#imprimindo intervalo
print(lista[0:3])

#ordenar lista
#lista.sort()

#inserção na lista
lista.append('karython')

#inserindo em posição específica
lista.insert(2,'james bond')

#inserindo varios valores
lista.extend(['ana', 'beatriz', 'david', 'josé'])

numeros = []

#adicionando de forma dinâmica
for i in range(10):
    numeros.append(i*2)
print(numeros)

#removendo item da lista
print(f"Lista antes de remover{lista}")

#pop -> remove pelo indice
lista.pop(0)

#removendo o ultimo
lista.pop()

#removendo pelo valor, obs: remove a primeira ocorrencia
lista.remove('ciclano')




print(f"Lista depois de remover{lista}")
"""for i in range(len(lista)):
    print(f"{i+1}° valor da lista: {lista[i]}")"""

lista_numeros = [n for n in range(11)]
print(f"Lista antes de remover {lista_numeros}")
#removendo intervalo por indice 
del lista_numeros[2:5]
print(f"Lista depois de remover{lista_numeros}")

lista_nomes = ['gomes','fulano' ,'ciclano','beltrano', 'cintra']
#alteração valor da lista

lista_nomes[1] = 'lucas'

print(lista_nomes)

numero = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numero)):
    if numero[i] > 5:
        numero[i] = numero[i]*2
print(numero)

#list compreheision
numero2 = [10,20 ,30, 40,50]

numero2 = [n*2 if n > 20 else n for n in numero2]
print(numero2)