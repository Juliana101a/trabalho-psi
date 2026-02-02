

# O nosso 'inventário' de nomes
def jogo_gestor():

    base_de_dados = []

    print("=" * 40)
    print("🏆 BEM-VINDO AO DESAFIO DO GESTOR!")
    print("Aprenda a manipular listas enquanto joga.")
    print("=" * 40)

    while True:
        print("\n--- MENU DE COMANDOS ---")
        print("1. [ADICIONAR] - Ganhe um novo aliado")
        print("2. [REMOVER]   - Remova um nome da equipa")
        print("3. [LISTAR]    - Ver todos os membros")
        print("4. [PROCURAR]  - Localizar um membro específico")
        print("0. [SAIR]      - Encerrar missão")

        escolha = input("\nQual é a sua jogada? ")

        # REQUISITO 1: Adicionar nome
        if escolha == "1":
            novo_nome = input("⚔️ Digite o nome do novo aliado: ").strip()
            if novo_nome:
                base_de_dados.append(novo_nome)
                print(f"✅ SUCESSO! '{novo_nome}' foi invocado para a lista.")
            else:
                print("❌ ERRO: O nome não pode estar vazio!")

        # REQUISITO 2: Remover nome
        elif escolha == "2":
            alvo = input("🗑️ Digite o nome que deseja remover: ").strip()
            if alvo in base_de_dados:
                base_de_dados.remove(alvo)
                print(f"⚠️ AVISO: '{alvo}' saiu da equipa.")
            else:
                print(f"❓ O nome '{alvo}' não existe no nosso registo.")

        # REQUISITO 3: Listar todos os nomes
        elif escolha == "3":
            print("\n📋 RELATÓRIO ATUAL DA EQUIPA:")
            if not base_de_dados:
                print("--- A lista está deserta no momento ---")
            else:
                for i, nome in enumerate(base_de_dados, 1):
                    print(f" Slot {i}: {nome}")
            print(f"Total de membros: {len(base_de_dados)}")

        # REQUISITO 4: Procurar um nome
        elif escolha == "4":
            busca = input("🔍 Quem você está a tentar localizar? ").strip()
            if busca in base_de_dados:
                posicao = base_de_dados.index(busca) + 1
                print(f"⭐ ENCONTRADO! '{busca}' está posicionado no Slot {posicao}.")
            else:
                print(f"🕵️ O nome '{busca}' não foi avistado em lado nenhum.")

        # Saída do Jogo
        elif escolha == "0":
            print("\n💾 Progresso guardado. Missão terminada!")
            break

        else:
            print("🚫 Comando inválido! Escolha entre 0 e 4.")

# Iniciar o desafio
if __name__ == "__main__":
    jogo_gestor()
