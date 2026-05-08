import persistencia

from datetime import datetime

# ---------------------------------------------------------
# Contadores Globais para IDs (Persistência em memória)
# ---------------------------------------------------------
persistencia.contador_cliente = 1
persistencia.contador_hotel = 1
persistencia.contador_id_quarto = 1
persistencia.contador_id_reserva = 1
persistencia.contador_pagamento = 1

# ---------------------------------------------------------
# Funções de Geração de IDs (Padrão: Letra + 000)
# ---------------------------------------------------------
def gerar_id_cliente():

    novo_id = f"C{persistencia.contador_cliente:03d}"
    persistencia.contador_cliente += 1

    return novo_id


def gerar_id_hotel():

    novo_id = f"H{persistencia.contador_hotel:03d}"
    persistencia.contador_hotel += 1

    return novo_id


def gerar_id_quarto():

    novo_id = f"Q{persistencia.contador_id_quarto:03d}"
    persistencia.contador_id_quarto += 1

    return novo_id


def gerar_id_reserva():

    novo_id = f"R{persistencia.contador_id_reserva:03d}"
    persistencia.contador_id_reserva += 1

    return novo_id


def gerar_id_pagamento():

    novo_id = f"P{persistencia.contador_pagamento:03d}"
    persistencia.contador_pagamento += 1

    return novo_id


# ---------------------------------------------------------
# Funções de Datas e Tempo
# ---------------------------------------------------------
def validar_data(data_texto):
    """Valida se a string está no formato YYYY-MM-DD"""

    try:

        if not data_texto:
            return False

        datetime.strptime(data_texto, "%Y-%m-%d")

        return True

    except (ValueError, TypeError):

        return False


def validar_data_nascimento(data_texto):
    """Alias para validar_data usado no módulo cliente"""

    return validar_data(data_texto)


def obter_data_hora_atual():
    """Retorna data e hora atual formatada para o log de pagamentos"""

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def validar_datas_reserva(checkin, checkout):
    """Garante integridade lógica: checkout após o checkin"""

    if not validar_data(checkin) or not validar_data(checkout):
        return False

    dt_in = datetime.strptime(checkin, "%Y-%m-%d")
    dt_out = datetime.strptime(checkout, "%Y-%m-%d")

    return dt_out > dt_in


# ---------------------------------------------------------
# Funções de Conversão Segura (Evita que o main.py quebre)
# ---------------------------------------------------------
def converter_para_float(valor):
    """Converte input de texto para float com segurança"""

    try:
        return float(valor)

    except (ValueError, TypeError):
        return 0.0


def converter_para_int(valor):
    """Converte input de texto para int com segurança"""

    try:
        return int(valor)

    except (ValueError, TypeError):
        return 0


# ---------------------------------------------------------
# Atualizar contadores baseado nos JSON carregados
# ---------------------------------------------------------
def atualizar_contadores(clientes, quartos, reservas, pagamentos):

    if clientes:
        ultimo = max(int(id[1:]) for id in clientes.keys())
        persistencia.contador_cliente = ultimo + 1

    if quartos:
        ultimo = max(int(id[1:]) for id in quartos.keys())
        persistencia.contador_id_quarto = ultimo + 1

    if reservas:
        ultimo = max(int(id[1:]) for id in reservas.keys())
        persistencia.contador_id_reserva = ultimo + 1

    if pagamentos:
        ultimo = max(int(id[1:]) for id in pagamentos.keys())
        persistencia.contador_pagamento = ultimo + 1







