valor_unitario = 12.5
quantidade = int(input("Digite a quantidade: "))
valor_total = valor_unitario * quantidade
if quantidade <= 5:
    valor_total = valor_total * 0.97
elif quantidade <= 10:
    valor_total = valor_total * 0.95
else:
    valor_total = valor_total * 0.93
print(f"Valor Total R$ {valor_total}")
