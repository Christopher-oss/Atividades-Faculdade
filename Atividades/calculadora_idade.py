#entrada de dados
data_nascimento = input ('Digite sua data de NASCIMENTO (dd/mm/aaaa): ')
data_atual = input ('Digite a data de HOJE (dd/mm/aaaa): ')

#separação da data de NASCIMENTO (dd/mm/aaaa)
dia_nascimento = int (data_nascimento[:2])
mes_nascimento = int (data_nascimento[3:5])
ano_nascimento = int (data_nascimento[6:])

#separação da data ATUAL (dd/mm/aaaa)
dia_atual = int (data_atual[:2])
mes_atual = int (data_atual[3:5])
ano_atual = int (data_atual[6:])

#calculo da idade
idade = ano_atual - ano_nascimento

#verificador do mes de aniversario
if mes_nascimento > mes_atual:
    idade -= 1
#verificador do dia de aniversario
if dia_nascimento > dia_atual:
    idade -= 1

print ('Sua idade é: ', idade, 'anos')