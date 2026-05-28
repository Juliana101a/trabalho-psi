from tkinter import *
from tkinter import messagebox

from cliente import (
    criar_cliente,
    listar_clientes
)

from hotel import (
    criar_hotel,
    listar_hoteis
)

from quarto import (
    criar_quarto,
    listar_quartos
)

from reserva import (
    criar_reserva,
    listar_reservas
)

from pagamento import (
    criar_pagamento,
    listar_pagamentos
)


# =========================
# CLIENTES
# =========================

def janela_clientes():
    janela = Toplevel()
    janela.title("Clientes")
    janela.geometry("500x500")

    Label(janela, text="Nome").pack()
    nome = Entry(janela)
    nome.pack()

    Label(janela, text="NIF").pack()
    nif = Entry(janela)
    nif.pack()

    Label(janela, text="Telefone").pack()
    telefone = Entry(janela)
    telefone.pack()

    Label(janela, text="Email").pack()
    email = Entry(janela)
    email.pack()

    Label(janela, text="Data").pack()
    data = Entry(janela)
    data.pack()

    resultado = Text(janela, height=10, width=50)
    resultado.pack()

    def criar():
        status, cid = criar_cliente(
            nome.get(),
            nif.get(),
            telefone.get(),
            email.get(),
            data.get()
        )

        messagebox.showinfo("Sucesso", f"Cliente criado: {cid}")

    def listar():
        resultado.delete("1.0", END)

        status, clientes = listar_clientes()

        for c in clientes:
            resultado.insert(END, f"{c}\n")

    Button(janela, text="Criar Cliente", command=criar).pack(pady=5)

    Button(janela, text="Listar Clientes", command=listar).pack(pady=5)


# =========================
# HOTEIS
# =========================

def janela_hoteis():
    janela = Toplevel()
    janela.title("Hotéis")
    janela.geometry("500x500")

    Label(janela, text="Nome").pack()
    nome = Entry(janela)
    nome.pack()

    Label(janela, text="Endereço").pack()
    endereco = Entry(janela)
    endereco.pack()

    Label(janela, text="Telefone").pack()
    telefone = Entry(janela)
    telefone.pack()

    Label(janela, text="Classificação").pack()
    classificacao = Entry(janela)
    classificacao.pack()

    resultado = Text(janela, height=10, width=50)
    resultado.pack()

    def criar():
        status, hid = criar_hotel(
            nome.get(),
            endereco.get(),
            telefone.get(),
            classificacao.get()
        )

        messagebox.showinfo("Sucesso", f"Hotel criado: {hid}")

    def listar():
        resultado.delete("1.0", END)

        status, hoteis = listar_hoteis()

        for h in hoteis:
            resultado.insert(END, f"{h}\n")

    Button(janela, text="Criar Hotel", command=criar).pack(pady=5)

    Button(janela, text="Listar Hotéis", command=listar).pack(pady=5)


# =========================
# QUARTOS
# =========================

def janela_quartos():
    janela = Toplevel()
    janela.title("Quartos")
    janela.geometry("500x600")

    Label(janela, text="ID Hotel").pack()
    id_hotel = Entry(janela)
    id_hotel.pack()

    Label(janela, text="Número").pack()
    numero = Entry(janela)
    numero.pack()

    Label(janela, text="Descrição").pack()
    descricao = Entry(janela)
    descricao.pack()

    Label(janela, text="Tipo").pack()
    tipo = Entry(janela)
    tipo.pack()

    Label(janela, text="Preço").pack()
    preco = Entry(janela)
    preco.pack()

    Label(janela, text="Lotação").pack()
    lotacao = Entry(janela)
    lotacao.pack()

    resultado = Text(janela, height=10, width=50)
    resultado.pack()

    def criar():
        status, qid = criar_quarto(
            id_hotel.get(),
            numero.get(),
            descricao.get(),
            tipo.get(),
            preco.get(),
            lotacao.get()
        )

        messagebox.showinfo("Sucesso", f"Quarto criado: {qid}")

    def listar():
        resultado.delete("1.0", END)

        status, quartos = listar_quartos()

        for q in quartos:
            resultado.insert(END, f"{q}\n")

    Button(janela, text="Criar Quarto", command=criar).pack(pady=5)

    Button(janela, text="Listar Quartos", command=listar).pack(pady=5)


