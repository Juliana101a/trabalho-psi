
from persistencia import guardar_dados
from utils import validar_data

clientes = {}
contador = 1


def criar_cliente(nome, nif, telefone, email, data_nascimento):

    global contador

    if not validar_data(data_nascimento):
        return 400, "Data inválida"

    id_cliente = f"C{contador:03d}"
    contador += 1

    clientes[id_cliente] = {
        "nome": nome,
        "nif": nif,
        "telefone": telefone,
        "email": email,
        "data_nascimento": data_nascimento
    }

    guardar_dados("clientes.json", clientes)

    return 201, id_cliente


def listar_clientes():
    return 200, [{"id_cliente": i, **d} for i, d in clientes.items()]


def consultar_cliente(id_cliente):
    if id_cliente not in clientes:
        return 404, "Não encontrado"

    return 200, {"id_cliente": id_cliente, **clientes[id_cliente]}


def atualizar_cliente(id_cliente, nome=None, nif=None, telefone=None, email=None, data_nascimento=None):

    if id_cliente not in clientes:
        return 404, "Não encontrado"

    if nome is not None: clientes[id_cliente]["nome"] = nome
    if nif is not None: clientes[id_cliente]["nif"] = nif
    if telefone is not None: clientes[id_cliente]["telefone"] = telefone
    if email is not None: clientes[id_cliente]["email"] = email
    if data_nascimento is not None: clientes[id_cliente]["data_nascimento"] = data_nascimento

    guardar_dados("clientes.json", clientes)

    return 200, id_cliente


def remover_cliente(id_cliente):

    if id_cliente not in clientes:
        return 404, "Não encontrado"

    return 200, clientes.pop(id_cliente)






