

# ==============================

# main_app.py
# Menu terminal para testar CRUD completo do hotel
# ==============================

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
# Menu principal
# ------------------------------
def menu():
    print("\n===== MENU HOTEL =====")
    print("1 - Criar quarto")
    print("2 - Listar quartos")
    print("3 - Consultar quarto")
    print("4 - Atualizar quarto")
    print("5 - Remover quarto")
    print("6 - Criar reserva")
    print("7 - Listar reservas")
    print("8 - Consultar reserva")
    print("9 - Atualizar reserva")
    print("10 - Remover reserva")
    print("0 - Sair")

# ------------------------------
# Programa principal
# ------------------------------
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        # ================= Quarto =================
        if opcao == "1":
            numero = input("Número do quarto: ")
            descricao = input("Descrição do quarto: ")
            tipo_quarto = input("Tipo de quarto (suite, solteiro, casal): ")
            preco = input("Preço: ")
            criar_quarto(numero, descricao, tipo_quarto, preco)

        elif opcao == "2":
            listar_quartos()

        elif opcao == "3":
            id_quarto = input("ID do quarto: ")
            consultar_quarto(id_quarto)

        elif opcao == "4":
            id_quarto = input("ID do quarto: ")
            numero = input("Novo número (enter para manter): ")
            descricao = input("Nova descrição (enter para manter): ")
            tipo_quarto = input("Novo tipo (enter para manter): ")
            preco = input("Novo preço (enter para manter): ")
            atualizar_quarto(
                id_quarto,
                numero if numero else None,
                descricao if descricao else None,
                tipo_quarto if tipo_quarto else None,
                preco if preco else None
            )

        elif opcao == "5":
            id_quarto = input("ID do quarto: ")
            remover_quarto(id_quarto)

        # ================= Reserva =================
        elif opcao == "6":
            data_checkin = input("Data check-in (YYYY-MM-DD): ")
            data_checkout = input("Data check-out (YYYY-MM-DD): ")
            lista_quartos = input("Lista de quartos (IDs separados por vírgula): ").split(",")
            valor_total = input("Valor total: ")
            criar_reserva(data_checkin, data_checkout, lista_quartos, valor_total)

        elif opcao == "7":
            listar_reservas()

        elif opcao == "8":
            id_reserva = input("ID da reserva: ")
            consultar_reserva(id_reserva)

        elif opcao == "9":
            id_reserva = input("ID da reserva: ")
            data_checkin = input("Nova data check-in (enter para manter): ")
            data_checkout = input("Nova data check-out (enter para manter): ")
            lista_quartos = input("Nova lista de quartos (IDs separados por vírgula, enter para manter): ")
            valor_total = input("Novo valor total (enter para manter): ")
            atualizar_reserva(
                id_reserva,
                data_checkin if data_checkin else None,
                data_checkout if data_checkout else None,
                lista_quartos.split(",") if lista_quartos else None,
                valor_total if valor_total else None
            )

        elif opcao == "10":
            id_reserva = input("ID da reserva: ")
            remover_reserva(id_reserva)

        elif opcao == "0":
            print("A sair...")
            break

        else:
            print("Opção inválida.")

# ------------------------------
# Entry point
# ------------------------------
if __name__ == "__main__":
    main()






























































































































































