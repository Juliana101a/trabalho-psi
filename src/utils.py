
from datetime import datetime
import persistencia


# ------------------ CONTADORES ------------------
persistencia.contador_cliente = 1
persistencia.contador_hotel = 1
persistencia.contador_quarto = 1
persistencia.contador_reserva = 1
persistencia.contador_pagamento = 1


# ------------------ IDS ------------------
def gerar_id_cliente():
    cid = f"C{persistencia.contador_cliente:03d}"
    persistencia.contador_cliente += 1
    return cid


def gerar_id_hotel():
    hid = f"H{persistencia.contador_hotel:03d}"
    persistencia.contador_hotel += 1
    return hid


def gerar_id_quarto():
    qid = f"Q{persistencia.contador_quarto:03d}"
    persistencia.contador_quarto += 1
    return qid


def gerar_id_reserva():
    rid = f"R{persistencia.contador_reserva:03d}"
    persistencia.contador_reserva += 1
    return rid


def gerar_id_pagamento():
    pid = f"P{persistencia.contador_pagamento:03d}"
    persistencia.contador_pagamento += 1
    return pid


# ------------------ VALIDAÇÃO ------------------
def validar_data(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except:
        return False


def validar_datas_reserva(checkin, checkout):
    try:
        dt1 = datetime.strptime(checkin, "%Y-%m-%d")
        dt2 = datetime.strptime(checkout, "%Y-%m-%d")
        return dt2 > dt1
    except:
        return False


# ------------------ CONVERSÃO ------------------
def converter_float(v):
    try:
        return float(v)
    except:
        return 0.0


def converter_int(v):
    try:
        return int(v)
    except:
        return 0


# ------------------ DATA/HORA ------------------
def agora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ------------------ CONTADORES JSON ------------------
def atualizar_contadores(clientes, quartos, reservas, pagamentos):

    if clientes:
        persistencia.contador_cliente = max(int(i[1:]) for i in clientes) + 1

    if quartos:
        persistencia.contador_quarto = max(int(i[1:]) for i in quartos) + 1

    if reservas:
        persistencia.contador_reserva = max(int(i[1:]) for i in reservas) + 1

    if pagamentos:
        persistencia.contador_pagamento = max(int(i[1:]) for i in pagamentos) + 1









