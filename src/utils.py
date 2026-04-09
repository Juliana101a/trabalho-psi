

from datetime import datetime

contador_cliente = 1
contador_hotel = 1

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

def validar_data_nascimento(data_texto):
    try:
        datetime.strptime(data_texto, "%Y-%m-%d")
        return True
    except ValueError:
        return False
















# ==============================
# utils.py
# funções auxiliares unificadas
# ==============================

from datetime import datetime

# ------------------------------
# Contadores simples para IDs
# ------------------------------
contador_id_quarto = 1
contador_id_reserva = 1

# ------------------------------
# Funções de gerar IDs
# ------------------------------
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
# Função de validação de datas
# ------------------------------
def validar_data(data_texto):
    try:
        datetime.strptime(data_texto, "%Y-%m-%d")
        return True
    except ValueError:
        return False












































































