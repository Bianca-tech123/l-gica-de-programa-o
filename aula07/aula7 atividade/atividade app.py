'''
desenvolva um sistema de gerenciamento de veículos, permita cadastrar o veículo pegando do usuário os seguintes dados (modelo,marca,preço)

-os dados devem ser armazenados em um arquivo
- o usuário deve poder cadastrar quantos carros quiser sem ter que rodar o sistema novamente
  rodar o sistema novamente.
- deve ter a opção de ler os carros existentes
-devem ser cadastrados em um arquivo .txt e usar dicionário

'''
import os
import time

carros = []
arquivo_txt = "lista_carros.txt"

# Carregar carros do arquivo
if os.path.exists(arquivo_txt):
    with open(arquivo_txt, "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split("|")

            carro = {
                "id": int(dados[0]),
                "modelo": dados[1],
                "preco": float(dados[2]),
                "marca": dados[3]
            }

            carros.append(carro)

# Próximo ID
if carros:
    proximo_id = carros[-1]["id"] + 1
else:
    proximo_id = 1


# Função para salvar arquivo
def salvar_arquivo():
    with open(arquivo_txt, "w") as arquivo:
        for carro in carros:
            arquivo.write(
                f"{carro['id']}|{carro['modelo']}|{carro['preco']}|{carro['marca']}\n"
            )


while True:

    print("\n===== Sistema de Carros 🚗 =====")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("3 - Atualizar carro")
    print("4 - Deletar carro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # CREATE
    if opcao == "1":

        modelo = input("Digite o modelo: ").title()
        marca = input("Digite a marca: ").title()
        preco = float(input("Digite o preço: ").replace(",", "."))

        carro = {
            "id": proximo_id,
            "modelo": modelo,
            "marca": marca,
            "preco": preco
        }

        carros.append(carro)

        proximo_id += 1

        salvar_arquivo()

        print("Carro cadastrado!")

    # READ
    elif opcao == "2":

        if not carros:
            print("Nenhum carro cadastrado!")

        else:
            print("\n===== LISTA DE CARROS =====")

            for carro in carros:
                print(
                    f"ID: {carro['id']} | "
                    f"Modelo: {carro['modelo']} | "
                    f"Marca: {carro['marca']} | "
                    f"Preço: R$ {carro['preco']:.2f}"
                )

    # UPDATE
    elif opcao == "3":

        for carro in carros:
            print(
                f"ID: {carro['id']} | "
                f"Modelo: {carro['modelo']} | "
                f"Marca: {carro['marca']} | "
                f"Preço: R$ {carro['preco']:.2f}"
            )

        id_busca = int(input("Digite o ID do carro: "))

        encontrado = False

        for carro in carros:

            if carro["id"] == id_busca:

                carro["modelo"] = input("Novo modelo: ").title()
                carro["marca"] = input("Nova marca: ").title()
                carro["preco"] = float(
                    input("Novo preço: ").replace(",", ".")
                )

                salvar_arquivo()

                print("Carro atualizado!")

                encontrado = True

                break

        if not encontrado:
            print("Carro não encontrado!")

    # DELETE
    elif opcao == "4":

        for carro in carros:
            print(
                f"ID: {carro['id']} | "
                f"Modelo: {carro['modelo']} | "
                f"Marca: {carro['marca']} | "
                f"Preço: R$ {carro['preco']:.2f}"
            )

        id_busca = int(input("Digite o ID para deletar: "))

        encontrado = False

        for carro in carros:

            if carro["id"] == id_busca:

                carros.remove(carro)

                salvar_arquivo()

                print("Carro deletado!")

                encontrado = True

                break

        if not encontrado:
            print("Carro não encontrado!")

    # SAIR
    elif opcao == "0":

        print("Saindo do sistema...")

        for i in range(11):

            barra = "🟩" * i
            porcentagem = i * 10

            print(f"\r[{barra:<10}] {porcentagem}%", end="")

            time.sleep(0.2)

        print("\nSistema encerrado!")

        break

    else:
        print("Opção inválida!")