

from cliente import *
from hotel import *

def menu():
    print("\n===== SISTEMA HOTEL =====")
    print("1 - Criar cliente")
    print("2 - Listar clientes")
    print("3 - Consultar cliente")
    print("4 - Atualizar cliente")
    print("5 - Remover cliente")
    print("6 - Criar hotel")
    print("7 - Listar hotéis")
    print("8 - Consultar hotel")
    print("9 - Atualizar hotel")
    print("10 - Remover hotel")
    print("0 - Sair")

def main():
    while True:
        menu()
        op = input("Escolha uma opção: ")

        if op == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            data = input("Data nascimento (YYYY-MM-DD): ")
            criar_cliente(nome, telefone, email, data)

        elif op == "2":
            listar_clientes()

        elif op == "3":
            id_cliente = input("ID do cliente: ")
            consultar_cliente(id_cliente)

        elif op == "4":
            id_cliente = input("ID do cliente: ")
            nome = input("Novo nome (enter para manter): ")
            telefone = input("Novo telefone (enter para manter): ")
            email = input("Novo email (enter para manter): ")
            data = input("Nova data nascimento YYYY-MM-DD (enter para manter): ")
            atualizar_cliente(
                id_cliente,
                nome if nome else None,
                telefone if telefone else None,
                email if email else None,
                data if data else None
            )

        elif op == "5":
            id_cliente = input("ID do cliente: ")
            remover_cliente(id_cliente)

        elif op == "6":
            nome = input("Nome do hotel: ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            classificacao = input("Classificação: ")
            criar_hotel(nome, endereco, telefone, classificacao)

        elif op == "7":
            listar_hoteis()

        elif op == "8":
            id_hotel = input("ID do hotel: ")
            consultar_hotel(id_hotel)

        elif op == "9":
            id_hotel = input("ID do hotel: ")
            nome = input("Novo nome (enter para manter): ")
            endereco = input("Novo endereço (enter para manter): ")
            telefone = input("Novo telefone (enter para manter): ")
            classificacao = input("Nova classificação (enter para manter): ")
            atualizar_hotel(
                id_hotel,
                nome if nome else None,
                endereco if endereco else None,
                telefone if telefone else None,
                classificacao if classificacao else None
            )

        elif op == "10":
            id_hotel = input("ID do hotel: ")
            remover_hotel(id_hotel)

        elif op == "0":
            print("A sair...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()




























































