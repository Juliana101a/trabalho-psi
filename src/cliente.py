

from persistencia import guardar_dados, carregar_dados
from utils import gerar_id
from logger import log_info, log_warning, log_error


def criar_cliente(nome, nif, telefone, email, data):
    clientes = carregar_dados("clientes.json")
    cid = gerar_id("C", clientes)

    clientes[cid] = {
        "nome": nome,
        "nif": nif,
        "telefone": telefone,
        "email": email,
        "data": data
    }

    guardar_dados("clientes.json", clientes)
    log_info(f"Cliente criado: {cid}")
    return 201, cid


def listar_clientes():
    clientes = carregar_dados("clientes.json")
    log_info("Listagem clientes")
    return 200, [{"id": k, **v} for k, v in clientes.items()]


def consultar_cliente(cid):
    clientes = carregar_dados("clientes.json")

    if cid not in clientes:
        log_warning(f"Cliente não encontrado: {cid}")
        return 404, "não encontrado"

    log_info(f"Cliente consultado: {cid}")
    return 200, {"id": cid, **clientes[cid]}


def atualizar_cliente(cid, nome=None, nif=None, telefone=None, email=None, data=None):
    clientes = carregar_dados("clientes.json")

    if cid not in clientes:
        log_warning(f"Tentativa atualizar cliente inexistente: {cid}")
        return 404, "não encontrado"

    if nome:
        clientes[cid]["nome"] = nome

    if nif:
        clientes[cid]["nif"] = nif

    if telefone:
        clientes[cid]["telefone"] = telefone

    if email:
        clientes[cid]["email"] = email

    if data:
        clientes[cid]["data"] = data

    guardar_dados("clientes.json", clientes)
    log_info(f"Cliente atualizado: {cid}")
    return 200, cid


def remover_cliente(cid):
    clientes = carregar_dados("clientes.json")

    if cid not in clientes:
        log_warning(f"Tentativa remover cliente inexistente: {cid}")
        return 404, "não encontrado"

    r = clientes.pop(cid)
    guardar_dados("clientes.json", clientes)

    log_info(f"Cliente removido: {cid}")
    return 200, r
