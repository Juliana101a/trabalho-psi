# ==============================
# pagamento.py
# CRUD para controle financeiro
# ==============================

from utils import gerar_id_pagamento, obter_data_hora_atual
from reserva import reservas

pagamentos = {}

# --- CREATE ---
def registrar_pagamento(id_reserva, valor_pago, metodo_pagamento, status_pagamento):

    if id_reserva not in reservas:
        return 404, "Erro: A reserva informada não existe."

    if valor_pago <= 0:
        return 400, "Erro: O valor do pagamento deve ser superior a zero."

    id_pagamento = gerar_id_pagamento()
    data_hora = obter_data_hora_atual()

    pagamentos[id_pagamento] = {
        "id_reserva": id_reserva,
        "data_pagamento": data_hora,
        "valor_pago": valor_pago,
        "metodo_pagamento": metodo_pagamento,
        "status_pagamento": status_pagamento
    }

    if status_pagamento.lower() == "confirmado":
        reservas[id_reserva]["status_reserva"] = "Paga"

    print(f"[LOG] Pagamento {id_pagamento} registado com sucesso.")
    return 201, id_pagamento


# --- READ (LISTAR) ---
def listar_pagamentos():

    if not pagamentos:
        return 200, []

    lista_formatada = [
        {"id_pagamento": id_p, **dados}
        for id_p, dados in pagamentos.items()
    ]

    return 200, lista_formatada


# --- READ (CONSULTAR UM) ---
def consultar_pagamento(id_pagamento):

    if id_pagamento not in pagamentos:
        return 404, "Erro: Pagamento não encontrado."

    return 200, pagamentos[id_pagamento]


# --- UPDATE ---
def atualizar_pagamento(id_pagamento, valor_pago=None, metodo_pagamento=None, status_pagamento=None):

    if id_pagamento not in pagamentos:
        return 404, "Erro: Pagamento não encontrado."

    if valor_pago is not None:
        if valor_pago <= 0:
            return 400, "Erro: O valor deve ser superior a zero."
        pagamentos[id_pagamento]["valor_pago"] = valor_pago

    if metodo_pagamento is not None:
        pagamentos[id_pagamento]["metodo_pagamento"] = metodo_pagamento

    if status_pagamento is not None:
        pagamentos[id_pagamento]["status_pagamento"] = status_pagamento

        if status_pagamento.lower() == "confirmado":
            res_id = pagamentos[id_pagamento]["id_reserva"]
            if res_id in reservas:
                reservas[res_id]["status_reserva"] = "Paga"

    print(f"[LOG] Pagamento {id_pagamento} atualizado.")
    return 200, id_pagamento


# --- DELETE ---
def remover_pagamento(id_pagamento):

    if id_pagamento not in pagamentos:
        return 404, "Erro: Impossível remover registro inexistente."

    dados_removidos = pagamentos.pop(id_pagamento)

    # segurança: só mexe na reserva se existir
    id_reserva = dados_removidos["id_reserva"]
    if id_reserva in reservas:
        reservas[id_reserva]["status_reserva"] = "Pendente"

    print(f"[LOG] Pagamento {id_pagamento} removido do sistema.")

    return 200, id_pagamento
