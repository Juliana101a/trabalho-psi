

# ==============================
# utils.py
# funções auxiliares unificadas
# ==============================

from datetime import datetime

# ------------------------------
# Contadores Globais para IDs
# ------------------------------
contador_cliente = 1
contador_hotel = 1
contador_id_quarto = 1
contador_id_reserva = 1

# ------------------------------
# Funções de gerar IDs
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

# ------------------------------
# Funções de validação de datas
# ------------------------------
def validar_data(data_texto):
    """Valida se a string está no formato YYYY-MM-DD"""
    try:
        datetime.strptime(data_texto, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False

def validar_data_nascimento(data_texto):
    """Valida o formato da data de nascimento"""
    return validar_data(data_texto)

def validar_datas_reserva(checkin, checkout):
    """Garante que o checkout seja posterior ao checkin"""
    if not validar_data(checkin) or not validar_data(checkout):
        return False
    
    dt_in = datetime.strptime(checkin, "%Y-%m-%d")
    dt_out = datetime.strptime(checkout, "%Y-%m-%d")
    
    return dt_out > dt_in














































