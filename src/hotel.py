

from utils import gerar_id_hotel

hoteis = {}

# CREATE
def criar_hotel(nome, endereco, telefone, classificacao):
    id_hotel = gerar_id_hotel()
    hoteis[id_hotel] = {
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "classificacao": classificacao
    }
    print(f"Hotel criado com sucesso. ID: {id_hotel}")

# READ
def listar_hoteis():
    if not hoteis:
        print("Não existem hotéis registados.")
        return
    for id_h, dados in hoteis.items():
        print(f"ID: {id_h} | Nome: {dados['nome']} | Endereço: {dados['endereco']} | Tel: {dados['telefone']} | Classificação: {dados['classificacao']}")

def consultar_hotel(id_hotel):
    if id_hotel not in hoteis:
        print("Hotel não encontrado.")
        return
    print(hoteis[id_hotel])

# UPDATE
def atualizar_hotel(id_hotel, nome=None, endereco=None, telefone=None, classificacao=None):
    if id_hotel not in hoteis:
        print("Hotel não encontrado.")
        return
    if nome:
        hoteis[id_hotel]["nome"] = nome
    if endereco:
        hoteis[id_hotel]["endereco"] = endereco
    if telefone:
        hoteis[id_hotel]["telefone"] = telefone
    if classificacao:
        hoteis[id_hotel]["classificacao"] = classificacao
    print("Hotel atualizado com sucesso.")

# DELETE
def remover_hotel(id_hotel):
    if id_hotel not in hoteis:
        print("Hotel não encontrado.")
        return
    del hoteis[id_hotel]
    print("Hotel removido com sucesso.")








































