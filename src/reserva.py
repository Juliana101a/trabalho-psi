
from persistencia import guardar_dados, carregar_dados
from utils import validar_data, validar_datas_reserva, gerar_id
from logger import log_info, log_warning, log_error


def criar_reserva(id_hotel, id_quarto, checkin, checkout, extras, valor, status):
    reservas = carregar_dados("reservas.json")
    hoteis = carregar_dados("hoteis.json")
    quartos = carregar_dados("quartos.json")

    if id_hotel not in hoteis:
        log_warning("Hotel inválido reserva")
        return 404, "hotel não existe"

    if id_quarto not in quartos:
        log_warning("Quarto inválido reserva")
        return 404, "quarto não existe"

    if quartos[id_quarto]["id_hotel"] != id_hotel:
        log_error("Quarto não pertence ao hotel")
        return 400, "inconsistência"

    if not validar_data(checkin) or not validar_data(checkout):
        log_error("Data inválida reserva")
        return 400, "data inválida"

    if not validar_datas_reserva(checkin, checkout):
        log_error("Intervalo inválido reserva")
        return 400, "intervalo inválido"

    rid = gerar_id("R", reservas)

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
    log_info(f"Reserva criada: {rid}")
    return 201, rid


def listar_reservas():
    reservas = carregar_dados("reservas.json")
    log_info("Listagem reservas")
    return 200, [{"id": k, **v} for k, v in reservas.items()]


def consultar_reserva(rid):
    reservas = carregar_dados("reservas.json")

    if rid not in reservas:
        log_warning(f"Reserva não encontrada: {rid}")
        return 404, "não encontrado"

    log_info(f"Reserva consultada: {rid}")
    return 200, {"id": rid, **reservas[rid]}


def atualizar_reserva(rid, id_hotel=None, id_quarto=None, checkin=None, checkout=None, extras=None, valor=None, status=None):
    reservas = carregar_dados("reservas.json")

    if rid not in reservas:
        log_error(f"Atualização reserva falhou: {rid}")
        return 404, "não encontrado"

    if id_hotel: reservas[rid]["id_hotel"] = id_hotel
    if id_quarto: reservas[rid]["id_quarto"] = id_quarto
    if checkin: reservas[rid]["checkin"] = checkin
    if checkout: reservas[rid]["checkout"] = checkout
    if extras is not None: reservas[rid]["extras"] = extras
    if valor is not None: reservas[rid]["valor"] = valor
    if status: reservas[rid]["status"] = status

    guardar_dados("reservas.json", reservas)
    log_info(f"Reserva atualizada: {rid}")
    return 200, rid


def remover_reserva(rid):
    reservas = carregar_dados("reservas.json")

    if rid not in reservas:
        log_warning(f"Reserva inexistente: {rid}")
        return 404, "não encontrado"

    r = reservas.pop(rid)
    guardar_dados("reservas.json", reservas)

    log_info(f"Reserva removida: {rid}")
    return 200, r
























