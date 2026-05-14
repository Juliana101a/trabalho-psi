

from persistencia import guardar_dados, carregar_dados
from utils import agora

pagamentos = carregar_dados("pagamentos.json")
contador = 1


def gerar_id():
    global contador
    pid = f"P{contador:03d}"
    contador += 1
    return pid


def criar_pagamento(id_reserva, valor, metodo, status):
    pid = gerar_id()

    pagamentos[pid] = {
        "id_reserva": id_reserva,
        "valor": valor,
        "metodo": metodo,
        "status": status,
        "data": agora()
    }

    guardar_dados("pagamentos.json", pagamentos)
    return 201, pid


def listar_pagamentos():
    return 200, [{"id": k, **v} for k, v in pagamentos.items()]


def consultar_pagamento(pid):
    if pid not in pagamentos:
        return 404, "não encontrado"
    return 200, {"id": pid, **pagamentos[pid]}


def atualizar_pagamento(pid, id_reserva=None, valor=None, metodo=None, status=None):
    if pid not in pagamentos:
        return 404, "não encontrado"

    if id_reserva is not None:
        pagamentos[pid]["id_reserva"] = id_reserva
    if valor is not None:
        pagamentos[pid]["valor"] = valor
    if metodo is not None:
        pagamentos[pid]["metodo"] = metodo
    if status is not None:
        pagamentos[pid]["status"] = status

    guardar_dados("pagamentos.json", pagamentos)
    return 200, {"id": pid, **pagamentos[pid]}


def remover_pagamento(pid):
    if pid not in pagamentos:
        return 404, "não encontrado"

    r = pagamentos.pop(pid)
    guardar_dados("pagamentos.json", pagamentos)
    return 200, {"removido": r}





































