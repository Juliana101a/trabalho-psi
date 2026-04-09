

# ==============================
# quarto.py
# CRUD simples para entidade Quarto
# ==============================

from utils import gerar_id_quarto

quartos = {}

# CREATE
def criar_quarto(numero, descricao, tipo_quarto, preco):
    id_quarto = gerar_id_quarto()
    quartos[id_quarto] = {
        "numero": numero,
        "descricao": descricao,
        "tipo_quarto": tipo_quarto,
        "preco": preco
    }
    print(f"Quarto criado com sucesso. ID: {id_quarto}")
    return 201, "Sucesso"

# READ (listar todos)
def listar_quartos():
    if not quartos:
        print("Não existem quartos registados.")
        return 404, "Não existem quartos registados."
    for id_quarto, dados in quartos.items():
        print(f"ID: {id_quarto} | Nº: {dados['numero']} | Descrição: {dados['descricao']} | "
              f"Tipo: {dados['tipo_quarto']} | Preço: {dados['preco']}")
    return 200, "Sucesso"

# READ (consultar individual)
def consultar_quarto(id_quarto):
    if id_quarto not in quartos:
        print("Quarto não encontrado.")
        return 404, "Quarto não encontrado."
    print(quartos[id_quarto])
    return 200, "Sucesso"

# UPDATE
def atualizar_quarto(id_quarto, numero=None, descricao=None, tipo_quarto=None, preco=None):
    if id_quarto not in quartos:
        print("Quarto não encontrado.")
        return 404, "Quarto não encontrado."
    if numero:
        quartos[id_quarto]["numero"] = numero
    if descricao:
        quartos[id_quarto]["descricao"] = descricao
    if tipo_quarto:
        quartos[id_quarto]["tipo_quarto"] = tipo_quarto
    if preco:
        quartos[id_quarto]["preco"] = preco
    print("Quarto atualizado com sucesso.")
    return 200, "Sucesso"

# DELETE
def remover_quarto(id_quarto):
    if id_quarto not in quartos:
        print("Quarto não encontrado.")
        return 404, "Quarto não encontrado"
    del quartos[id_quarto]
    print("Quarto removido com sucesso.")
    return 200, "Sucesso"
























































