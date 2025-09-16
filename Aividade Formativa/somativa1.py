 
usuario = str(input("Insira seu nome: "))
estudantes = []
print("\nSeja Bem-Vindo", usuario,"!")

while True:
    
    
    print("\n***MENU INICIAL***","\n\nESCOLHA UMA DAS OPÇÕES:","\n(1) Gerenciar Estudantes.","\n(2) Gerenciar Professores.","\n(3) Gerenciar Disciplinas.","\n(4) Gerenciar Turmas.","\n(5) Gerenciar Matrículas.","\n\n(0) SAIR DO SISTEMA!")
    
    #Menu Inicial
    try:
        opcao = int(input("Insira a Opção Desejada: "))
    except ValueError:
        print("Opção Inserida não encontrada. Tente novamente!")
    if opcao == 1:
        
        while True:
            print ("\n***MENU DE OPERAÇÕES***","\n\nESCOLHA UMA DAS OPÇÕES:","\n(1) Incluir.\n(2) Listar.\n(3) Atualizar.\n(4) Excluir.\n\n(0) Voltar ao Menu Principal.")
            try:
                opcao_dois = int(input("Insira a Opção Desejada: "))
            except ValueError:
                print("\nOpção Inserida não encontrada. Tente novamente!")
                break

            if opcao_dois == 1:
                print("Opção escolhida: INCLUIR ALUNO")
                try:
                    aluno = str(input("Insira o nome do Aluno: "))
                    estudantes.append(aluno)
                except ValueError:
                    print("Opção Inserida não encontrada. Tente novamente!")
                    break                    

            elif opcao_dois == 2:
                print("\nOpção escolhida: LISTA DE ESTUDANTES")
                if not estudantes:
                    print("\nAinda não há nenhum nome cadastrado...")
                    try:
                        aluno = str(input("Cadastre um novo Aluno: "))
                        estudantes.append(aluno)
                    except ValueError:
                        ("Hmm, parece que tivemos uma situação inesperada. Tente novamente")
                        break
                else:
                    for estudante in estudantes:
                        print(estudante)
                        
            elif opcao_dois == 3:
                print("\nEM DESENVOLVIMENTO")
                break
            
            if opcao_dois == 4:
                print("Opção escolhida: EXCLUIR ALUNO")
                try:    
                    estudante_excluido = str(input("Digite o nome do Aluno que deseja EXCLUIR:"))
                    if estudante_excluido == estudantes:
                        estudantes.pop(estudante_excluido)    
                except ValueError:
                    print("Hmm, parece que tivemos uma situação inesperada. Tente novamente")
                    break
                    
    elif opcao in [2,3,4,5]:
        print ("EM DESENVOLVIMENTO. Retornando ao MENU inicial!")
        
    elif opcao == 0:
        print("Saindo do sistema...")
        break
    else:
        print ("Opção escolhida não encontrada. Tente Novamente!") 
                 
                