from persistencia import guardar_dados

hoteis = {}
contador = 1


def criar_hotel(nome, endereco, telefone, classificacao):

    global contador

    id_hotel = f"H{contador:03d}"
    contador += 1

    hoteis[id_hotel] = {
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "classificacao": classificacao
    }

    guardar_dados("hoteis.json", hoteis)

    return 201, id_hotel


def listar_hoteis():
    return 200, [{"id_hotel": i, **d} for i, d in hoteis.items()]


def consultar_hotel(id_hotel):
    if id_hotel not in hoteis:
        return 404, "Não encontrado"

    return 200, {"id_hotel": id_hotel, **hoteis[id_hotel]}


def atualizar_hotel(id_hotel, nome=None, endereco=None, telefone=None, classificacao=None):

    if id_hotel not in hoteis:
        return 404, "Não encontrado"

    if nome is not None: hoteis[id_hotel]["nome"] = nome
    if endereco is not None: hoteis[id_hotel]["endereco"] = endereco
    if telefone is not None: hoteis[id_hotel]["telefone"] = telefone
    if classificacao is not None: hoteis[id_hotel]["classificacao"] = classificacao

    guardar_dados("hoteis.json", hoteis)

    return 200, id_hotel


def remover_hotel(id_hotel):

    if id_hotel not in hoteis:
        return 404, "Não encontrado"

    return 200, hoteis.pop(id_hotel)







