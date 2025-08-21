print ('Vamos calcular o menor numero.\n')

#Coleta dos dados
numero_1 = int(input('Digite o 1° n°: '))
numero_2 = int(input('Digite o 2° n°: '))
numero_3 = int(input('Digite o 3° n°: '))

#comparação dos dados
if numero_1 == numero_2:
    print ('Os numeros inseridos não são diferentes.')
else:
    if numero_1 == numero_3:
        print ('Os numeros inseridos não são diferentes.')
    else: 
        if numero_2 == numero_3:
            print ('Os numeros inseridos não são diferentes.')
        else:
            menor = numero_1

        if numero_2 > menor:
            menor = numero_2

        if numero_2 > menor:
            menor = numero_2
        
        print ('O menor numero é:',menor)