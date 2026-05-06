from cliente import (
    criar_cliente, listar_clientes, consultar_cliente,
    atualizar_cliente, remover_cliente
)
from hotel import (
    criar_hotel, listar_hoteis, consultar_hotel,
    atualizar_hotel, remover_hotel
)
from quarto import (
    criar_quarto, listar_quartos, consultar_quarto,
    atualizar_quarto, remover_quarto
)
from reserva import (
    criar_reserva, listar_reservas, consultar_reserva,
    atualizar_reserva, remover_reserva
)
from pagamento import (
    registrar_pagamento, listar_pagamentos, consultar_pagamento,
    atualizar_pagamento, remover_pagamento
)
from utils import converter_para_float, converter_para_int


def exibir_menu():
    print("\n" + "=" * 60)
    print("        SISTEMA DE GESTÃO HOTELEIRA")
    print("=" * 60)
    print(" [1] Cliente - Criar        [6] Hotel - Criar        [11] Quarto - Criar")
    print(" [2] Cliente - Listar       [7] Hotel - Listar       [12] Quarto - Listar")
    print(" [3] Cliente - Consultar    [8] Hotel - Consultar    [13] Quarto - Consultar")
    print(" [4] Cliente - Atualizar    [9] Hotel - Atualizar    [14] Quarto - Atualizar")
    print(" [5] Cliente - Remover     [10] Hotel - Remover     [15] Quarto - Remover")
    print("-" * 60)
    print(" [16] Reserva - Criar      [21] Pagamento - Registar")
    print(" [17] Reserva - Listar     [22] Pagamento - Listar")
    print(" [18] Reserva - Consultar  [23] Pagamento - Consultar")
    print(" [19] Reserva - Atualizar   [24] Pagamento - Atualizar")
    print(" [20] Reserva - Remover     [25] Pagamento - Remover")
    print("-" * 60)
    print(" [0] Sair")
    print("=" * 60)


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        # ---------------- CLIENTE ----------------
        if opcao == "1":
            status, res = criar_cliente(
                input("Nome: "),
                input("NIF: "),
                input("Telefone: "),
                input("Email: "),
                input("Data nascimento (YYYY-MM-DD): ")
            )
            print(status, res)

        elif opcao == "2":
            status, lista = listar_clientes()
            print(status)
            for c in lista:
                print(c)

        elif opcao == "3":
            status, res = consultar_cliente(input("ID Cliente: "))
            print(status, res)

        elif opcao == "4":
            status, res = atualizar_cliente(
                input("ID Cliente: "),
                input("Nome (ou Enter): ") or None,
                input("NIF (ou Enter): ") or None,
                input("Telefone (ou Enter): ") or None,
                input("Email (ou Enter): ") or None,
                input("Data nascimento (ou Enter): ") or None
            )
            print(status, res)

        elif opcao == "5":
            status, res = remover_cliente(input("ID Cliente: "))
            print(status, res)

        # ---------------- HOTEL ----------------
        elif opcao == "6":
            status, res = criar_hotel(
                input("Nome: "),
                input("Endereço: "),
                input("Telefone: "),
                converter_para_int(input("Classificação: "))
            )
            print(status, res)

        elif opcao == "7":
            status, lista = listar_hoteis()
            print(status)
            for h in lista:
                print(h)

        elif opcao == "8":
            status, res = consultar_hotel(input("ID Hotel: "))
            print(status, res)

        elif opcao == "9":
            status, res = atualizar_hotel(input("ID Hotel: "))
            print(status, res)

        elif opcao == "10":
            status, res = remover_hotel(input("ID Hotel: "))
            print(status, res)

        # ---------------- QUARTO ----------------
        elif opcao == "11":
            status, res = criar_quarto(
                input("ID Hotel: "),
                input("Número: "),
                input("Descrição: "),
                input("Tipo: "),
                converter_para_float(input("Preço: ")),
                converter_para_int(input("Lotação: "))
            )
            print(status, res)

        elif opcao == "12":
            status, lista = listar_quartos()
            print(status)
            for q in lista:
                print(q)

        elif opcao == "13":
            status, res = consultar_quarto(input("ID Quarto: "))
            print(status, res)

        elif opcao == "14":
            status, res = atualizar_quarto(input("ID Quarto: "))
            print(status, res)

        elif opcao == "15":
            status, res = remover_quarto(input("ID Quarto: "))
            print(status, res)

        # ---------------- RESERVA ----------------
        elif opcao == "16":
            status, res = criar_reserva(
                input("ID Hotel: "),
                input("ID Quarto: "),
                input("Check-in: "),
                input("Check-out: "),
                input("Quartos extras (vírgula): ").split(","),
                converter_para_float(input("Valor total: ")),
                input("Status: ")
            )
            print(status, res)

        elif opcao == "17":
            status, lista = listar_reservas()
            print(status)
            for r in lista:
                print(r)

        elif opcao == "18":
            status, res = consultar_reserva(input("ID Reserva: "))
            print(status, res)

        elif opcao == "19":
            status, res = atualizar_reserva(input("ID Reserva: "))
            print(status, res)

        elif opcao == "20":
            status, res = remover_reserva(input("ID Reserva: "))
            print(status, res)

        # ---------------- PAGAMENTO ----------------
        elif opcao == "21":
            status, res = registrar_pagamento(
                input("ID Reserva: "),
                converter_para_float(input("Valor: ")),
                input("Método: "),
                input("Status: ")
            )
            print(status, res)

        elif opcao == "22":
            status, lista = listar_pagamentos()
            print(status)
            for p in lista:
                print(p)

        elif opcao == "23":
            status, res = consultar_pagamento(input("ID Pagamento: "))
            print(status, res)

        elif opcao == "24":
            status, res = atualizar_pagamento(input("ID Pagamento: "))
            print(status, res)

        elif opcao == "25":
            status, res = remover_pagamento(input("ID Pagamento: "))
            print(status, res)

        # ---------------- SAIR ----------------
        elif opcao == "0":
            print("A encerrar sistema...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()

