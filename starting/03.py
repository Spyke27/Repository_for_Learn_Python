palavraSecreta = "perfume"
tentativas = 0
acertos = ""
palavra = ""

while len(acertos) < len(palavraSecreta):
    tentativas += 1
    letra = input("Digite uma letra: ")
    
    if letra in palavraSecreta:
        acertos += letra
            
    for letra in palavraSecreta:
        if letra in acertos:
            palavra += letra
        else:
            palavra += "*"
    
print("Você Ganhou!")
print(f'Tentativas: {tentativas}')
            
        
    