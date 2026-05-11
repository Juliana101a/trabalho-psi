
from persistencia import guardar_dados
from hotel import hoteis

quartos = {}
contador = 1


def gerar_id():
    global contador
    qid = f"Q{contador:03d}"
    contador += 1
    return qid


def criar_quarto(id_hotel, numero, descricao, tipo, preco, lotacao):
    if id_hotel not in hoteis:
        return 404, "hotel não existe"

    qid = gerar_id()
    quartos[qid] = {
        "id_hotel": id_hotel,
        "numero": numero,
        "descricao": descricao,
        "tipo": tipo,
        "preco": preco,
        "lotacao": lotacao
    }
    guardar_dados("quartos.json", quartos)
    return 201, qid


def listar_quartos():
    return 200, [{"id": k, **v} for k, v in quartos.items()]


def consultar_quarto(qid):
    if qid not in quartos:
        return 404, "não encontrado"
    return 200, {"id": qid, **quartos[qid]}


def atualizar_quarto(qid, id_hotel=None, numero=None, descricao=None, tipo=None, preco=None, lotacao=None):
    if qid not in quartos:
        return 404, "não encontrado"

    if id_hotel: quartos[qid]["id_hotel"] = id_hotel
    if numero: quartos[qid]["numero"] = numero
    if descricao: quartos[qid]["descricao"] = descricao
    if tipo: quartos[qid]["tipo"] = tipo
    if preco is not None: quartos[qid]["preco"] = preco
    if lotacao is not None: quartos[qid]["lotacao"] = lotacao

    guardar_dados("quartos.json", quartos)
    return 200, qid


def remover_quarto(qid):
    if qid not in quartos:
        return 404, "não encontrado"

    r = quartos.pop(qid)
    guardar_dados("quartos.json", quartos)
    return 200, r















