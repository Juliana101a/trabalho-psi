

from persistencia import guardar_dados, carregar_dados
from utils import gerar_id, agora
from logger import log_info, log_warning, log_error


def criar_pagamento(id_reserva, valor, metodo, status):
    pagamentos = carregar_dados("pagamentos.json")
    reservas = carregar_dados("reservas.json")

    if id_reserva not in reservas:
        log_error("Reserva inválida no pagamento")
        return 404, "reserva não existe"

    pid = gerar_id("P", pagamentos)

    pagamentos[pid] = {
        "id_reserva": id_reserva,
        "valor": valor,
        "metodo": metodo,
        "status": status,
        "data": agora()
    }

    guardar_dados("pagamentos.json", pagamentos)
    log_info(f"Pagamento criado: {pid}")
    return 201, pid


def listar_pagamentos():
    pagamentos = carregar_dados("pagamentos.json")
    log_info("Listagem pagamentos")
    return 200, [{"id": k, **v} for k, v in pagamentos.items()]


def consultar_pagamento(pid):
    pagamentos = carregar_dados("pagamentos.json")

    if pid not in pagamentos:
        log_warning(f"Pagamento não encontrado: {pid}")
        return 404, "não encontrado"

    log_info(f"Pagamento consultado: {pid}")
    return 200, {"id": pid, **pagamentos[pid]}


#  CORRIGIDO (EVITA ERROS DO MAIN)
def atualizar_pagamento(pid, id_reserva=None, valor=None, metodo=None, status=None):
    pagamentos = carregar_dados("pagamentos.json")

    if pid not in pagamentos:
        log_error(f"Pagamento não existe: {pid}")
        return 404, "não encontrado"

    # atualização segura (sem quebrar se vier None ou vazio)
    if id_reserva:
        pagamentos[pid]["id_reserva"] = id_reserva

    if valor is not None and valor != "":
        pagamentos[pid]["valor"] = valor

    if metodo:
        pagamentos[pid]["metodo"] = metodo

    if status:
        pagamentos[pid]["status"] = status

    guardar_dados("pagamentos.json", pagamentos)

    log_info(f"Pagamento atualizado: {pid}")
    return 200, pagamentos[pid]


#  CORRIGIDO (SEGURO MESMO SE ID NÃO EXISTIR)
def remover_pagamento(pid):
    pagamentos = carregar_dados("pagamentos.json")

    if not pid or pid not in pagamentos:
        log_warning(f"Tentativa remover pagamento inexistente: {pid}")
        return 404, "não encontrado"

    removido = pagamentos.pop(pid)

    guardar_dados("pagamentos.json", pagamentos)

    log_info(f"Pagamento removido: {pid}")
    return 200, removido




























































































