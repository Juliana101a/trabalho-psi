
# ==============================
# quarto.py
# CRUD e Gestão de Disponibilidade
# ==============================

from utils import gerar_id_quarto
from hotel import hoteis  # Importação necessária para validar se o hotel existe

quartos = {}

# CREATE
def criar_quarto(numero, descricao, tipo_quarto, preco, lotacao, id_hotel):
    # REGRA: Verificar se o hotel existe antes de criar o quarto
    if id_hotel not in hoteis:
        print(f"Erro: Hotel {id_hotel} não encontrado.")
        return 404, "Hotel não encontrado."

    id_quarto = gerar_id_quarto()

    quartos[id_quarto] = {
        "id_hotel": id_hotel, # Adicionado conforme solicitado
        "numero": numero,
        "descricao": descricao,
        "tipo_quarto": tipo_quarto,
        "preco": preco,
        "lotacao": lotacao,
        "id_hotel": id_hotel
    }

    print(f"Quarto criado com sucesso. ID: {id_quarto}")
    return 201, {"id_quarto": id_quarto, **quartos[id_quarto]}

# READ (listar todos)
def listar_quartos():
    if not quartos:
        print("Não existem quartos registados.")
        return 404, "Não existem quartos registados."

    lista_formatada = [{"id_quarto": id_q, **dados} for id_q, dados in quartos.items()]

    for q in lista_formatada:
        print(f"ID: {q['id_quarto']} | Hotel: {q['id_hotel']} | Nº: {q['numero']} | Tipo: {q['tipo_quarto']}")

    return 200, lista_formatada

# READ (consultar individual)
def consultar_quarto(id_quarto):
    # REGRA: Verificar se o quarto existe
    if id_quarto not in quartos:
        print("Quarto não encontrado.")
        return 404, "Quarto não encontrado."

    dados = {"id_quarto": id_quarto, **quartos[id_quarto].copy()}
    print(dados)
    return 200, dados

# UPDATE
def atualizar_quarto(id_quarto, numero=None, descricao=None, tipo_quarto=None, preco=None, lotacao=None, id_hotel=None):
    # REGRA: Verificar se o quarto existe
    if id_quarto not in quartos:
        print("Quarto não encontrado.")
        return 404, "Quarto não encontrado."

    # REGRA: Se houver mudança de hotel, verificar se o novo hotel existe
    if id_hotel is not None:
        if id_hotel not in hoteis:
            print(f"Erro: Novo Hotel {id_hotel} não encontrado.")
            return 404, "Hotel de destino não existe."
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

    print("Quarto atualizado com sucesso.")
    return 200, {"id_quarto": id_quarto, **quartos[id_quarto].copy()}

# DELETE
def remover_quarto(id_quarto):
    # REGRA: Verificar se o quarto existe
    if id_quarto not in quartos:
        print("Quarto não encontrado.")
        return 404, "Quarto não encontrado."

    quarto_removido = quartos.pop(id_quarto)
    print("Quarto removido com sucesso.")
    return 200, {"id_quarto": id_quarto, "quarto_removido": quarto_removido}

# DISPONIBILIDADE
def consultar_quartos_disponiveis(reservas):
    """
    Verifica quais quartos não estão associados a nenhuma reserva.
    """
    if not quartos:
        print("Não existem quartos no sistema.")
        return 404, "Não existem quartos registados."

    # Obtém IDs de quartos que já estão em reservas
    ids_ocupados = [res["id_quarto"] for res in reservas.values()]

    # Filtra quartos que não estão na lista de ocupados
    disponiveis = [
        {"id_quarto": id_q, **dados}
        for id_q, dados in quartos.items()
        if id_q not in ids_ocupados
    ]

    total = len(disponiveis)

    if total == 0:
        print("Nenhum quarto disponível para reserva.")
        return 404, "Não existem quartos disponíveis."

    print(f"Total de quartos disponíveis: {total}")
    return 200, {"total_disponivel": total, "quartos": disponiveis}





























