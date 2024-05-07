valor_unitario = 12.5
quantidade = int(input("Quantidade de camisas: "))
valor_total = valor_unitario * quantidade
if quantidade <= 5:
    valor_total = valor_total * 0.97
else:
    if quantidade <= 10:
        valor_total = valor_total * 0.97
    else:
        valor_total = valor_total * 0.93 
print(f"valor total da compra: R${valor_total:.02f}")
