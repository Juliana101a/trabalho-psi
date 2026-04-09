

from utils import gerar_id_cliente, validar_data_nascimento

clientes = {}

# CREATE
def criar_cliente(nome, telefone, email, data_nascimento):
    if not validar_data_nascimento(data_nascimento):
        print("Data inválida. Use formato YYYY-MM-DD.")
        return

    id_cliente = gerar_id_cliente()
    clientes[id_cliente] = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "data_nascimento": data_nascimento
    }
    print(f"Cliente criado com sucesso. ID: {id_cliente}")

# READ
def listar_clientes():
    if not clientes:
        print("Não existem clientes registados.")
        return
    for id_c, dados in clientes.items():
        print(f"ID: {id_c} | Nome: {dados['nome']} | Tel: {dados['telefone']} | Email: {dados['email']} | Nascimento: {dados['data_nascimento']}")

def consultar_cliente(id_cliente):
    if id_cliente not in clientes:
        print("Cliente não encontrado.")
        return
    print(clientes[id_cliente])

# UPDATE
def atualizar_cliente(id_cliente, nome=None, telefone=None, email=None, data_nascimento=None):
    if id_cliente not in clientes:
        print("Cliente não encontrado.")
        return

    if data_nascimento:
        if not validar_data_nascimento(data_nascimento):
            print("Data inválida.")
            return
        clientes[id_cliente]["data_nascimento"] = data_nascimento

    if nome:
        clientes[id_cliente]["nome"] = nome
    if telefone:
        clientes[id_cliente]["telefone"] = telefone
    if email:
        clientes[id_cliente]["email"] = email

    print("Cliente atualizado com sucesso.")

# DELETE
def remover_cliente(id_cliente):
    if id_cliente not in clientes:
        print("Cliente não encontrado.")
        return
    del clientes[id_cliente]
    print("Cliente removido com sucesso.")









































