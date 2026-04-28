
# ==============================
# reserva.py
# CRUD e Gestão de Reservas
# ==============================

from utils import gerar_id_reserva, validar_data
from quarto import quartos
from hotel import hoteis  # Importação para validar a existência do hotel

reservas = {}

# CREATE
def criar_reserva(id_hotel, data_checkin, data_checkout, lista_quartos, valor_total, status_reserva):
    # REGRA: Verificar se o hotel existe
    if id_hotel not in hoteis:
        print(f"Erro: Hotel {id_hotel} não encontrado.")
        return 404, "Hotel não encontrado."

    # REGRA: Validação das datas
    if not validar_data(data_checkin):
        return 500, "Data de check-in inválida, use formato YYYY-MM-DD"
    if not validar_data(data_checkout):
        return 500, "Data de check-out inválida, use formato YYYY-MM-DD"

    # REGRA: Verificar se cada quarto na lista existe no sistema
    for q_id in lista_quartos:
        if q_id not in quartos:
            print(f"Erro: Quarto {q_id} não encontrado.")
            return 404, f"Quarto {q_id} não encontrado."

    id_reserva = gerar_id_reserva()
    
    reservas[id_reserva] = {
        "id_hotel": id_hotel,
        "data_checkin": data_checkin,
        "data_checkout": data_checkout,
        "lista_quartos": lista_quartos,
        "valor_total": valor_total,
        "status_reserva": status_reserva
    }
    
    print(f"Reserva criada com sucesso. ID: {id_reserva}")
    return 201, {"id_reserva": id_reserva, **reservas[id_reserva]}

# READ (listar todas)
def listar_reservas():
    if not reservas:
        print("Não existem reservas registadas.")
        return 404, "Não existem reservas registadas."
    
    lista_formatada = [{"id_reserva": id_r, **dados} for id_r, dados in reservas.items()]
    
    for r in lista_formatada:
        print(f"ID: {r['id_reserva']} | Hotel: {r['id_hotel']} | Status: {r['status_reserva']}")
              
    return 200, lista_formatada

# READ (consultar individual)
def consultar_reserva(id_reserva):
    # REGRA: Verificar se a reserva existe
    if id_reserva not in reservas:
        print("Reserva não encontrada.")
        return 404, "Reserva não encontrada."
    
    dados = {"id_reserva": id_reserva, **reservas[id_reserva].copy()}
    print(dados)
    return 200, dados

# UPDATE
def atualizar_reserva(id_reserva, id_hotel=None, data_checkin=None, data_checkout=None, lista_quartos=None, valor_total=None, status_reserva=None):
    # REGRA: Verificar se a reserva existe
    if id_reserva not in reservas:
        print("Reserva não encontrada.")
        return 404, "Reserva não encontrada."
    
    # REGRA: Se mudar o hotel, verificar se o novo existe
    if id_hotel is not None:
        if id_hotel not in hoteis:
            return 404, "Hotel de destino não existe."
        reservas[id_reserva]["id_hotel"] = id_hotel
    
    # Validação de Datas no Update
    if data_checkin:
        if not validar_data(data_checkin):
            return 500, "Data de check-in inválida"
        reservas[id_reserva]["data_checkin"] = data_checkin
        
    if data_checkout:
        if not validar_data(data_checkout):
            return 500, "Data de check-out inválida"
        reservas[id_reserva]["data_checkout"] = data_checkout
        
    # REGRA: Se mudar a lista de quartos, verificar se todos os novos existem
    if lista_quartos:
        for q_id in lista_quartos:
            if q_id not in quartos:
                return 404, f"Quarto {q_id} não encontrado"
        reservas[id_reserva]["lista_quartos"] = lista_quartos
        
    if valor_total is not None:
        reservas[id_reserva]["valor_total"] = valor_total
        
    if status_reserva is not None:
        reservas[id_reserva]["status_reserva"] = status_reserva

    print("Reserva atualizada com sucesso.")
    return 200, {"id_reserva": id_reserva, **reservas[id_reserva].copy()}

# DELETE
def remover_reserva(id_reserva):
    # REGRA: Verificar se a reserva existe
    if id_reserva not in reservas:
        print("Reserva não encontrada.")
        return 404, "Reserva não encontrada."
        
    reserva_removida = reservas.pop(id_reserva)
    print("Reserva removida com sucesso.")
    return 200, {"id_reserva": id_reserva, "reserva_removida": reserva_removida}






































