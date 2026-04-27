
# ==============================
# main.py
# Interface do Sistema Hoteleiro
# ==============================

from cliente import *
from hotel import *
from quarto import *
from reserva import *
from pagamento import *

def exibir_menu():
    print("\n" + "="*70)
    print("                SISTEMA DE GESTÃO HOTELEIRA")
    print("="*70)
    print("  1- Criar Cliente      |  6- Criar Hotel      | 11- Criar Quarto")
    print("  2- Listar Clientes    |  7- Listar Hotéis    | 12- Listar Quartos")
    print("  3- Consultar Cliente  |  8- Consultar Hotel  | 13- Consultar Quarto")
    print("  4- Atualizar Cliente  |  9- Atualizar Hotel  | 14- Atualizar Quarto")
    print("  5- Remover Cliente    | 10- Remover Hotel    | 15- Remover Quarto")
    print("-" * 70)
    print(" 16- Criar Reserva      | 21- Registrar Pagamento")
    print(" 17- Listar Reservas    | 22- Listar Pagamentos")
    print(" 18- Consultar Reserva  | 23- Consultar Pagamento")
    print(" 19- Atualizar Reserva  | 24- Atualizar Pagamento")
    print(" 20- Remover Reserva    | 25- Remover Pagamento")
    print("-" * 70)
    print("  0- Sair")
    print("="*70)

def main():
    while True:
        exibir_menu()
        op = input("Escolha uma opção: ")

        # --- CLIENTE ---
        if op == "1":
            nome = input("Nome: ")
            nif = input("NIF: ")
            tel = input("Telefone: ")
            mail = input("Email: ")
            data = input("Data Nascimento (YYYY-MM-DD): ")
            status, msg = criar_cliente(nome, nif, tel, mail, data)
            print(f"\n[{status}] {msg}")

        elif op == "2":
            status, lista = listar_clientes()
            print(f"\nClientes: {lista}")

        # --- HOTEL ---
        elif op == "6":
            n = input("Nome do Hotel: ")
            e = input("Endereço: ")
            t = input("Telefone: ")
            c = input("Classificação (1-5): ")
            status, msg = criar_hotel(n, e, t, c)
            print(f"\n[{status}] {msg}")

        # --- QUARTO ---
        elif op == "11":
            num = input("Número do Quarto: ")
            des = input("Descrição: ")
            tip = input("Tipo: ")
            pre = float(input("Preço: "))
            lot = int(input("Lotação: "))
            status, msg = criar_quarto(num, des, tip, pre, lot)
            print(f"\n[{status}] {msg}")

        # --- RESERVA ---
        elif op == "16":
            idh = input("ID do Hotel: ")
            cin = input("Check-in (YYYY-MM-DD): ")
            out = input("Check-out (YYYY-MM-DD): ")
            q_ids = input("IDs dos Quartos (separados por vírgula): ").replace(" ", "").split(",")
            val = float(input("Valor Total: "))
            st = input("Status (Pendente/Confirmada): ")
            status, msg = criar_reserva(idh, cin, out, q_ids, val, st)
            print(f"\n[{status}] {msg}")

        # --- PAGAMENTO ---
        elif op == "21":
            idr = input("ID da Reserva: ")
            val = float(input("Valor Pago: "))
            met = input("Método (Cartão/Dinheiro): ")
            st = input("Status Pagamento (Confirmado/Pendente): ")
            status, msg = registrar_pagamento(idr, val, met, st)
            print(f"\n[{status}] {msg}")

        # --- CONSULTAS (Utilizando os IDs) ---
        elif op in ["3", "8", "13", "18", "23"]:
            idx = input("Introduza o ID: ")
            if op == "3":  print(consultar_cliente(idx))
            if op == "8":  print(consultar_hotel(idx))
            if op == "13": print(consultar_quarto(idx))
            if op == "18": print(consultar_reserva(idx))
            if op == "23": print(consultar_pagamento(idx))

        # --- REMOÇÕES ---
        elif op in ["5", "10", "15", "20", "25"]:
            idx = input("Introduza o ID para remover: ")
            if op == "5":  s, m = remover_cliente(idx)
            if op == "10": s, m = remover_hotel(idx)
            if op == "15": s, m = remover_quarto(idx)
            if op == "20": s, m = remover_reserva(idx)
            if op == "25": s, m = remover_pagamento(idx)
            print(f"\n[{s}] {m}")

        elif op == "0":
            print("A encerrar sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

