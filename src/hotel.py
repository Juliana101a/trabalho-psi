

from persistencia import guardar_dados, carregar_dados

contador = 1


def gerar_id():
    global contador
    hid = f"H{contador:03d}"
    contador += 1
    return hid


def criar_hotel(nome, endereco, telefone, classificacao):
    hoteis = carregar_dados("hoteis.json")
    hid = gerar_id()
    hoteis[hid] = {
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "classificacao": classificacao
    }
    guardar_dados("hoteis.json", hoteis)
    return 201, hid


def listar_hoteis():
    hoteis = carregar_dados("hoteis.json")
    return 200, [{"id": k, **v} for k, v in hoteis.items()]


def consultar_hotel(hid):
    hoteis = carregar_dados("hoteis.json")
    if hid not in hoteis:
        return 404, "não encontrado"
    return 200, {"id": hid, **hoteis[hid]}


def atualizar_hotel(hid, nome=None, endereco=None, telefone=None, classificacao=None):
    hoteis = carregar_dados("hoteis.json")
    if hid not in hoteis:
        return 404, "não encontrado"

    if nome is not None:
        hoteis[hid]["nome"] = nome
    if endereco is not None:
        hoteis[hid]["endereco"] = endereco
    if telefone is not None:
        hoteis[hid]["telefone"] = telefone
    if classificacao is not None:
        hoteis[hid]["classificacao"] = classificacao

    guardar_dados("hoteis.json", hoteis)
    return 200, hid


def remover_hotel(hid):
    hoteis = carregar_dados("hoteis.json")
    if hid not in hoteis:
        return 404, "não encontrado"

    r = hoteis.pop(hid)
    guardar_dados("hoteis.json", hoteis)
    return 200, r









