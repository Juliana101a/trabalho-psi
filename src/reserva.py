
from persistencia import guardar_dados
from quarto import quartos
from utils import validar_data

reservas = {}
contador = 1


def gerar_id():
    global contador
    rid = f"R{contador:03d}"
    contador += 1
    return rid


def criar_reserva(id_hotel, id_quarto, checkin, checkout, extras, valor, status):
    if id_quarto not in quartos:
        return 404, "quarto não existe"

    if not validar_data(checkin) or not validar_data(checkout):
        return 400, "data inválida"

    rid = gerar_id()

    reservas[rid] = {
        "id_hotel": id_hotel,
        "id_quarto": id_quarto,
        "checkin": checkin,
        "checkout": checkout,
        "extras": extras,
        "valor": valor,
        "status": status
    }

    guardar_dados("reservas.json", reservas)
    return 201, rid


def listar_reservas():
    return 200, [{"id": k, **v} for k, v in reservas.items()]


def consultar_reserva(rid):
    if rid not in reservas:
        return 404, "não encontrado"
    return 200, {"id": rid, **reservas[rid]}


def atualizar_reserva(rid, id_hotel=None, id_quarto=None, checkin=None, checkout=None, extras=None, valor=None, status=None):
    if rid not in reservas:
        return 404, "não encontrado"

    if id_hotel: reservas[rid]["id_hotel"] = id_hotel
    if id_quarto: reservas[rid]["id_quarto"] = id_quarto
    if checkin: reservas[rid]["checkin"] = checkin
    if checkout: reservas[rid]["checkout"] = checkout
    if extras is not None: reservas[rid]["extras"] = extras
    if valor is not None: reservas[rid]["valor"] = valor
    if status: reservas[rid]["status"] = status

    guardar_dados("reservas.json", reservas)
    return 200, rid


def remover_reserva(rid):
    if rid not in reservas:
        return 404, "não encontrado"

    r = reservas.pop(rid)
    guardar_dados("reservas.json", reservas)
    return 200, r







