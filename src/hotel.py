

from utils import gerar_id_hotel

hoteis = {}

# CREATE
def criar_hotel(nome, endereco, telefone, classificacao):
    id_hotel = gerar_id_hotel()

    hotel = {
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "classificacao": classificacao
    }

    hoteis[id_hotel] = hotel

    return 201, {"id_hotel": id_hotel, **hotel}


# READ (todos)
def listar_hoteis():
    return 200, hoteis.copy()


# READ (um hotel)
def consultar_hotel(id_hotel):
    if id_hotel not in hoteis:
        return 404, "Hotel não encontrado."

    return 200, hoteis[id_hotel].copy()


# UPDATE
def atualizar_hotel(id_hotel, nome=None, endereco=None, telefone=None, classificacao=None):
    if id_hotel not in hoteis:
        return 404, "Hotel não encontrado."

    if nome is not None:
        hoteis[id_hotel]["nome"] = nome

    if endereco is not None:
        hoteis[id_hotel]["endereco"] = endereco

    if telefone is not None:
        hoteis[id_hotel]["telefone"] = telefone

    if classificacao is not None:
        hoteis[id_hotel]["classificacao"] = classificacao

    return 200, hoteis[id_hotel].copy()


# DELETE
def remover_hotel(id_hotel):
    if id_hotel not in hoteis:
        return 404, "Hotel não encontrado."

    hotel_removido = hoteis.pop(id_hotel)

    return 200, {
        "id_hotel": id_hotel,
        "hotel_removido": hotel_removido
    }






































