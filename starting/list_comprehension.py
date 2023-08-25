precos = [100, 200, 300, 400, 500]

# Mapping
novos_precos = [preco * 1.5 for preco in precos]
print(novos_precos)

# Filtering
valor_imposto = [preco * 0.3 for preco in precos if preco >= 250]
print(valor_imposto)
