import os
import time

carros = []
proximo_id = 1

os.system("cls")
while True:
    print("===== Sistema de Carros 🚗 =====")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("3 - Atualizar carro")
    print("4 - Deletar carro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")
#create
    if opcao == "1":
        modelo = input('Digite o modelo do carro: ').title()
        preco = float(input ('Digite o preço do carro: ').replace(",", "."))
        marca = input('Digite a marca do carro: ')

        carro = {
            'id'      : proximo_id,
            'modelo'  : modelo,
            'preco'   : preco,
            'marca'   : marca   
        }

        carros.append(carro)
        proximo_id +=1

        print("✅Carro cadastrado com sucesso!")
#read
    elif opcao == "2" :
        if not carros:
            print("❌Nenhum carro cadastrado!")
        else:
            print("\nLista de Carros")
            for carro in carros:
                print(f"ID: {carro['id']}| Modelo: {carro['modelo']}| Preço: {carro['preco']}| Marca: {carro['marca']}")
#update
    elif opcao == "3" :
     for carro in carros:
        print("\nLista de Carros")
        print(f"ID: {carro['id']}| Modelo: {carro['modelo']}| Preço: {carro['preco']}| Marca: {carro['marca']}")
     id_busca = int(input("Digite o id do carro para atualizar:"))

     encontrado = False
     for carro in carros:
         if carro['id'] == id_busca:
            novo_modelo = input('Digite o novo modelo: ').title()
            novo_preco = float(input('Digite o novo preço: ').replace(",","."))
            nova_marca = input('Digite o novo marca: ').title

            carro["modelo"] = novo_modelo
            carro ["preco"] = novo_preco
            carro ["marca"] = nova_marca

            print("Carro atualizado com sucesso!")
            encontrado = True
            break
     if not encontrado:
         print("Carro não encontrado!")
                         
#delete
    elif opcao == "4" :
        print("\nLista de Carros")
        print(f"ID: {carro['id']}| Modelo: {carro['modelo']}| Preço: {carro['preco']}| Marca: {carro['marca']}")
        id_busca = int(input("Digite o id do carro para deletar: "))
        encontrado = False
        for carro in carros:
            if carro['id'] == id_busca:
             carros.remove(carro)
             print("Carro deletado com sucesso!")
             break
        if not encontrado:
            print("Carro não encontrado!")

    elif opcao == "0":
            total = 10
            barra =""
            print("Saindo do Sistema...")
            for i in range(total+1):
                barra +="🟩" 
                porcentagem = int((i / total ) *100)
                vazio = "-"*(total - 1)
                print(f'\r[{barra}] {porcentagem}%', end ="")     
                time.sleep(0.2)
            break
    else:
            print("❌Opção Inválida")