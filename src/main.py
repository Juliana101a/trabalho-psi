

from cliente import (
    criar_cliente, listar_clientes, consultar_cliente,
    atualizar_cliente, remover_cliente
)

from hotel import (
    criar_hotel, listar_hoteis, consultar_hotel,
    atualizar_hotel, remover_hotel
)

from quarto import (
    criar_quarto, listar_quartos, consultar_quarto,
    atualizar_quarto, remover_quarto
)

from reserva import (
    criar_reserva, listar_reservas, consultar_reserva,
    atualizar_reserva, remover_reserva
)

from pagamento import (
    criar_pagamento, listar_pagamentos, consultar_pagamento,
    atualizar_pagamento, remover_pagamento
)

from utils import converter_float, converter_int


# ------------------ MENU ------------------
def exibir_menu():
    print("\n" + "=" * 60)
    print("        SISTEMA DE GESTÃO HOTELEIRA")
    print("=" * 60)

    print(" [1-5] Cliente | [6-10] Hotel | [11-15] Quarto")
    print(" [16-20] Reserva | [21-25] Pagamento")
    print(" [0] Sair")
    print("=" * 60)


def main():
    while True:
        exibir_menu()
        op = input("Escolha: ")

        try:
            # CLIENTE
            if op == "1":
                print(criar_cliente(
                    input("Nome: "),
                    input("NIF: "),
                    input("Telefone: "),
                    input("Email: "),
                    input("Data nascimento: ")
                ))

            elif op == "2":
                print(listar_clientes())

            elif op == "3":
                print(consultar_cliente(input("ID Cliente: ")))

            elif op == "4":
                print(atualizar_cliente(
                    input("ID Cliente: "),
                    input("Nome: ") or None,
                    input("NIF: ") or None,
                    input("Telefone: ") or None,
                    input("Email: ") or None,
                    input("Data: ") or None
                ))

            elif op == "5":
                print(remover_cliente(input("ID Cliente: ")))

            # HOTEL
            elif op == "6":
                print(criar_hotel(
                    input("Nome: "),
                    input("Endereço: "),
                    input("Telefone: "),
                    converter_int(input("Classificação: "))
                ))

            elif op == "7":
                print(listar_hoteis())

            elif op == "8":
                print(consultar_hotel(input("ID Hotel: ")))

            elif op == "9":
                print(atualizar_hotel(
                    input("ID Hotel: "),
                    input("Nome: ") or None,
                    input("Endereço: ") or None,
                    input("Telefone: ") or None,
                    converter_int(input("Classificação: "))
                ))

            elif op == "10":
                print(remover_hotel(input("ID Hotel: ")))

            # QUARTO
            elif op == "11":
                print(criar_quarto(
                    input("ID Hotel: "),
                    input("Número: "),
                    input("Descrição: "),
                    input("Tipo: "),
                    converter_float(input("Preço: ")),
                    converter_int(input("Lotação: "))
                ))

            elif op == "12":
                print(listar_quartos())

            elif op == "13":
                print(consultar_quarto(input("ID Quarto: ")))

            elif op == "14":
                print(atualizar_quarto(
                    input("ID Quarto: "),
                    input("ID Hotel: ") or None,
                    input("Número: ") or None,
                    input("Descrição: ") or None,
                    input("Tipo: ") or None,
                    converter_float(input("Preço: ")),
                    converter_int(input("Lotação: "))
                ))

            elif op == "15":
                print(remover_quarto(input("ID Quarto: ")))

            # RESERVA
            elif op == "16":
                print(criar_reserva(
                    input("ID Hotel: "),
                    input("ID Quarto: "),
                    input("Check-in: "),
                    input("Check-out: "),
                    input("Extras (separados por vírgula): ").split(","),
                    converter_float(input("Valor: ")),
                    input("Status: ")
                ))

            elif op == "17":
                print(listar_reservas())

            elif op == "18":
                print(consultar_reserva(input("ID Reserva: ")))

            elif op == "19":
                opcao = input("Atualizar valor? (s/n): ")

                valor = converter_float(input("Valor: ")) if opcao == "s" else None

                print(atualizar_reserva(
                    input("ID Reserva: "),
                    input("Hotel: ") or None,
                    input("Quarto: ") or None,
                    input("Check-in: ") or None,
                    input("Check-out: ") or None,
                    None,
                    valor,
                    input("Status: ") or None
                ))

            elif op == "20":
                print(remover_reserva(input("ID Reserva: ")))

            # PAGAMENTO
            elif op == "21":
                print(criar_pagamento(
                    input("ID Reserva: "),
                    converter_float(input("Valor: ")),
                    input("Método: "),
                    input("Status: ")
                ))

            elif op == "22":
                print(listar_pagamentos())

            elif op == "23":
                print(consultar_pagamento(input("ID Pagamento: ")))

            elif op == "24":
                opcao = input("Atualizar valor? (s/n): ")

                valor = converter_float(input("Valor: ")) if opcao == "s" else None

                print(atualizar_pagamento(
                    input("ID Pagamento: "),
                    input("Reserva: ") or None,
                    valor,
                    input("Método: ") or None,
                    input("Status: ") or None
                ))

            elif op == "25":
                print(remover_pagamento(input("ID Pagamento: ")))

            elif op == "0":
                print("A encerrar sistema...")
                break

            else:
                print("Opção inválida!")

        except Exception as e:
            print("Erro no sistema:", e)


if __name__ == "__main__":
    main()




































































