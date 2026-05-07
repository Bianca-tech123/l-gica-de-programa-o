#7- Solicite dois números e verifique se o segundo é menor que o primeiro
num1 = input("Digite um numero: ")
num2 = input("Digite o segundo numero: ")

num1 = float(num1)
num2 = float(num2)

if num2 < num1:
    print("O segundo número e menor que o primeiro.")
else:
    print("O segundo número e maior que o primeiro.")