
# ==============================
# main.py
# menu terminal para testar CRUD
# ==============================

from cliente import (
    criar_cliente,
    listar_clientes,
    consultar_cliente,
    atualizar_cliente,
    remover_cliente
)

from hotel import (
    criar_hotel,
    listar_hoteis,
    consultar_hotel,
    atualizar_hotel,
    remover_hotel
)


# ------------------------------
# MENU
# ------------------------------
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


# ------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------
def main():
    while True:
        menu()
        op = input("Escolha uma opção: ")

        # ================= CLIENTE =================
        if op == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            data = input("Data nascimento (YYYY-MM-DD): ")

            return_code = criar_cliente(nome, telefone, email, data)

            if return_code[0] == 201:
                print("Cliente criado com sucesso.")
            else:
                print("Internal Error:", return_code[1])

        elif op == "2":
            return_code = listar_clientes()

            if return_code[0] == 200:
                print("Clientes listados com sucesso.")
            else:
                print("Internal Error:", return_code[1])

        elif op == "3":
            id_cliente = input("ID do cliente: ")
            return_code = consultar_cliente(id_cliente)

            if return_code[0] == 200:
                print("Cliente consultado com sucesso.")
            else:
                print("Internal Error:", return_code[1])

        elif op == "4":
            id_cliente = input("ID do cliente: ")

            nome = input("Novo nome (enter para manter): ")
            telefone = input("Novo telefone (enter para manter): ")
            email = input("Novo email (enter para manter): ")
            data = input("Nova data nascimento YYYY-MM-DD (enter para manter): ")

            return_code = atualizar_cliente(
                id_cliente,
                nome if nome else None,
                telefone if telefone else None,
                email if email else None,
                data if data else None
            )

            if return_code[0] == 200:
                print("Cliente atualizado com sucesso.")
            else:
                print("Internal Error:", return_code[1])

        elif op == "5":
            id_cliente = input("ID do cliente: ")
            return_code = remover_cliente(id_cliente)

            if return_code[0] == 200:
                print("Cliente removido com sucesso.")
            else:
                print("Internal Error:", return_code[1])

        # ================= HOTEL =================
        elif op == "6":
            nome = input("Nome do hotel: ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            classificacao = input("Classificação: ")

            return_code = criar_hotel(nome, endereco, telefone, classificacao)

            if return_code[0] == 201:
                print("Hotel criado com sucesso.")
            else:
                print("Internal Error:", return_code[1])

        elif op == "7":
            return_code = listar_hoteis()

            if return_code[0] == 200:
                print("Hotéis listados com sucesso.")
            else:
                print("Internal Error:", return_code[1])

        elif op == "8":
            id_hotel = input("ID do hotel: ")
            return_code = consultar_hotel(id_hotel)

            if return_code[0] == 200:
                print("Hotel consultado com sucesso.")
            else:
                print("Internal Error:", return_code[1])

        elif op == "9":
            id_hotel = input("ID do hotel: ")

            nome = input("Novo nome (enter para manter): ")
            endereco = input("Novo endereço (enter para manter): ")
            telefone = input("Novo telefone (enter para manter): ")
            classificacao = input("Nova classificação (enter para manter): ")

            return_code = atualizar_hotel(
                id_hotel,
                nome if nome else None,
                endereco if endereco else None,
                telefone if telefone else None,
                classificacao if classificacao else None
            )

            if return_code[0] == 200:
                print("Hotel atualizado com sucesso.")
            else:
                print("Internal Error:", return_code[1])

        elif op == "10":
            id_hotel = input("ID do hotel: ")
            return_code = remover_hotel(id_hotel)

            if return_code[0] == 200:
                print("Hotel removido com sucesso.")
            else:
                print("Internal Error:", return_code[1])

        elif op == "0":
            print("A sair...")
            break

        else:
            print("Opção inválida.")


# ------------------------------
# ENTRY POINT
# ------------------------------
if __name__ == "__main__":
    main()













































