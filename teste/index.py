nome = "rodrigo"

print(f'Seu nome é {nome.capitalize()}')

nome = nome.upper()
print(f'Seu nome invertido é {nome[::-1]}')

if ' ' in nome:
    print('Seu nome contém espaços!')
else:
    print('Seu nome não contém espaços!')

print(f'Seu nome tem {len(nome)} letras.')
print(f'A primeira letra do seu nome é {nome[0]}.')
print(f'A última letra do seu nome é {nome[len(nome)-1]}.')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero in numeros:
    print(f'{numero} elevado ao quadrado é {numero ** 2}.')
        

