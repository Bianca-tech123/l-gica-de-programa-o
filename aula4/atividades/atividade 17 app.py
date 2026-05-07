#17- Receba o valor em metro do usuário. Converta o valor em centimetros, milimetros e quilometros. Exiba os tres resultados
val = input("O valor em metros é: ")
val = float(val)
cm = val * 100
cm = float(cm)
mili = val * 1000
km = val / 1000

print("O valor em centímetros é: ",(cm),"\n","O valor em milimetros é: ",(mili),"\nO valor em quilomêtros é: ",(km))