#2- Peça a temperatura em Fahrenheit e exiba o valor convertido em Celsius
fah = input("Digite a temperatura em fahrenheit: ")
fah = float(fah)
cel = fah - 32
cel1 = cel / 1.8
print(f"A temperatura convertida em celsius é: {cel1:.2f}")