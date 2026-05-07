#1- Solicite dois números e exiba o resultado da divisão do segundo pelo primeiro com duas casas decimais.
num = input("Digite um número: ")
num2 = input("Digite o segundo número: ")
num = int(num)
num2 = int(num2)
div = num2 / num
print(f"A divisão é: {div:.2f}"