
from persistencia import guardar_dados, carregar_dados


contador = 1


def gerar_id():
    global contador
    cid = f"C{contador:03d}"
    contador += 1
    return cid


def criar_cliente(nome, nif, telefone, email, data):
    clientes = carregar_dados("clientes.json")
    cid = gerar_id()
    clientes[cid] = {
        "nome": nome,
        "nif": nif,
        "telefone": telefone,
        "email": email,
        "data": data
    }
    guardar_dados("clientes.json", clientes)
    return 201, cid


def listar_clientes():
    clientes = carregar_dados("clientes.json")
    return 200, [{"id": k, **v} for k, v in clientes.items()]


def consultar_cliente(cid):
    clientes = carregar_dados("clientes.json")
    if cid not in clientes:
        return 404, "não encontrado"
    return 200, {"id": cid, **clientes[cid]}


def atualizar_cliente(cid, nome=None, nif=None, telefone=None, email=None, data=None):
    clientes = carregar_dados("clientes.json")
    if cid not in clientes:
        return 404, "não encontrado"

    if nome is not None:
        clientes[cid]["nome"] = nome
    if nif is not None:
        clientes[cid]["nif"] = nif
    if telefone is not None:
        clientes[cid]["telefone"] = telefone
    if email is not None:
        clientes[cid]["email"] = email
    if data is not None:
        clientes[cid]["data"] = data

    guardar_dados("clientes.json", clientes)
    return 200, cid


def remover_cliente(cid):
    clientes = carregar_dados("clientes.json")
    if cid not in clientes:
        return 404, "não encontrado"

    r = clientes.pop(cid)
    guardar_dados("clientes.json", clientes)
    return 200, r
