#Questão06
"""
import os , time

listaNum = [1,2,3,4,5,6,7,8,9,10]
for num in listaNum:
    dobro = num * 2 
    print (f"O dobro de {num} é {dobro}")
time.sleep(10)
os.system("cls")
"""
lista = [1,2,3,4,5,6,7,8,9,10]
dobro = [v*2 for v in lista]

print(dobro)