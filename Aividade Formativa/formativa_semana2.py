#Variaveis Menu de Opções
voltar = 0
incluir = 1
listar = 2
atualizar = 3
excluir = 4


# Apresentação 
print('Seja Bem vindo!')
print('Como você se chama?')
nome = input('\nDigite seu nome: ')

#Menu de opções
print('\nOlá', nome,'. Escolha uma das opções abaixo: ')
print('\n(0) SAIR\n(1) Gerenciar Estudante!\n(2) Gerenciar Professores!\n(3) Gerenciar Disciplinas!\n(4) Gerenciar Turmas!\n(5) Gerenciar Matriculas!\n ')

#Ações do Menu
opcao_desejada = int(input('Informe a Opção Desejada: '))

if opcao_desejada == 1:
    print('Gerenciar Estudantes: ')
    print(voltar'(0)'\n incluir '(1)')
    acao_conta = int(input('Qual ação deseja realizar: '))
elif opcao_desejada == 2:
    print('Gerenciar Professores: ')
    print('\n(1) Incluir!\n(2) Listar!\n(3) Atualizar!\n(4) Excluir!\n(0) Voltar ao Menu Principal.\n')
    acao_conta = int(input('Qual ação deseja realizar: '))
elif opcao_desejada == 3:
    print('Gerenciar Disciplinas: ')
    print('\n(1) Incluir!\n(2) Listar!\n(3) Atualizar!\n(4) Excluir!\n(0) Voltar ao Menu Principal.\n')
    acao_conta = int(input('Qual ação deseja realizar: '))
elif opcao_desejada == 4:
    print('Gerenciar Turmas: ')
    print('\n(1) Incluir!\n(2) Listar!\n(3) Atualizar!\n(4) Excluir!\n(0) Voltar ao Menu Principal.\n')
    acao_conta = int(input('Qual ação deseja realizar: '))
elif opcao_desejada == 5:
    print('Gerenciar Matriculas: ')
    print('\n(1) Incluir!\n(2) Listar!\n(3) Atualizar!\n(4) Excluir!\n(0) Voltar ao Menu Principal.\n')
    acao_conta = int(input('Qual ação deseja realizar: '))
elif opcao_desejada == 0:
    print('SAIU DO SISTEMA!')

else:
    input('Desculpe. Opção não encontrada, tente novamente!')


