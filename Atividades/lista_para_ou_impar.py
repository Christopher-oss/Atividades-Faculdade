
pares = []
impares = []

for i in range (5):
    num = int (input ("Digite um Numero: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        if num %2 == 1:
            impares.append(num)
            
print ("numeros pares:", pares, "\n numeros impares: ", impares)