# =========================
# RESERVAS
# =========================

def janela_reservas():
    janela = Toplevel()
    janela.title("Reservas")
    janela.geometry("500x600")

    Label(janela, text="ID Hotel").pack()
    id_hotel = Entry(janela)
    id_hotel.pack()

    Label(janela, text="ID Quarto").pack()
    id_quarto = Entry(janela)
    id_quarto.pack()

    Label(janela, text="Checkin").pack()
    checkin = Entry(janela)
    checkin.pack()

    Label(janela, text="Checkout").pack()
    checkout = Entry(janela)
    checkout.pack()

    Label(janela, text="Extras").pack()
    extras = Entry(janela)
    extras.pack()

    Label(janela, text="Valor").pack()
    valor = Entry(janela)
    valor.pack()

    Label(janela, text="Status").pack()
    status_reserva = Entry(janela)
    status_reserva.pack()

    resultado = Text(janela, height=10, width=50)
    resultado.pack()

    def criar():
        status, rid = criar_reserva(
            id_hotel.get(),
            id_quarto.get(),
            checkin.get(),
            checkout.get(),
            extras.get(),
            valor.get(),
            status_reserva.get()
        )

        messagebox.showinfo("Sucesso", f"Reserva criada: {rid}")

    def listar():
        resultado.delete("1.0", END)

        status, reservas = listar_reservas()

        for r in reservas:
            resultado.insert(END, f"{r}\n")

    Button(janela, text="Criar Reserva", command=criar).pack(pady=5)

    Button(janela, text="Listar Reservas", command=listar).pack(pady=5)


# =========================
# PAGAMENTOS
# =========================

def janela_pagamentos():
    janela = Toplevel()
    janela.title("Pagamentos")
    janela.geometry("500x500")

    Label(janela, text="ID Reserva").pack()
    id_reserva = Entry(janela)
    id_reserva.pack()

    Label(janela, text="Valor").pack()
    valor = Entry(janela)
    valor.pack()

    Label(janela, text="Método").pack()
    metodo = Entry(janela)
    metodo.pack()

    Label(janela, text="Status").pack()
    status_pagamento = Entry(janela)
    status_pagamento.pack()

    resultado = Text(janela, height=10, width=50)
    resultado.pack()

    def criar():
        status, pid = criar_pagamento(
            id_reserva.get(),
            valor.get(),
            metodo.get(),
            status_pagamento.get()
        )

        messagebox.showinfo("Sucesso", f"Pagamento criado: {pid}")

    def listar():
        resultado.delete("1.0", END)

        status, pagamentos = listar_pagamentos()

        for p in pagamentos:
            resultado.insert(END, f"{p}\n")

    Button(janela, text="Criar Pagamento", command=criar).pack(pady=5)

    Button(janela, text="Listar Pagamentos", command=listar).pack(pady=5)


# =========================
# JANELA PRINCIPAL
# =========================

root = Tk()

root.title("Sistema Gestão Hotel")

root.geometry("400x400")

Label(
    root,
    text="Sistema Gestão Hotel",
    font=("Arial", 18)
).pack(pady=20)

Button(
    root,
    text="Clientes",
    width=20,
    command=janela_clientes
).pack(pady=5)

Button(
    root,
    text="Hotéis",
    width=20,
    command=janela_hoteis
).pack(pady=5)

Button(
    root,
    text="Quartos",
    width=20,
    command=janela_quartos
).pack(pady=5)

Button(
    root,
    text="Reservas",
    width=20,
    command=janela_reservas
).pack(pady=5)

Button(
    root,
    text="Pagamentos",
    width=20,
    command=janela_pagamentos
).pack(pady=5)

Button(
    root,
    text="Sair",
    width=20,
    command=root.quit
).pack(pady=20)

root.mainloop()
