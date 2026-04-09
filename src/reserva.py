

# ==============================
# reserva.py
# CRUD simples para entidade Reserva
# ==============================

from utils import gerar_id_reserva, validar_data
from quarto import quartos

reservas = {}

# CREATE
def criar_reserva(data_checkin, data_checkout, lista_quartos, valor_total):
    # validação das datas
    if not validar_data(data_checkin):
        return 500, "Data de check-in inválida, use formato YYYY-MM-DD"
    if not validar_data(data_checkout):
        return 500, "Data de check-out inválida, use formato YYYY-MM-DD"

    # validação de quartos existentes
    for q in lista_quartos:
        if q not in quartos:
            return 404, f"Quarto {q} não encontrado"

    id_reserva = gerar_id_reserva()
    reservas[id_reserva] = {
        "data_checkin": data_checkin,
        "data_checkout": data_checkout,
        "lista_quartos": lista_quartos,
        "valor_total": valor_total
    }
    print(f"Reserva criada com sucesso. ID: {id_reserva}")
    return 201, "Sucesso"

# READ (listar todos)
def listar_reservas():
    if not reservas:
        print("Não existem reservas registadas.")
        return 404, "Não existem reservas registadas."
    for id_reserva, dados in reservas.items():
        print(f"ID: {id_reserva} | Check-in: {dados['data_checkin']} | Check-out: {dados['data_checkout']} | "
              f"Quartos: {dados['lista_quartos']} | Valor: {dados['valor_total']}")
    return 200, "Sucesso"

# READ (consultar individual)
def consultar_reserva(id_reserva):
    if id_reserva not in reservas:
        print("Reserva não encontrada.")
        return 404, "Reserva não encontrada."
    print(reservas[id_reserva])
    return 200, "Sucesso"

# UPDATE
def atualizar_reserva(id_reserva, data_checkin=None, data_checkout=None, lista_quartos=None, valor_total=None):
    if id_reserva not in reservas:
        print("Reserva não encontrada.")
        return 404, "Reserva não encontrada."
    if data_checkin:
        if not validar_data(data_checkin):
            return 500, "Data de check-in inválida"
        reservas[id_reserva]["data_checkin"] = data_checkin
    if data_checkout:
        if not validar_data(data_checkout):
            return 500, "Data de check-out inválida"
        reservas[id_reserva]["data_checkout"] = data_checkout
    if lista_quartos:
        for q in lista_quartos:
            if q not in quartos:
                return 404, f"Quarto {q} não encontrado"
        reservas[id_reserva]["lista_quartos"] = lista_quartos
    if valor_total:
        reservas[id_reserva]["valor_total"] = valor_total
    print("Reserva atualizada com sucesso.")
    return 200, "Sucesso"

# DELETE
def remover_reserva(id_reserva):
    if id_reserva not in reservas:
        print("Reserva não encontrada.")
        return 404, "Reserva não encontrada"
    del reservas[id_reserva]
    print("Reserva removida com sucesso.")
    return 200, "Sucesso"






























































