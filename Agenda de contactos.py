def mostrar_menu():
    print("\n===== AGENDA =====")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Sair")


def adicionar(agenda):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    agenda[nome] = telefone  # chave -> valor
    print(f"✔ {nome} adicionado.")


def listar(agenda):
    if not agenda:
        print("Agenda vazia.")
        return
    for nome, telefone in agenda.items():
        print(f"{nome}: {telefone}")


def buscar(agenda):
    nome = input("Buscar nome: ")
    if nome in agenda:
        print(f"{nome} -> {agenda[nome]}")
    else:
        print("Contato não encontrado.")


# Programa principal
agenda = {}  # dicionário vazio

while True:
    mostrar_menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar(agenda)
    elif opcao == "2":
        listar(agenda)
    elif opcao == "3":
        buscar(agenda)
    elif opcao == "4":
        print("Até logo!")
        break
    else:
        print("Opção inválida.")