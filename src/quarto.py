

from persistencia import guardar_dados, carregar_dados
from utils import gerar_id
from logger import log_info, log_warning


def criar_quarto(id_hotel, numero, descricao, tipo, preco, lotacao):
    quartos = carregar_dados("quartos.json")
    hoteis = carregar_dados("hoteis.json")

    if id_hotel not in hoteis:
        log_warning(f"Hotel inválido ao criar quarto: {id_hotel}")
        return 404, "hotel não existe"

    qid = gerar_id("Q", quartos)

    quartos[qid] = {
        "id_hotel": id_hotel,
        "numero": numero,
        "descricao": descricao,
        "tipo": tipo,
        "preco": preco,
        "lotacao": lotacao
    }

    guardar_dados("quartos.json", quartos)
    log_info(f"Quarto criado: {qid}")
    return 201, qid


def listar_quartos():
    quartos = carregar_dados("quartos.json")
    log_info("Listagem quartos")
    return 200, [{"id": k, **v} for k, v in quartos.items()]


def consultar_quarto(qid):
    quartos = carregar_dados("quartos.json")

    if qid not in quartos:
        log_warning(f"Quarto não encontrado: {qid}")
        return 404, "não encontrado"

    log_info(f"Quarto consultado: {qid}")
    return 200, {"id": qid, **quartos[qid]}


def atualizar_quarto(qid, id_hotel=None, numero=None, descricao=None, tipo=None, preco=None, lotacao=None):
    quartos = carregar_dados("quartos.json")

    if qid not in quartos:
        log_warning(f"Tentativa atualizar quarto inexistente: {qid}")
        return 404, "não encontrado"

    if id_hotel:
        quartos[qid]["id_hotel"] = id_hotel

    if numero:
        quartos[qid]["numero"] = numero

    if descricao:
        quartos[qid]["descricao"] = descricao

    if tipo:
        quartos[qid]["tipo"] = tipo

    if preco is not None:
        quartos[qid]["preco"] = preco

    if lotacao is not None:
        quartos[qid]["lotacao"] = lotacao

    guardar_dados("quartos.json", quartos)
    log_info(f"Quarto atualizado: {qid}")
    return 200, qid


def remover_quarto(qid):
    quartos = carregar_dados("quartos.json")

    if qid not in quartos:
        log_warning(f"Remoção quarto inexistente: {qid}")
        return 404, "não encontrado"

    r = quartos.pop(qid)
    guardar_dados("quartos.json", quartos)

    log_info(f"Quarto removido: {qid}")
    return 200, r
































































