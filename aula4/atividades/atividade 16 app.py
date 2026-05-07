#16- Solicite um valor principal, a taxa de juros e o tempo e exiba dos juros simples
num = input("O valor é: ")
tax = input("A taxa de juros é: ")
temp = input("O tempo em dias é: ")
num = int(num)
tax = float(tax)
temp = int(temp)
juros = num + tax * temp
print("O juros a ser pago é: ",(juros))