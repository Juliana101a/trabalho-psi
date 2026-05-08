# ==============================
# reserva.py
# CRUD simples para entidade Reserva
# ==============================

from utils import gerar_id_reserva, validar_data
from quarto import quartos
from persistencia import guardar_dados

reservas = {}


# CREATE
def criar_reserva(id_hotel, id_quarto, data_checkin, data_checkout, lista_quartos, valor_total, status_reserva):

    # validação de datas
    if not validar_data(data_checkin):
        return 400, "Data de check-in inválida (YYYY-MM-DD)"

    if not validar_data(data_checkout):
        return 400, "Data de check-out inválida (YYYY-MM-DD)"

    # validação de quartos
    if id_quarto not in quartos:
        return 404, "Quarto principal não encontrado"

    for q in lista_quartos:
        if q not in quartos:
            return 404, f"Quarto {q} não encontrado"

    id_reserva = gerar_id_reserva()

    reservas[id_reserva] = {
        "id_hotel": id_hotel,
        "id_quarto": id_quarto,
        "data_checkin": data_checkin,
        "data_checkout": data_checkout,
        "lista_quartos": lista_quartos,
        "valor_total": valor_total,
        "status_reserva": status_reserva
    }

    guardar_dados("reservas.json", reservas)

    return 201, id_reserva


# READ (listar todos)
def listar_reservas():

    if not reservas:
        return 200, []

    lista_formatada = [
        {"id_reserva": id_r, **dados}
        for id_r, dados in reservas.items()
    ]

    return 200, lista_formatada


# READ (consultar uma)
def consultar_reserva(id_reserva):

    if id_reserva not in reservas:
        return 404, "Reserva não encontrada"

    return 200, {"id_reserva": id_reserva, **reservas[id_reserva]}


# UPDATE
def atualizar_reserva(id_reserva, id_hotel=None, id_quarto=None,
                      data_checkin=None, data_checkout=None,
                      lista_quartos=None, valor_total=None,
                      status_reserva=None):

    if id_reserva not in reservas:
        return 404, "Reserva não encontrada"

    if id_hotel is not None:
        reservas[id_reserva]["id_hotel"] = id_hotel

    if id_quarto is not None:
        if id_quarto not in quartos:
            return 404, "Quarto não encontrado"
        reservas[id_reserva]["id_quarto"] = id_quarto

    if data_checkin is not None:
        if not validar_data(data_checkin):
            return 400, "Data de check-in inválida"
        reservas[id_reserva]["data_checkin"] = data_checkin

    if data_checkout is not None:
        if not validar_data(data_checkout):
            return 400, "Data de check-out inválida"
        reservas[id_reserva]["data_checkout"] = data_checkout

    if lista_quartos is not None:
        for q in lista_quartos:
            if q not in quartos:
                return 404, f"Quarto {q} não encontrado"
        reservas[id_reserva]["lista_quartos"] = lista_quartos

    if valor_total is not None:
        reservas[id_reserva]["valor_total"] = valor_total

    if status_reserva is not None:
        reservas[id_reserva]["status_reserva"] = status_reserva

    guardar_dados("reservas.json", reservas)

    return 200, id_reserva


# DELETE
def remover_reserva(id_reserva):

    if id_reserva not in reservas:
        return 404, "Reserva não encontrada"

    reservas.pop(id_reserva)

    guardar_dados("reservas.json", reservas)

    return 200, id_reserva




