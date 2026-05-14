
from persistencia import guardar_dados

hoteis = {}
contador = 1


def gerar_id():
    global contador
    hid = f"H{contador:03d}"
    contador += 1
    return hid


def criar_hotel(nome, endereco, telefone, classif):
    hid = gerar_id()
    hoteis[hid] = {
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "classificacao": classif
    }
    guardar_dados("hoteis.json", hoteis)
    return 201, hid


def listar_hoteis():
    return 200, [{"id": k, **v} for k, v in hoteis.items()]


def consultar_hotel(hid):
    if hid not in hoteis:
        return 404, "não encontrado"
    return 200, {"id": hid, **hoteis[hid]}


def atualizar_hotel(hid, nome=None, endereco=None, telefone=None, classif=None):
    if hid not in hoteis:
        return 404, "não encontrado"

    if nome: hoteis[hid]["nome"] = nome
    if endereco: hoteis[hid]["endereco"] = endereco
    if telefone: hoteis[hid]["telefone"] = telefone
    if classif is not None: hoteis[hid]["classificacao"] = classif

    guardar_dados("hoteis.json", hoteis)
    return 200, hid


def remover_hotel(hid):
    if hid not in hoteis:
        return 404, "não encontrado"

    r = hoteis.pop(hid)
    guardar_dados("hoteis.json", hoteis)
    return 200, r










