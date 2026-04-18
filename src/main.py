
# ==============================
# main.py
# Sistema completo (Cliente, Hotel, Quarto, Reserva)
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

from quarto import (
    criar_quarto,
    listar_quartos,
    consultar_quarto,
    atualizar_quarto,
    remover_quarto
)

from reserva import (
    criar_reserva,
    listar_reservas,
    consultar_reserva,
    atualizar_reserva,
    remover_reserva
)


# ------------------------------
# MENU
# ------------------------------
def menu():
    print("\n===== SISTEMA HOTEL COMPLETO =====")

    # CLIENTE
    print("1 - Criar cliente")
    print("2 - Listar clientes")
    print("3 - Consultar cliente")
    print("4 - Atualizar cliente")
    print("5 - Remover cliente")

    # HOTEL
    print("6 - Criar hotel")
    print("7 - Listar hotéis")
    print("8 - Consultar hotel")
    print("9 - Atualizar hotel")
    print("10 - Remover hotel")

    # QUARTO
    print("11 - Criar quarto")
    print("12 - Listar quartos")
    print("13 - Consultar quarto")
    print("14 - Atualizar quarto")
    print("15 - Remover quarto")

    # RESERVA
    print("16 - Criar reserva")
    print("17 - Listar reservas")
    print("18 - Consultar reserva")
    print("19 - Atualizar reserva")
    print("20 - Remover reserva")

    print("0 - Sair")


# ------------------------------
# MAIN
# ------------------------------
def main():
    while True:
        menu()
        op = input("Escolha uma opção: ")

        # ========= CLIENTE =========
        if op == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            data = input("Data nascimento (YYYY-MM-DD): ")

            rc = criar_cliente(nome, telefone, email, data)
            if rc[0] == 201:
                print("Cliente criado com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "2":
            rc = listar_clientes()
            if rc[0] == 200:
                print("Clientes listados com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "3":
            id_cliente = input("ID do cliente: ")
            rc = consultar_cliente(id_cliente)
            if rc[0] == 200:
                print("Cliente consultado com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "4":
            id_cliente = input("ID do cliente: ")

            nome = input("Novo nome (enter para manter): ")
            telefone = input("Novo telefone (enter para manter): ")
            email = input("Novo email (enter para manter): ")
            data = input("Nova data nascimento (enter para manter): ")

            rc = atualizar_cliente(
                id_cliente,
                nome if nome else None,
                telefone if telefone else None,
                email if email else None,
                data if data else None
            )

            if rc[0] == 200:
                print("Cliente atualizado com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "5":
            id_cliente = input("ID do cliente: ")
            rc = remover_cliente(id_cliente)

            if rc[0] == 200:
                print("Cliente removido com sucesso.")
            else:
                print("Erro:", rc[1])

        # ========= HOTEL =========
        elif op == "6":
            nome = input("Nome do hotel: ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            classificacao = input("Classificação: ")

            rc = criar_hotel(nome, endereco, telefone, classificacao)

            if rc[0] == 201:
                print("Hotel criado com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "7":
            rc = listar_hoteis()

            if rc[0] == 200:
                print("Hotéis listados com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "8":
            id_hotel = input("ID do hotel: ")
            rc = consultar_hotel(id_hotel)

            if rc[0] == 200:
                print("Hotel consultado com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "9":
            id_hotel = input("ID do hotel: ")

            nome = input("Novo nome (enter para manter): ")
            endereco = input("Novo endereço (enter para manter): ")
            telefone = input("Novo telefone (enter para manter): ")
            classificacao = input("Nova classificação (enter para manter): ")

            rc = atualizar_hotel(
                id_hotel,
                nome if nome else None,
                endereco if endereco else None,
                telefone if telefone else None,
                classificacao if classificacao else None
            )

            if rc[0] == 200:
                print("Hotel atualizado com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "10":
            id_hotel = input("ID do hotel: ")
            rc = remover_hotel(id_hotel)

            if rc[0] == 200:
                print("Hotel removido com sucesso.")
            else:
                print("Erro:", rc[1])

        # ========= QUARTO =========
        elif op == "11":
            numero = input("Número do quarto: ")
            descricao = input("Descrição: ")
            tipo = input("Tipo: ")
            preco = input("Preço: ")

            rc = criar_quarto(numero, descricao, tipo, preco)

            if rc[0] == 201:
                print("Quarto criado com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "12":
            rc = listar_quartos()

            if rc[0] == 200:
                print("Quartos listados com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "13":
            id_quarto = input("ID do quarto: ")
            rc = consultar_quarto(id_quarto)

            if rc[0] == 200:
                print("Quarto consultado com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "14":
            id_quarto = input("ID do quarto: ")

            numero = input("Novo número (enter para manter): ")
            descricao = input("Nova descrição (enter para manter): ")
            tipo = input("Novo tipo (enter para manter): ")
            preco = input("Novo preço (enter para manter): ")

            rc = atualizar_quarto(
                id_quarto,
                numero if numero else None,
                descricao if descricao else None,
                tipo if tipo else None,
                preco if preco else None
            )

            if rc[0] == 200:
                print("Quarto atualizado com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "15":
            id_quarto = input("ID do quarto: ")
            rc = remover_quarto(id_quarto)

            if rc[0] == 200:
                print("Quarto removido com sucesso.")
            else:
                print("Erro:", rc[1])

        # ========= RESERVA =========
        elif op == "16":
            checkin = input("Data check-in: ")
            checkout = input("Data check-out: ")
            quartos = input("IDs dos quartos (separados por vírgula): ").split(",")
            valor = input("Valor total: ")

            rc = criar_reserva(checkin, checkout, quartos, valor)

            if rc[0] == 201:
                print("Reserva criada com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "17":
            rc = listar_reservas()

            if rc[0] == 200:
                print("Reservas listadas com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "18":
            id_reserva = input("ID da reserva: ")
            rc = consultar_reserva(id_reserva)

            if rc[0] == 200:
                print("Reserva consultada com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "19":
            id_reserva = input("ID da reserva: ")

            checkin = input("Novo check-in (enter para manter): ")
            checkout = input("Novo check-out (enter para manter): ")
            quartos = input("Novos quartos (enter para manter): ")
            valor = input("Novo valor (enter para manter): ")

            rc = atualizar_reserva(
                id_reserva,
                checkin if checkin else None,
                checkout if checkout else None,
                quartos.split(",") if quartos else None,
                valor if valor else None
            )

            if rc[0] == 200:
                print("Reserva atualizada com sucesso.")
            else:
                print("Erro:", rc[1])

        elif op == "20":
            id_reserva = input("ID da reserva: ")
            rc = remover_reserva(id_reserva)

            if rc[0] == 200:
                print("Reserva removida com sucesso.")
            else:
                print("Erro:", rc[1])

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












































