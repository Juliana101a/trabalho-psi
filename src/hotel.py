
from persistencia import guardar_dados, carregar_dados
from utils import gerar_id
from logger import log_info, log_warning


def criar_hotel(nome, endereco, telefone, classificacao):
    hoteis = carregar_dados("hoteis.json")
    hid = gerar_id("H", hoteis)

    hoteis[hid] = {
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "classificacao": classificacao
    }

    guardar_dados("hoteis.json", hoteis)
    log_info(f"Hotel criado: {hid}")
    return 201, hid


def listar_hoteis():
    hoteis = carregar_dados("hoteis.json")
    log_info("Listagem hotéis")
    return 200, [{"id": k, **v} for k, v in hoteis.items()]


def consultar_hotel(hid):
    hoteis = carregar_dados("hoteis.json")

    if hid not in hoteis:
        log_warning(f"Hotel não encontrado: {hid}")
        return 404, "não encontrado"

    log_info(f"Hotel consultado: {hid}")
    return 200, {"id": hid, **hoteis[hid]}


def atualizar_hotel(hid, nome=None, endereco=None, telefone=None, classificacao=None):
    hoteis = carregar_dados("hoteis.json")

    if hid not in hoteis:
        log_warning(f"Tentativa atualizar hotel inexistente: {hid}")
        return 404, "não encontrado"

    if nome:
        hoteis[hid]["nome"] = nome

    if endereco:
        hoteis[hid]["endereco"] = endereco

    if telefone:
        hoteis[hid]["telefone"] = telefone

    if classificacao is not None:
        hoteis[hid]["classificacao"] = classificacao

    guardar_dados("hoteis.json", hoteis)
    log_info(f"Hotel atualizado: {hid}")
    return 200, hid


def remover_hotel(hid):
    hoteis = carregar_dados("hoteis.json")

    if hid not in hoteis:
        log_warning(f"Remoção hotel inexistente: {hid}")
        return 404, "não encontrado"

    r = hoteis.pop(hid)
    guardar_dados("hoteis.json", hoteis)

    log_info(f"Hotel removido: {hid}")
    return 200, r
