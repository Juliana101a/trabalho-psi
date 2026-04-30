

# ==============================
# reserva.py
# Gestão de Reservas com Validação Cruzada
# ==============================

from utils import gerar_id_reserva, validar_datas_reserva
from quarto import quartos
from hotel import hoteis
from cliente import clientes

reservas = {}

# --- CREATE ---
def criar_reserva(id_hotel, id_cliente, id_quarto, data_checkin, data_checkout, lista_quartos, valor_total, status_reserva):
    # 1. REGRA: Verificar se o Cliente existe
    if id_cliente not in clientes:
        print(f"Erro: Cliente {id_cliente} não encontrado.")
        return 404, "Cliente não encontrado."

    # 2. REGRA: Verificar se o Hotel existe
    if id_hotel not in hoteis:
        print(f"Erro: Hotel {id_hotel} não encontrado.")
        return 404, "Hotel não encontrado."

    # 3. REGRA: Verificar se o Quarto Principal existe
    if id_quarto not in quartos:
        print(f"Erro: Quarto principal {id_quarto} não encontrado.")
        return 404, "Quarto principal não encontrado."

    # 4. REGRA: Verificar se todos os quartos da lista adicional existem
    for q_id in lista_quartos:
        if q_id not in quartos:
            print(f"Erro: Quarto adicional {q_id} não encontrado.")
            return 404, f"Quarto adicional {q_id} não encontrado."

    # 5. REGRA: Validação Cronológica das Datas (Check-out > Check-in)
    if not validar_datas_reserva(data_checkin, data_checkout):
        print("Erro: Datas inválidas. O check-out deve ser posterior ao check-in.")
        return 400, "Cronologia de datas inválida."

    # Se passou todas as validações, cria a reserva
    id_reserva = gerar_id_reserva()
    
    reservas[id_reserva] = {
        "id_hotel": id_hotel,
        "id_cliente": id_cliente,
        "id_quarto": id_quarto,
        "data_checkin": data_checkin,
        "data_checkout": data_checkout,
        "lista_quartos": lista_quartos,
        "valor_total": valor_total,
        "status_reserva": status_reserva
    }
    
    print(f"Reserva {id_reserva} criada com sucesso para o cliente {id_cliente}.")
    return 201, {"id_reserva": id_reserva, **reservas[id_reserva]}

# --- READ (Listar todas) ---
def listar_reservas():
    if not reservas:
        print("Não existem reservas registadas.")
        return 404, "Não existem reservas registadas."
    
    lista_formatada = [{"id_reserva": id_r, **dados} for id_r, dados in reservas.items()]
    
    for r in lista_formatada:
        print(f"ID: {r['id_reserva']} | Cliente: {r['id_cliente']} | Status: {r['status_reserva']}")
              
    return 200, lista_formatada

# --- READ (Consultar uma) ---
def consultar_reserva(id_reserva):
    if id_reserva not in reservas:
        print("Reserva não encontrada.")
        return 404, "Reserva não encontrada."
    
    dados = {"id_reserva": id_reserva, **reservas[id_reserva].copy()}
    print(dados)
    return 200, dados

# --- UPDATE ---
def atualizar_reserva(id_reserva, **kwargs):
    if id_reserva not in reservas:
        print("Reserva não encontrada.")
        return 404, "Reserva não encontrada."
    
    # Atualiza apenas os campos passados (ex: status_reserva, valor_total)
    for chave, valor in kwargs.items():
        if valor is not None:
            reservas[id_reserva][chave] = valor

    print(f"Reserva {id_reserva} atualizada.")
    return 200, {"id_reserva": id_reserva, **reservas[id_reserva]}

# --- DELETE ---
def remover_reserva(id_reserva):
    if id_reserva not in reservas:
        print("Reserva não encontrada.")
        return 404, "Reserva não encontrada."
        
    reserva_removida = reservas.pop(id_reserva)
    print(f"Reserva {id_reserva} removida com sucesso.")
    return 200, {"id_reserva": id_reserva, "status": "Removida"}




















