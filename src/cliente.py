

from utils import gerar_id_cliente, validar_data_nascimento

clientes = {}

# CREATE
def criar_cliente(nome, telefone, email, data_nascimento):
    if not validar_data_nascimento(data_nascimento):
        return 400, "Data inválida. Use formato YYYY-MM-DD."

    id_cliente = gerar_id_cliente()

    clientes[id_cliente] = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "data_nascimento": data_nascimento
    }

    return 201, {"id_cliente": id_cliente, **clientes[id_cliente]}


# READ (todos)
def listar_clientes():
    return 200, clientes.copy()


# READ (um cliente)
def consultar_cliente(id_cliente):
    if id_cliente not in clientes:
        return 404, "Cliente não encontrado."

    return 200, clientes[id_cliente].copy()


# UPDATE
def atualizar_cliente(id_cliente, nome=None, telefone=None, email=None, data_nascimento=None):
    if id_cliente not in clientes:
        return 404, "Cliente não encontrado."

    if data_nascimento is not None:
        if not validar_data_nascimento(data_nascimento):
            return 400, "Data inválida. Use formato YYYY-MM-DD."
        clientes[id_cliente]["data_nascimento"] = data_nascimento

    if nome is not None:
        clientes[id_cliente]["nome"] = nome

    if telefone is not None:
        clientes[id_cliente]["telefone"] = telefone

    if email is not None:
        clientes[id_cliente]["email"] = email

    return 200, clientes[id_cliente].copy()


# DELETE
def remover_cliente(id_cliente):
    if id_cliente not in clientes:
        return 404, "Cliente não encontrado."

    cliente_removido = clientes.pop(id_cliente)

    return 200, {
        "id_cliente": id_cliente,
        "cliente_removido": cliente_removido
    }







































