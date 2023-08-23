"""Mini Forca"""

PALAVRA_SECRETA = 'perfume'
TENTATIVAS = 0
ACERTOS = ""
PALAVRA = ""

while len(ACERTOS) < len(PALAVRA_SECRETA):
    TENTATIVAS += 1
    letra = input("Digite uma letra: ")

    if letra in PALAVRA_SECRETA:
        ACERTOS += letra

    for letra in PALAVRA_SECRETA:
        if letra in ACERTOS:
            PALAVRA += letra
        else:
            PALAVRA += "*"

print("Você Ganhou!")
print(f"Tentativas: {TENTATIVAS}")
