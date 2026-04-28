
# ==============================
# main.py
# Interface Final do Sistema
# ==============================

from cliente import *
from hotel import *
from quarto import *
---
from reserva import *
from pagamento import *

def exibir_menu():
    print("\n" + "="*70)
    print("                SISTEMA DE GESTÃO HOTELEIRA v1.0")
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
            listar_clientes()

        # --- HOTEL ---
        elif op == "6":
            n = input("Nome do Hotel: ")
            e = input("Endereço: ")
            t = input("Telefone: ")
            c = input("Classificação (1-5): ")
            status, msg = criar_hotel(n, e, t, c)
            print(f"\n[{status}] {msg}")

        elif op == "7":
            listar_hoteis()

        # --- QUARTO ---
        elif op == "11":
            idh = input("ID do Hotel para este quarto: ")
            num = input("Número do Quarto: ")
            des = input("Descrição: ")
            tip = input("Tipo: ")
            try:
                pre = float(input("Preço por noite: "))
                lot = int(input("Lotação Máxima: "))
                status, msg = criar_quarto(num, des, tip, pre, lot, idh)
                print(f"\n[{status}] {msg}")
            except ValueError:
                print("\n[Erro] Preço e Lotação devem ser numéricos.")

        elif op == "12":
            listar_quartos()

        # --- RESERVA ---
        elif op == "16":
            print("\n--- Nova Reserva ---")
            idh = input("ID do Hotel: ")
            idc = input("ID do Cliente: ")
            idq_p = input("ID do Quarto Principal: ")
            cin = input("Check-in (YYYY-MM-DD): ")
            out = input("Check-out (YYYY-MM-DD): ")
            
            # Tratamento da lista de quartos adicionais
            q_ids_raw = input("IDs de quartos adicionais (separados por vírgula ou vazio): ")
            q_ids = [id.strip() for id in q_ids_raw.split(",") if id.strip()]
            
            try:
                val = float(input("Valor Total da Reserva: "))
                st = input("Status (Pendente/Confirmada): ")
                # Chamada com id_cliente (idc) para segurança total
                status, msg = criar_reserva(idh, idc, idq_p, cin, out, q_ids, val, st)
                print(f"\n[{status}] {msg}")
            except ValueError:
                print("\n[Erro] Valor deve ser numérico.")

        elif op == "17":
            listar_reservas()

        # --- PAGAMENTO ---
        elif op == "21":
            idr = input("ID da Reserva: ")
            try:
                val = float(input("Valor a Pagar: "))
                met = input("Método (Cartão/Dinheiro/MBWay): ")
                st = input("Status Pagamento (Confirmado/Pendente): ")
                status, msg = registrar_pagamento(idr, val, met, st)
                print(f"\n[{status}] {msg}")
            except ValueError:
                print("\n[Erro] Valor deve ser numérico.")

        elif op == "22":
            listar_pagamentos()

        # --- CONSULTAS GERAIS ---
        elif op in ["3", "8", "13", "18", "23"]:
            idx = input("Introduza o ID para consulta: ")
            if op == "3":  consultar_cliente(idx)
            if op == "8":  consultar_hotel(idx)
            if op == "13": consultar_quarto(idx)
            if op == "18": consultar_reserva(idx)
            if op == "23": consultar_pagamento(idx)

        # --- ATUALIZAÇÕES (EXEMPLO PARA CLIENTE) ---
        elif op == "4":
            idx = input("ID do Cliente a atualizar: ")
            nome = input("Novo Nome (ou vazio): ") or None
            status, msg = atualizar_cliente(idx, nome=nome)
            print(f"\n[{status}] {msg}")

        # --- REMOÇÕES ---
        elif op in ["5", "10", "15", "20", "25"]:
            idx = input("Introduza o ID para remover: ")
            if op == "5":  s, m = remover_cliente(idx)
            if op == "10": s, m = remover_hotel(idx)
            if op == "15": s, m = remover_quarto(idx)
            if op == "20": s, m = remover_reserva(idx)
            if op == "25": s, m = remover_pagamento(idx)
            print(f"\n[{s}] Operação concluída.")

        elif op == "0":
            print("\nA encerrar o sistema... Guardando dados (simulado).")
            break
        else:
            print("\n[Erro] Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
