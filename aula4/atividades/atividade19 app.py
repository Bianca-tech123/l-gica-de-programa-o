#19- Peça a distancia percorrida e o combustivel gasto e exiba o consumo medio do veiculo solicite um numero e exiba o valor absoluto dele 
dis = float(input("Digite a distância percorrida em Km: "))
comb = float(input("Digite o combustível gasto em litros: "))
consum = dis / comb
print(f"O consumo médio é {consum:.2f}, seu valor absoluto é {abs(consum):.2f}")