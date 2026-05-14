
from datetime import datetime


# ------------------ CONTADORES ------------------
contadores = {
    "cliente": 1,
    "hotel": 1,
    "quarto": 1,
    "reserva": 1,
    "pagamento": 1
}


# ------------------ IDS ------------------
def gerar_id_cliente():
    cid = f"C{contadores['cliente']:03d}"
    contadores['cliente'] += 1
    return cid


def gerar_id_hotel():
    hid = f"H{contadores['hotel']:03d}"
    contadores['hotel'] += 1
    return hid


def gerar_id_quarto():
    qid = f"Q{contadores['quarto']:03d}"
    contadores['quarto'] += 1
    return qid


def gerar_id_reserva():
    rid = f"R{contadores['reserva']:03d}"
    contadores['reserva'] += 1
    return rid


def gerar_id_pagamento():
    pid = f"P{contadores['pagamento']:03d}"
    contadores['pagamento'] += 1
    return pid


# ------------------ VALIDAÇÃO ------------------
def validar_data(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validar_datas_reserva(checkin, checkout):
    try:
        dt1 = datetime.strptime(checkin, "%Y-%m-%d")
        dt2 = datetime.strptime(checkout, "%Y-%m-%d")
        return dt2 > dt1
    except ValueError:
        return False


# ------------------ CONVERSÃO ------------------
def converter_float(v):
    try:
        return float(v)
    except (ValueError, TypeError):
        return 0.0


def converter_int(v):
    try:
        return int(v)
    except (ValueError, TypeError):
        return 0


# ------------------ DATA/HORA ------------------
def agora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")