

# ==============================
# utils.py
# Motor de Identificação e Regras
# ==============================

from datetime import datetime

# Contadores para garantir IDs únicos e sequenciais
contador_cliente = 1
contador_hotel = 1
contador_id_quarto = 1
contador_id_reserva = 1
contador_id_pagamento = 1

# --- GERADORES DE ID ---
# Seguem o padrão: Letra + 00X (ex: Q001, R005)

def gerar_id_cliente():
    global contador_cliente
    novo_id = f"C{contador_cliente:03d}"
    contador_cliente += 1
    return novo_id

def gerar_id_hotel():
    global contador_hotel
    novo_id = f"H{contador_hotel:03d}"
    contador_hotel += 1
    return novo_id

def gerar_id_quarto():
    global contador_id_quarto
    novo_id = f"Q{contador_id_quarto:03d}"
    contador_id_quarto += 1
    return novo_id

def gerar_id_reserva():
    global contador_id_reserva
    novo_id = f"R{contador_id_reserva:03d}"
    contador_id_reserva += 1
    return novo_id

def gerar_id_pagamento():
    global contador_id_pagamento
    novo_id = f"P{contador_id_pagamento:03d}"
    contador_id_pagamento += 1
    return novo_id

# --- VALIDAÇÕES DE REGRAS ---

def validar_data(data_texto):
    """
    Verifica se a data está no formato correto (YYYY-MM-DD).
    Usado no Quarto (descrições temporais) e Reserva.
    """
    try:
        if not data_texto:
            return False
        datetime.strptime(data_texto, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False

def validar_datas_reserva(checkin, checkout):
    """
    REGRA CRÍTICA: O checkout tem de ser depois do checkin.
    Impede erros financeiros e de ocupação.
    """
    if not validar_data(checkin) or not validar_data(checkout):
        return False
    
    dt_in = datetime.strptime(checkin, "%Y-%m-%d")
    dt_out = datetime.strptime(checkout, "%Y-%m-%d")
    
    return dt_out > dt_in

def obter_data_hora_atual():
    """Usado para registar o momento exato do pagamento."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validar_data_nascimento(data_texto):
    """Garante que o cliente tem uma data de nascimento real."""
    return validar_data(data_texto)



































