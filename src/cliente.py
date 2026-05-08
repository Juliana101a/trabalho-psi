
from persistencia import guardar_dados



from utils import gerar_id_cliente, validar_data_nascimento

clientes = {}


def criar_cliente(nome, nif, telefone, email, data_nascimento):
    if not validar_data_nascimento(data_nascimento):
        return 400, "Data inválida"

    id_cliente = gerar_id_cliente()

    clientes[id_cliente] = {
        "nome": nome,
        "nif": nif,
        "telefone": telefone,
        "email": email,
        "data_nascimento": data_nascimento
    }

    return 201, id_cliente


def listar_clientes():
    if not clientes:
        return 200, []

    return 200, [
        {"id_cliente": id_c, **dados}
        for id_c, dados in clientes.items()
    ]


def consultar_cliente(id_cliente):
    if id_cliente not in clientes:
        return 404, "Cliente não encontrado"

    return 200, {"id_cliente": id_cliente, **clientes[id_cliente]}


def atualizar_cliente(id_cliente, nome=None, nif=None, telefone=None, email=None, data_nascimento=None):
    if id_cliente not in clientes:
        return 404, "Cliente não encontrado"

    if nome: clientes[id_cliente]["nome"] = nome
    if nif: clientes[id_cliente]["nif"] = nif
    if telefone: clientes[id_cliente]["telefone"] = telefone
    if email: clientes[id_cliente]["email"] = email

    if data_nascimento:
        if not validar_data_nascimento(data_nascimento):
            return 400, "Data inválida"
        clientes[id_cliente]["data_nascimento"] = data_nascimento

    return 200, id_cliente


def remover_cliente(id_cliente):
    if id_cliente not in clientes:
        return 404, "Cliente não encontrado"

    clientes.pop(id_cliente)
    guardar_dados("clientes.json", clientes)

    return 200, id_cliente







