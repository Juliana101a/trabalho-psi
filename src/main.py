
# ==============================
# main.py
# Maestro do Sistema Hoteleiro
# ==============================

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
    print("\n" + "="*60)
    print("             SISTEMA DE GESTÃO HOTELEIRA")
    print("="*60)
    print(" [1]  Novo Cliente        | [6]  Novo Hotel        | [11] Novo Quarto")
    print(" [2]  Listar Clientes     | [7]  Listar Hotéis      | [12] Listar Quartos")
    print(" [3]  Consultar Cliente   | [8]  Consultar Hotel    | [13] Consultar Quarto")
    print(" [4]  Atualizar Cliente   | [9]  Atualizar Hotel    | [14] Atualizar Quarto")
    print(" [5]  Remover Cliente     | [10] Remover Hotel      | [15] Remover Quarto")
    print("-" * 60)
    print(" [16] Nova Reserva        | [21] Registar Pagamento")
    print(" [17] Listar Reservas     | [22] Listar Pagamentos")
    print(" [18] Consultar Reserva   | [23] Consultar Pagamento")
    print(" [19] Atualizar Reserva   | [24] Atualizar Pagamento")
    print(" [20] Remover Reserva     | [25] Remover Pagamento")
    print("-" * 60)
    print(" [0]  SAIR")
    print("="*60)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        # --- SEÇÃO: CLIENTES ---
        if opcao == "1":
            n = input("Nome: ")
            ni = input("NIF: ")
            t = input("Telefone: ")
            e = input("Email: ")
            d = input("Data Nasc. (YYYY-MM-DD): ")
            status, res = criar_cliente(n, ni, t, e, d)
            print(f"\n STATUS {status}: {res}")

        elif opcao == "2":
            status, lista = listar_clientes()
            if status == 200:
                print("\n--- LISTA DE CLIENTES ---")
                for c in lista: print(c)

        elif opcao == "4":
            id_c = input("ID do Cliente: ")
            n = input("Novo Nome (Enter para manter): ")
            ni = input("Novo NIF (Enter para manter): ")
            t = input("Novo Telefone (Enter para manter): ")
            e = input("Novo Email (Enter para manter): ")
            d = input("Nova Data (Enter para manter): ")
            status, res = atualizar_cliente(id_c, n or None, ni or None, t or None, e or None, d or None)
            print(f"\n STATUS {status}: {res}")

        # --- SEÇÃO: HOTÉIS ---
        elif opcao == "6":
            n = input("Nome do Hotel: ")
            en = input("Endereço: ")
            t = input("Telefone: ")
            c = converter_para_int(input("Classificação (1-5): "))
            status, res = criar_hotel(n, en, t, c)
            print(f"\n STATUS {status}: {res}")

        elif opcao == "7":
            status, lista = listar_hoteis()
            if status == 200:
                print("\n--- LISTA DE HOTÉIS ---")
                for h in lista: print(h)

        # --- SEÇÃO: QUARTOS ---
        elif opcao == "11":
            id_h = input("ID do Hotel: ")
            num = input("Número do Quarto: ")
            des = input("Descrição: ")
            tip = input("Tipo (Ex: Suite): ")
            pre = converter_para_float(input("Preço da Diária: "))
            lot = converter_para_int(input("Lotação: "))
            status, res = criar_quarto(id_h, num, des, tip, pre, lot)
            print(f"\n STATUS {status}: {res}")

        elif opcao == "12":
            listar_quartos()

        # --- SEÇÃO: RESERVAS ---
        elif opcao == "16":
            id_h = input("ID do Hotel: ")
            id_q = input("ID do Quarto Principal: ")
            cin = input("Check-in (YYYY-MM-DD): ")
            cout = input("Check-out (YYYY-MM-DD): ")
            q_extras = input("IDs quartos extras (separados por vírgula): ").replace(" ", "").split(",")
            if q_extras == ['']: q_extras = []
            val = converter_para_float(input("Valor Total: "))
            st = input("Status (Pendente/Confirmada): ")
            status, res = criar_reserva(id_h, id_q, cin, cout, q_extras, val, st)
            print(f"\n STATUS {status}: {res}")

        elif opcao == "17":
            listar_reservas()

        # --- SEÇÃO: PAGAMENTOS ---
        elif opcao == "21":
            id_r = input("ID da Reserva: ")
            val = converter_para_float(input("Valor a Pagar: "))
            met = input("Método (Dinheiro/Cartão/MBWay): ")
            st = input("Status (Confirmado/Pendente): ")
            status, res = registrar_pagamento(id_r, val, met, st)
            print(f"\n STATUS {status}: {res}")

        elif opcao == "22":
            status, lista = listar_pagamentos()
            if status == 200:
                print("\n--- LISTA DE PAGAMENTOS ---")
                for p in lista: print(p)

        # --- SEÇÃO: CONSULTAS GERAIS ---
        elif opcao in ["3", "8", "13", "18", "23"]:
            id_busca = input("Introduza o ID para consulta: ")
            funcs = {"3": consultar_cliente, "8": consultar_hotel, "13": consultar_quarto, 
                     "18": consultar_reserva, "23": consultar_pagamento}
            status, res = funcs[opcao](id_busca)
            print(f"\n STATUS {status}: {res}")

        # --- SEÇÃO: REMOÇÕES GERAIS ---
        elif opcao in ["5", "10", "15", "20", "25"]:
            id_rem = input("Introduza o ID para remoção: ")
            funcs = {"5": remover_cliente, "10": remover_hotel, "15": remover_quarto, 
                     "20": remover_reserva, "25": remover_pagamento}
            status, res = funcs[opcao](id_rem)
            print(f"\n STATUS {status}: {res}")

        elif opcao == "0":
            print("\nA encerrar o sistema... Até breve!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
