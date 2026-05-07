# ==============================
# quarto.py
# CRUD simples para entidade Quarto
# ==============================

from utils import gerar_id_quarto

quartos = {}

# CREATE
def criar_quarto(id_hotel, numero, descricao, tipo_quarto, preco, lotacao):

    id_quarto = gerar_id_quarto()

    quartos[id_quarto] = {
        "id_hotel": id_hotel,
        "numero": numero,
        "descricao": descricao,
        "tipo_quarto": tipo_quarto,
        "preco": preco,
        "lotacao": lotacao
    }

    return 201, id_quarto


# READ (listar todos)
def listar_quartos():

    if not quartos:
        return 200, []

    lista_formatada = [
        {"id_quarto": id_q, **dados}
        for id_q, dados in quartos.items()
    ]

    return 200, lista_formatada


# READ (consultar um)
def consultar_quarto(id_quarto):

    if id_quarto not in quartos:
        return 404, "Quarto não encontrado."

    return 200, quartos[id_quarto]


# UPDATE
def atualizar_quarto(id_quarto, id_hotel=None, numero=None, descricao=None,
                     tipo_quarto=None, preco=None, lotacao=None):

    if id_quarto not in quartos:
        return 404, "Quarto não encontrado."

    if id_hotel is not None:
        quartos[id_quarto]["id_hotel"] = id_hotel
    if numero is not None:
        quartos[id_quarto]["numero"] = numero
    if descricao is not None:
        quartos[id_quarto]["descricao"] = descricao
    if tipo_quarto is not None:
        quartos[id_quarto]["tipo_quarto"] = tipo_quarto
    if preco is not None:
        quartos[id_quarto]["preco"] = preco
    if lotacao is not None:
        quartos[id_quarto]["lotacao"] = lotacao

    return 200, id_quarto


# DELETE
def remover_quarto(id_quarto):

    if id_quarto not in quartos:
        return 404, "Quarto não encontrado."

    quartos.pop(id_quarto)

    return 200, id_quarto


