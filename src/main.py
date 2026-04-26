
# ==============================
# main.py
# Sistema completo (Cliente, Hotel, Quarto, Reserva)
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

def menu():
    print("\n===== SISTEMA HOTEL COMPLETO =====")
    print("1 - Criar cliente      | 6  - Criar hotel       | 11 - Criar quarto      | 16 - Criar reserva")
    print("2 - Listar clientes    | 7  - Listar hotéis      | 12 - Listar quartos    | 17 - Listar reservas")
    print("3 - Consultar cliente  | 8  - Consultar hotel    | 13 - Consultar quarto   | 18 - Consultar reserva")
    print("4 - Atualizar cliente  | 9  - Atualizar hotel    | 14 - Atualizar quarto   | 19 - Atualizar reserva")
    print("5 - Remover cliente    | 10 - Remover hotel      | 15 - Remover quarto     | 20 - Remover reserva")
    print("0 - Sair")

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
            print(f"{'Sucesso' if rc[0]==201 else 'Erro'}: {rc[1]}")

        elif op == "2":
            listar_clientes()

        # ========= HOTEL =========
        elif op == "6":
            nome = input("Nome do hotel: ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            classificacao = input("Classificação: ")
            rc = criar_hotel(nome, endereco, telefone, classificacao)
            print(f"{'Sucesso' if rc[0]==201 else 'Erro'}: {rc[1]}")

        elif op == "7":
            listar_hoteis()

        # ========= QUARTO =========
        elif op == "11":
            numero = input("Número do quarto: ")
            descricao = input("Descrição: ")
            tipo = input("Tipo: ")
            preco = input("Preço: ")
            lotacao = input("Lotação: ") # Campo adicionado conforme regra
            rc = criar_quarto(numero, descricao, tipo, preco, lotacao)
            print(f"{'Sucesso' if rc[0]==201 else 'Erro'}: {rc[1]}")

        elif op == "12":
            listar_quartos()

        # ========= RESERVA =========
        elif op == "16":
            id_hotel = input("ID do Hotel: ") # Campo adicionado conforme regra
            checkin = input("Data check-in (YYYY-MM-DD): ")
            checkout = input("Data check-out (YYYY-MM-DD): ")
            quartos_ids = input("IDs dos quartos (separados por vírgula): ").replace(" ", "").split(",")
            valor = input("Valor total: ")
            status = input("Status da reserva: ") # Campo adicionado conforme regra
            
            rc = criar_reserva(id_hotel, checkin, checkout, quartos_ids, valor, status)
            print(f"{'Sucesso' if rc[0]==201 else 'Erro'}: {rc[1]}")

        elif op == "17":
            listar_reservas()

        # ========= CONSULTAS / UPDATES / REMOÇÕES (Exemplos simplificados) =========
        elif op in ["3", "8", "13", "18"]:
            id_busca = input("Introduza o ID para consultar: ")
            if op == "3": consultar_cliente(id_busca)
            if op == "8": consultar_hotel(id_busca)
            if op == "13": consultar_quarto(id_busca)
            if op == "18": consultar_reserva(id_busca)

        elif op == "14": # Exemplo Update Quarto com Lotação
            id_q = input("ID do quarto: ")
            n = input("Novo número (vazio p/ manter): ")
            d = input("Nova desc (vazio p/ manter): ")
            t = input("Novo tipo (vazio p/ manter): ")
            p = input("Novo preço (vazio p/ manter): ")
            l = input("Nova lotação (vazio p/ manter): ")
            rc = atualizar_quarto(id_q, n or None, d or None, t or None, p or None, l or None)
            print(f"{'Sucesso' if rc[0]==200 else 'Erro'}: {rc[1]}")

        elif op == "19": # Exemplo Update Reserva Completo
            id_r = input("ID da reserva: ")
            h = input("Novo Hotel ID (vazio p/ manter): ")
            ci = input("Novo Check-in (vazio p/ manter): ")
            co = input("Novo Check-out (vazio p/ manter): ")
            q = input("Novos Quartos IDs (vazio p/ manter): ")
            v = input("Novo Valor (vazio p/ manter): ")
            s = input("Novo Status (vazio p/ manter): ")
            
            list_q = q.replace(" ", "").split(",") if q else None
            rc = atualizar_reserva(id_r, h or None, ci or None, co or None, list_q, v or None, s or None)
            print(f"{'Sucesso' if rc[0]==200 else 'Erro'}: {rc[1]}")

        elif op == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida ou funcionalidade em manutenção.")

if __name__ == "__main__":
    main()























