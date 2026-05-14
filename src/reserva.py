
from persistencia import guardar_dados, carregar_dados
from utils import validar_datas_reserva, validar_data

contador = 1


def gerar_id():
    global contador
    rid = f"R{contador:03d}"
    contador += 1
    return rid


def criar_reserva(id_hotel, id_quarto, checkin, checkout, extras, valor, status):
    reservas = carregar_dados("reservas.json")
    if not validar_data(checkin) or not validar_data(checkout):
        return 400, "data inválida"

    if not validar_datas_reserva(checkin, checkout):
        return 400, "intervalo inválido"

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
    reservas = carregar_dados("reservas.json")
    return 200, [{"id": k, **v} for k, v in reservas.items()]


def consultar_reserva(rid):
    reservas = carregar_dados("reservas.json")
    if rid not in reservas:
        return 404, "não encontrado"
    return 200, {"id": rid, **reservas[rid]}


def atualizar_reserva(rid, id_hotel=None, id_quarto=None, checkin=None, checkout=None, extras=None, valor=None, status=None):
    reservas = carregar_dados("reservas.json")
    if rid not in reservas:
        return 404, "não encontrado"

    if id_hotel is not None:
        reservas[rid]["id_hotel"] = id_hotel
    if id_quarto is not None:
        reservas[rid]["id_quarto"] = id_quarto
    if checkin is not None:
        reservas[rid]["checkin"] = checkin
    if checkout is not None:
        reservas[rid]["checkout"] = checkout
    if extras is not None:
        reservas[rid]["extras"] = extras
    if valor is not None:
        reservas[rid]["valor"] = valor
    if status is not None:
        reservas[rid]["status"] = status

    guardar_dados("reservas.json", reservas)
    return 200, {"id": rid, **reservas[rid]}


def remover_reserva(rid):
    reservas = carregar_dados("reservas.json")
    if rid not in reservas:
        return 404, "não encontrado"

    r = reservas.pop(rid)
    guardar_dados("reservas.json", reservas)
    return 200, r





















