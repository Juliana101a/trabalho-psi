Projeto Gestor Hotel – CRUD Hotel
📘 Descrição do Projeto

Este projeto foi desenvolvido com fins pedagógicos para o Curso Profissional de Gestão e Programação de Sistemas Informáticos (GPSI) – 10.º ano.

O objetivo principal é demonstrar como implementar operações CRUD (Create, Read, Update, Delete) em Python utilizando:

Funções (sem classes)
Dicionários
Separação por ficheiros
Validação de dados
Menus em terminal

O projeto simula a gestão das entidades Cliente, Hotel, Quarto e Reserva.

🎯 Objetivos Pedagógicos

Com este projeto, aprendi a:

Organizar código em múltiplos ficheiros Python
Utilizar dicionários como estrutura de armazenamento
Implementar operações CRUD
Validar dados introduzidos pelo utilizador
Gerar identificadores automáticos
Trabalhar com datas em Python
Separar lógica de negócio da interface (menu)
📂 Estrutura do Projeto
gestor_hotel/
└── src/
    ├── main_app.py       # Menu principal do sistema, interface em terminal
    ├── cliente.py        # CRUD completo da entidade Cliente
    ├── hotel.py          # CRUD e gestão da entidade Hotel
    ├── quarto.py         # CRUD completo da entidade Quarto
    ├── reserva.py        # CRUD completo da entidade Reserva
    └── utils.py          # Funções auxiliares (geração de IDs, validação de datas)
Descrição de cada ficheiro

main_app.py

Contém o menu interativo em terminal.
Responsável apenas por apresentar opções, recolher dados do utilizador e chamar funções dos outros módulos.

cliente.py

CRUD completo da entidade Cliente: criar, listar, consultar, atualizar e remover clientes.
Inclui validações como data de nascimento e geração automática de ID.
Armazenamento em dicionário na memória.

hotel.py

CRUD completo da entidade Hotel: criar, listar, consultar, atualizar e remover hotéis.
Inclui validações como geração automática de ID.
Armazenamento em dicionário na memória.

quarto.py

CRUD completo da entidade Quarto: criar, listar, consultar, atualizar e remover quartos.
Campos: número do quarto, descrição, tipo (suite, solteiro, casal), preço.

reserva.py

CRUD completo da entidade Reserva: criar, listar, consultar, atualizar e remover reservas.
Campos: ID da reserva, data check-in, data check-out, lista de quartos, valor da reserva.

utils.py

Funções auxiliares para todo o projeto:
Geração automática de IDs
Validação de datas no formato YYYY-MM-DD
▶️ Como Executar o Projeto

1️⃣ Garantir que o Python está instalado.

2️⃣ Navegar até a pasta src no terminal:

cd gestor_hotel/src

3️⃣ Executar o menu principal:

python main_app.py

4️⃣ Utilizar o menu apresentado para gerir clientes, hotéis, quartos e reservas.

📚 Conceitos Trabalhados
Funções
Dicionários
Módulos Python e importação entre ficheiros
Validação de dados
Estruturas condicionais
Ciclos (while)
Operações CRUD
👨‍🏫 Utilização

Este projeto foi desenvolvido para:

Introdução prática ao CRUD
Exercícios guiados
Avaliação prática
Preparação para projetos maiores
📄 Licença Pedagógica

Projeto desenvolvido exclusivamente para fins educativos no curso GPSI – 10.º ano.

Pode ser reutilizado e adaptado livremente.
