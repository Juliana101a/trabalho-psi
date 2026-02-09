# ================================
# MINI PROJETO 3
# GESTOR DE UMA TURMA 🎓
# ================================

def mostrar_menu():
    print("\n" + "=" * 45)
    print("📚 GESTOR DE UMA TURMA")
    print("=" * 45)
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Procurar aluno")
    print("4 - Listar alunos")
    print("5 - Simular aula 🎮")
    print("0 - Sair")
    print("=" * 45)


def gestor_turma():
    turma = []  # lista principal

    print("=" * 45)
    print("👋 Bem-vindo ao Gestor de uma Turma!")
    print("Aprenda Python enquanto gere alunos.")
    print("=" * 45)

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        # ADICIONAR
        if opcao == "1":
            nome = input("Nome do aluno: ").strip()
            if nome:
                turma.append(nome)
                print(f"✅ Aluno '{nome}' adicionado com sucesso!")
            else:
                print("⚠ Nome inválido.")

        # REMOVER
        elif opcao == "2":
            if not turma:
                print("⚠ A turma está vazia.")
            else:
                nome = input("Nome do aluno a remover: ")
                if nome in turma:
                    turma.remove(nome)
                    print("f🗑 Aluno '{nome}' removido.")
                else:
                    print("❌ Aluno não encontrado.")

        # PROCURAR
        elif opcao == "3":
            nome = input("Nome do aluno a procurar: ")
            if nome in turma:
                posicao = turma.index(nome) + 1
                print(f"🔍 Aluno encontrado na posição {posicao}.")
            else:
                print("❌ Aluno não existe na turma.")

        # LISTAR
        elif opcao == "4":
            if not turma:
                print("📭 Nenhum aluno registado.")
            else:
                print("\n📋 Lista de Alunos:")
                for i in range(len(turma)):
                    print(f"{i + 1}. {turma[i]}")

        # JOGO / SIMULAÇÃO
        elif opcao == "5":
            if not turma:
                print("😴 Não há alunos para a aula.")
            else:
                print("\n🎮 SIMULAÇÃO DE AULA")
                print("O professor faz uma pergunta...")
                aluno = turma[0]
                print(f"🙋 {aluno} responde corretamente!")
                print("🏆 Aula concluída com sucesso!")

        # SAIR
        elif opcao == "0":
            print("\n👋 Programa encerrado. Bom trabalho!")
            break

        # OPÇÃO INVÁLIDA
        else:
            print("⚠ Opção inválida. Tente novamente.")


# INÍCIO DO PROGRAMA
if __name__ == "__main__":
    gestor_turma()

