

# ==============================
# reserva.py
# CRUD simples para entidade Reserva
# ==============================

from utils import gerar_id_reserva, validar_data
from quarto import quartos

reservas = {}

# CREATE
def criar_reserva(id_hotel, data_checkin, data_checkout, lista_quartos, valor_total, status_reserva):
    # validação das datas
    if not validar_data(data_checkin):
        return 500, "Data de check-in inválida, use formato YYYY-MM-DD"
    if not validar_data(data_checkout):
        return 500, "Data de check-out inválida, use formato YYYY-MM-DD"

    # validação de quartos existentes
    for q in lista_quartos:
        if q not in quartos:
            return 404, f"Quarto {q} não encontrado"

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

# READ (listar todos)
def listar_reservas():
    if not reservas:
        print("Não existem reservas registadas.")
        return 404, "Não existem reservas registadas."
    
    lista_formatada = [{"id_reserva": id_r, **dados} for id_r, dados in reservas.items()]
    
    for r in lista_formatada:
        print(f"ID: {r['id_reserva']} | Hotel: {r['id_hotel']} | Check-in: {r['data_checkin']} | "
              f"Status: {r['status_reserva']} | Valor: {r['valor_total']}")
              
    return 200, lista_formatada

# READ (consultar individual)
def consultar_reserva(id_reserva):
    if id_reserva not in reservas:
        print("Reserva não encontrada.")
        return 404, "Reserva não encontrada."
    
    dados = {"id_reserva": id_reserva, **reservas[id_reserva].copy()}
    print(dados)
    return 200, dados

# UPDATE
def atualizar_reserva(id_reserva, id_hotel=None, data_checkin=None, data_checkout=None, lista_quartos=None, valor_total=None, status_reserva=None):
    if id_reserva not in reservas:
        print("Reserva não encontrada.")
        return 404, "Reserva não encontrada."
    
    if id_hotel is not None:
        reservas[id_reserva]["id_hotel"] = id_hotel
    
    if data_checkin:
        if not validar_data(data_checkin):
            return 500, "Data de check-in inválida"
        reservas[id_reserva]["data_checkin"] = data_checkin
        
    if data_checkout:
        if not validar_data(data_checkout):
            return 500, "Data de check-out inválida"
        reservas[id_reserva]["data_checkout"] = data_checkout
        
    if lista_quartos:
        for q in lista_quartos:
            if q not in quartos:
                return 404, f"Quarto {q} não encontrado"
        reservas[id_reserva]["lista_quartos"] = lista_quartos
        
    if valor_total is not None:
        reservas[id_reserva]["valor_total"] = valor_total
        
    if status_reserva is not None:
        reservas[id_reserva]["status_reserva"] = status_reserva

    print("Reserva atualizada com sucesso.")
    return 200, {"id_reserva": id_reserva, **reservas[id_reserva].copy()}

# DELETE
def remover_reserva(id_reserva):
    if id_reserva not in reservas:
        print("Reserva não encontrada.")
        return 404, "Reserva não encontrada"
        
    reserva_removida = reservas.pop(id_reserva)
    print("Reserva removida com sucesso.")
    return 200, {"id_reserva": id_reserva, "reserva_removida": reserva_removida}




















































