
# 🏨 Gestor de Hotel – Sistema CRUD em Python

## 📘 Descrição

Este projeto foi desenvolvido no âmbito do Curso Profissional de Gestão e Programação de Sistemas Informáticos (GPSI) – 10.º ano, com o objetivo de aplicar conceitos fundamentais de programação através da construção de um sistema de gestão hoteleira.

A aplicação permite gerir diferentes entidades de um hotel, incluindo clientes, hotéis, quartos, reservas e pagamentos, implementando operações CRUD (**Create, Read, Update, Delete**) com armazenamento em memória.

---

## 🎯 Objetivos de Aprendizagem

Durante o desenvolvimento deste projeto foram trabalhados os seguintes conceitos:

* Organização de código em múltiplos ficheiros Python
* Utilização de dicionários como estrutura de dados
* Implementação de operações CRUD
* Validação de dados introduzidos pelo utilizador
* Geração automática de identificadores (IDs)
* Manipulação e validação de datas
* Separação entre lógica de negócio e interface (menu)

---

## 🧩 Funcionalidades

O sistema permite:

* 👤 Gestão de Clientes
* 🏨 Gestão de Hotéis
* 🛏️ Gestão de Quartos
* 📅 Gestão de Reservas
* 💳 Gestão de Pagamentos

Cada entidade suporta operações completas de:

* Criar
* Listar
* Consultar
* Atualizar
* Remover

---

## 📂 Estrutura do Projeto

```
gestor_hotel/
└── src/
    ├── main_app.py   # Interface em terminal (menu principal)
    ├── cliente.py    # CRUD de clientes
    ├── hotel.py      # CRUD de hotéis
    ├── quarto.py     # CRUD de quartos
    ├── reserva.py    # CRUD de reservas
    ├── pagamento.py  # CRUD de pagamentos
    └── utils.py      # Funções auxiliares
```

---

## 📄 Descrição dos Módulos

### `main_app.py`

Responsável pela interface em terminal.
Apresenta o menu, recolhe dados do utilizador e chama as funções dos módulos.

### `cliente.py`

Gestão de clientes com validação de dados (ex: data de nascimento) e geração automática de ID.

### `hotel.py`

Gestão de hotéis, incluindo criação, edição e remoção.

### `quarto.py`

Gestão de quartos associados a hotéis, incluindo preço, tipo e descrição.

### `reserva.py`

Gestão de reservas com validação de datas (check-in e check-out) e associação a clientes, hotéis e quartos.

### `pagamento.py`

Gestão de pagamentos associados às reservas.
Inclui registo de pagamentos, controlo de valor pago, método de pagamento e atualização do estado da reserva.

### `utils.py`

Funções auxiliares reutilizáveis:

* Geração de IDs
* Validação de datas
* Conversão de tipos

---

## ▶️ Como Executar

1. Garantir que o Python está instalado
2. Navegar até à pasta do projeto:

   ```
   cd gestor_hotel/src
   ```
3. Executar o programa:

   ```
   python main_app.py
   ```
4. Utilizar o menu interativo no terminal

---

## 📚 Conceitos Aplicados

* Funções
* Dicionários
* Modularização de código
* Estruturas condicionais (`if/else`)
* Ciclos (`while`)
* Validação de dados
* CRUD

---

## 🚀 Possíveis Melhorias Futuras

* Persistência de dados (SQLite ou ficheiros)
* Interface gráfica (Tkinter ou web)
* API REST (FastAPI ou Flask)
* Sistema de autenticação
* Controlo de disponibilidade de quartos (evitar overbooking)
* Gestão de pagamentos parciais e totais

---

## 👨‍🏫 Contexto Educativo

Projeto desenvolvido com fins pedagógicos no curso GPSI – 10.º ano, como introdução prática ao desenvolvimento de aplicações estruturadas em Python.

---

## 📄 Licença

Uso livre para fins educativos. Pode ser reutilizado e adaptado.
