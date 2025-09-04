nomes  = []

while True:
    nome = input ("Digite o Nome: ")
    if nome == "Sair":
        break
    sobrenome = input ("Digite o Sobrenome: ")
    
    nome_completo = [nome, sobrenome]
    nomes.append(nome_completo)
    
for nome in nomes: 
    print (nome[1] + "," + nome[0])  