nums = [17,33,23,11,8,15,9]
maior = nums [0]
menor = nums [0]

for num in nums:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
        
print ("O menor numero é: ", menor, "\n O maior numero é: ", maior)