cpf = '746.824.890-70'.replace('.', '').replace('-', '')
nove_digitos = cpf[:9]
contador1 = 10
resultado1 = 0

# Validando se o cpf não possui todos os dígitos iguais
if cpf[0] * len(cpf) == cpf:
    
    # Calculando primeiro dígito
    for digito1 in nove_digitos:
        resultado1 += int(digito1) * contador1
        contador1 -= 1
        
    resultado1 = (resultado1 * 10) % 11
    primeiro_digito = resultado1 if resultado1 < 10 else 0

    # Calculando segundo dígito
    contador2 = 11
    resultado2 = 0
    dez_digitos = cpf[:10]

    for digito2 in dez_digitos:
        resultado2 += int(digito2) * contador2
        contador2 -= 1
        
    resultado2 = (resultado2 * 10) % 11
    segundo_digito = resultado2 if resultado2 < 10 else 0

    cpf_calculado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

    # Validando CPF
    if(cpf == cpf_calculado):
        print("CPF Válido!")
    else: 
        print("CPF Inválido!")

else: 
    print("CPF Válido!")