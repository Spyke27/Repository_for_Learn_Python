numeros = range(0, 20, 2)
num = 0

for numero in numeros:
    print(f'{numero} elevado ao quadrado é {numero ** 2}.')
    
while num < 20:
    print(f'{2**num}')
    num = num + 1