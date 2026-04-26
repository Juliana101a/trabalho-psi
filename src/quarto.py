

# ==============================
# quarto.py
# CRUD simples para entidade Quarto
# ==============================

from utils import gerar_id_quarto

quartos = {}

# CREATE
def criar_quarto(numero, descricao, tipo_quarto, preco, lotacao):
    id_quarto = gerar_id_quarto()
    
    quartos[id_quarto] = {
        "numero": numero,
        "descricao": descricao,
        "tipo_quarto": tipo_quarto,
        "preco": preco,
        "lotacao": lotacao
    }
    
    print(f"Quarto criado com sucesso. ID: {id_quarto}")
    return 201, {"id_quarto": id_quarto, **quartos[id_quarto]}

# READ (listar todos)
def listar_quartos():
    if not quartos:
        print("Não existem quartos registados.")
        return 404, "Não existem quartos registados."
    
    # Retorna lista de dicionários com IDs incluídos
    lista_formatada = [{"id_quarto": id_q, **dados} for id_q, dados in quartos.items()]
    
    for q in lista_formatada:
        print(f"ID: {q['id_quarto']} | Nº: {q['numero']} | Tipo: {q['tipo_quarto']} | Lotação: {q['lotacao']}")
        
    return 200, lista_formatada

# READ (consultar individual)
def consultar_quarto(id_quarto):
    if id_quarto not in quartos:
        print("Quarto não encontrado.")
        return 404, "Quarto não encontrado."
    
    dados = {"id_quarto": id_quarto, **quartos[id_quarto].copy()}
    print(dados)
    return 200, dados

# UPDATE
def atualizar_quarto(id_quarto, numero=None, descricao=None, tipo_quarto=None, preco=None, lotacao=None):
    if id_quarto not in quartos:
        print("Quarto não encontrado.")
        return 404, "Quarto não encontrado."
    
    if numero is not None:
        quartos[id_quarto]["numero"] = numero
    if descricao is not None:
        quartos[id_quarto]["descricao"] = descricao
    if tipo_quarto is not None:
        quartos[id_quarto]["tipo_quarto"] = tipo_quarto
    if preco is not None:
        quartos[id_quarto]["preco"] = preco
    if lotacao is not None:
        quartos[id_quarto]["lotacao"] = lotacao
        
    print("Quarto atualizado com sucesso.")
    return 200, {"id_quarto": id_quarto, **quartos[id_quarto].copy()}

# DELETE
def remover_quarto(id_quarto):
    if id_quarto not in quartos:
        print("Quarto não encontrado.")
        return 404, "Quarto não encontrado."
    
    quarto_removido = quartos.pop(id_quarto)
    print("Quarto removido com sucesso.")
    return 200, {"id_quarto": id_quarto, "quarto_removido": quarto_removido}























































