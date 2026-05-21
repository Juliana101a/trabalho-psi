

def atualizar_hotel(hid, nome=None, endereco=None, telefone=None, classificacao=None):
    hoteis = carregar_dados("hoteis.json")

    if hid not in hoteis:
        log_error(f"Atualização falhou hotel: {hid}")
        return 404, "não encontrado"

    if nome: hoteis[hid]["nome"] = nome
    if endereco: hoteis[hid]["endereco"] = endereco
    if telefone: hoteis[hid]["telefone"] = telefone
    if classificacao is not None: hoteis[hid]["classificacao"] = classificacao

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





