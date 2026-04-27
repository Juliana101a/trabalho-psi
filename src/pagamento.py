
# ==============================
# pagamento.py
# CRUD para controle financeiro
# ==============================

from utils import gerar_id_pagamento, obter_data_hora_atual
from reserva import reservas

# Dicionário global para persistência em memória
pagamentos = {}

# --- CREATE ---
def registrar_pagamento(id_reserva, valor_pago, metodo_pagamento, status_pagamento):
    """
    Regra: Um pagamento só nasce se a reserva existir e o valor for real.
    """
    # 1. Validação de Integridade (Cama arrumada: nada fora do lugar)
    if id_reserva not in reservas:
        return 404, "Erro: A reserva informada não existe."

    if valor_pago <= 0:
        return 400, "Erro: O valor do pagamento deve ser superior a zero."

    # 2. Geração de Dados Automáticos
    id_pagamento = gerar_id_pagamento()
    data_hora = obter_data_hora_atual()

    # 3. Armazenamento Organizado
    pagamentos[id_pagamento] = {
        "id_reserva": id_reserva,
        "data_pagamento": data_hora,
        "valor_pago": valor_pago,
        "metodo_pagamento": metodo_pagamento,
        "status_pagamento": status_pagamento
    }

    # 4. Sincronização (Regra de Ouro: Ação e Reação)
    # Se o pagamento for 'confirmado', atualizamos o status da reserva automaticamente
    if status_pagamento.lower() == "confirmado":
        reservas[id_reserva]["status_reserva"] = "Paga"

    print(f"[LOG] Pagamento {id_pagamento} registado com sucesso.")
    return 201, {"id_pagamento": id_pagamento, **pagamentos[id_pagamento]}


# --- READ (Listar todos) ---
def listar_pagamentos():
    if not pagamentos:
        return 200, [] # Retorna lista vazia, mantendo o fluxo limpo

    lista_formatada = [{"id_pagamento": id_p, **dados} for id_p, dados in pagamentos.items()]
    return 200, lista_formatada


# --- READ (Consultar um) ---
def consultar_pagamento(id_pagamento):
    if id_pagamento not in pagamentos:
        return 404, "Erro: Pagamento não encontrado."

    return 200, {"id_pagamento": id_pagamento, **pagamentos[id_pagamento].copy()}


# --- UPDATE ---
def atualizar_pagamento(id_pagamento, valor_pago=None, metodo_pagamento=None, status_pagamento=None):
    """
    Regra: Atualiza apenas o que for enviado, mantendo o resto intacto.
    """
    if id_pagamento not in pagamentos:
        return 404, "Erro: Pagamento não encontrado."

    # Atualização cirúrgica
    if valor_pago is not None:
        pagamentos[id_pagamento]["valor_pago"] = valor_pago

    if metodo_pagamento is not None:
        pagamentos[id_pagamento]["metodo_pagamento"] = metodo_pagamento

    if status_pagamento is not None:
        pagamentos[id_pagamento]["status_pagamento"] = status_pagamento
        # Re-sincronização com a reserva
        if status_pagamento.lower() == "confirmado":
            res_id = pagamentos[id_pagamento]["id_reserva"]
            reservas[res_id]["status_reserva"] = "Paga"

    print(f"[LOG] Pagamento {id_pagamento} atualizado.")
    return 200, {"id_pagamento": id_pagamento, **pagamentos[id_pagamento].copy()}


# --- DELETE ---
def remover_pagamento(id_pagamento):
    if id_pagamento not in pagamentos:
        return 404, "Erro: Impossível remover registro inexistente."

    dados_removidos = pagamentos.pop(id_pagamento)
    print(f"[LOG] Pagamento {id_pagamento} removido do sistema.")

    return 200, {
        "id_pagamento": id_pagamento,
        "status": "Removido",
        "detalhes": dados_removidos
    }









































































































