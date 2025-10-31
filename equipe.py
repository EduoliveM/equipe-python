equipe = []

def adicionar_membro():
    nome = input("Digite o nome do membro da equipe: ").strip()
    salario = float(input("Digite o salário do membro: "))
    membro = {"nome": nome, "salario": salario}
    equipe.append(membro)
    print(f"\n✅ Membro {nome} adicionado com sucesso!\n")

def listar_equipe():
    if not equipe:
        print("\n⚠️ Nenhum membro cadastrado.\n")
        return
    print("\n📋 Lista da Equipe:")
    for i, m in enumerate(equipe, start=1):
        print(f"{i}. {m['nome']} - R$ {m['salario']:.2f}")
    print()

def buscar_membro():
    nome_busca = input("Digite o nome do membro que deseja buscar: ").strip().lower()
    encontrados = [m for m in equipe if nome_busca in m['nome'].lower()]
    if encontrados:
        print("\n🔍 Membros encontrados:")
        for m in encontrados:
            print(f"- {m['nome']} | Salário: R$ {m['salario']:.2f}")
    else:
        print("\n❌ Nenhum membro encontrado com esse nome.")
    print()

def calcular_media_salarial():
    if not equipe:
        print("\n⚠️ Nenhum membro cadastrado para calcular a média.\n")
        return
    media = sum(m['salario'] for m in equipe) / len(equipe)
    print(f"\n💰 A média salarial da equipe é: R$ {media:.2f}\n")

def menu():
    while True:
        print("=== MENU DA EQUIPE ===")
        print("1. Adicionar membro")
        print("2. Listar equipe")
        print("3. Buscar membro por nome")
        print("4. Calcular média salarial")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_membro()
        elif opcao == "2":
            listar_equipe()
        elif opcao == "3":
            buscar_membro()
        elif opcao == "4":
            calcular_media_salarial()
        elif opcao == "5":
            print("\n👋 Encerrando o programa. Até logo!")
            break
        else:
            print("\n❌ Opção inválida. Tente novamente.\n")

menu()