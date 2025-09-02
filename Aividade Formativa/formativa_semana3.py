usuario = input("Insira seu nome: ")

while True:
    print(f"\nSeja Bem-Vindo, {usuario}!\n")
    print("ESCOLHA UMA DAS OPÇÕES:")
    print("(1) Gerenciar Estudantes.")
    print("(2) Gerenciar Professores.")
    print("(3) Gerenciar Disciplinas.")
    print("(4) Gerenciar Turmas.")
    print("(5) Gerenciar Matrículas.")
    print("(0) SAIR DO SISTEMA!")

    opcao = int(input("\nDIGITE A OPÇÃO DESEJADA: "))

    if opcao in [1, 2, 3, 4, 5]:
        print(f"\nOPÇÃO ESCOLHIDA: {opcao}")
        print("(1) Incluir.\n(2) Listar.\n(3) Atualizar.\n(4) Excluir.\n(0) Voltar ao Menu Principal.")
        segunda_opcao = int(input("DIGITE A OPÇÃO DESEJADA: "))

        if segunda_opcao in [1, 2, 3, 4]:
            print(f"\nOPÇÃO ESCOLHIDA: {segunda_opcao}")
            print("EM DESENVOLVIMENTO\nEscolha uma das opções abaixo:\n(0) Voltar ao Menu Principal.")

            while True:
                opcao_final = int(input("DIGITE A OPÇÃO DESEJADA: "))
                if opcao_final == 0:
                    break;  # volta ao menu principal
                else:
                    print("\nOpção Inválida! Digite 0 para voltar ao menu principal.")

        elif segunda_opcao == 0:
            continue  # volta ao menu principal
        else:
            print("\nOpção Inválida!")

    elif opcao == 0:
        print("Saindo do sistema...")
        break
    else:
        print("\nOpção Inválida!")