
from datetime import datetime


def gerar_id(prefixo, dados):
    if not dados:
        return f"{prefixo}001"

    ids = []
    for k in dados.keys():
        try:
            ids.append(int(k[1:]))
        except:
            pass

    novo = max(ids) + 1 if ids else 1
    return f"{prefixo}{novo:03d}"


def validar_data(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except:
        return False


def validar_datas_reserva(checkin, checkout):
    try:
        d1 = datetime.strptime(checkin, "%Y-%m-%d")
        d2 = datetime.strptime(checkout, "%Y-%m-%d")
        return d2 > d1
    except:
        return False


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


def agora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
