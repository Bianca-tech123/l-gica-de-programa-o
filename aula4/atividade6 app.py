"""
1- Solicite dois números e exiba o resultado da divisão do segundo pelo primeiro com duas casas decimais.
2- Peça a temperatura em Fahrenheit e exiba o valor convertido em Celsius
3- Peça o valor em dólares e exiba o valor correspondente em reais.
4- Peça três números e exiba a media aritmética entre eles.
5- Solicite o nome de usuário e mostre qual tipo de dados esta armazenado.
6- Crie uma lista com 10 números e exiba a lista com o dobro de cada um dos números
7- Solicite dois números e verifique se o segundo é menor que o primeiro
8- Solicite o nome e sobre nome de dois usuários e imprima o nome do primeiro com o sobrenome do segundo e o nome do segundo com o sobrenome do primeiro
9- Peça um número e exiba a metade dele
10- Solicite a altura e a largura de um retângulo e exiba a área
11- Crie um sistema que receba um numero e exiba o seu antecessor e seu sucessor
12- Crie um sistema que receba um numero e mostre seu dobro, triplo e raiz quadrada
13- Peça um número e exiba o quadrado dele
14- Peça três numeros e exiba o produto deles
15- Peça o valor de um produto exiba o valor após aplicar um desconto de 10%
16- Solicite um valor principal, a taxa de juros e o tempo e exiba dos juros simples
17- Receba o valor em metro do usuário. Converta o valor em centimetros, milimetros e quilometros. Exiba os tres resultados
18- Peça uma quantidade em horas e exiba o valor correspondente em minutos
19- Peça a distancia percorrida e o combustivel gasto e exiba o consumo medio do veiculo solicite um numero e exiba o valor absoluto dele 
20- Solicite um numero e exiba o valor absoluto dele (sem considerar o sinal)
"""
"""import os, time

lista_numero = [1,2,3,4,5,6,7,8,9,10]
for num in lista_numero:
    dobro = num * 2
    print(f"O dobro de {num} é {dobro}")
time.sleep(10)
os.system("cls")"""

"""
#NOTE - Code do professor
lista = [1,2,3,4,5,6,7,8,9,10]
dobro = [v * 2 for v in lista]
print(dobro)
"""

#NOTE - Outro jeito
lista = [1,2,3,4,5,6,7,8,9,10]
for i in lista:
    dobro = i*2
print(dobro)