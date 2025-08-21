from typing import List

print('Vamos calcular sua média na matéria X!')

# Receber as notas
nota_1 = float(input('\nInsira sua nota do 1° Bimestre (2025): '))
nota_2 = float(input('Insira sua nota do 2° Bimestre (2025): '))
nota_3 = float(input('Insira sua nota do 3° Bimestre (2025): '))
nota_4 = float(input('Insira sua nota do 4° Bimestre (2025): '))

# Somar e calcular a média
notas: List[float] = [nota_1, nota_2, nota_3, nota_4]
nota_total = sum(notas)
nota_media = nota_total / len(notas)  # Corrigido para len(notas)

print ('Sua nota final é: \n', nota_media)
# Validar aprovação
if nota_media >= 75:
    print('Parabéns! Você foi aprovado!')
elif nota_media < 75 and nota_media > 45:
    print('Faça a prova de Recuperação!')
else:
    print('Você está reprovado...')
