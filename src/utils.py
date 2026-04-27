

# ==============================
# utils.py
# Ferramentas auxiliares e IDs
# ==============================

from datetime import datetime

# ------------------------------
# Contadores Globais
# ------------------------------
# Garantem que os IDs sejam sequenciais e únicos
contador_cliente = 1
contador_hotel = 1
contador_id_quarto = 1
contador_id_reserva = 1
contador_id_pagamento = 1

# ------------------------------
# Geradores de ID (Letra + 000)
# ------------------------------

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

# ------------------------------
# Gestão de Datas e Tempo
# ------------------------------

def obter_data_hora_atual():
    """Retorna o carimbo de data/hora para logs e pagamentos."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validar_data(data_texto):
    """Valida se a string segue o padrão YYYY-MM-DD."""
    try:
        if not data_texto:
            return False
        datetime.strptime(data_texto, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False

def validar_data_nascimento(data_texto):
    """Alias para clareza no cadastro de clientes."""
    return validar_data(data_texto)

def validar_datas_reserva(checkin, checkout):
    """Garante que o checkout seja cronologicamente posterior ao checkin."""
    if not validar_data(checkin) or not validar_data(checkout):
        return False
    
    dt_in = datetime.strptime(checkin, "%Y-%m-%d")
    dt_out = datetime.strptime(checkout, "%Y-%m-%d")
    
    return dt_out > dt_in










































