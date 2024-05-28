listas_compras = []

num_produtos = int(input("Quantos produtos vc deseja adicionar?": ))

for i in range (num_produtos):
    produto = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    listas_compras.append([produto,quantidade])

    print("Lista de cmpras: ")
    for produto, quantidade: in listas_compras
    print ;(f"Produto: {produto} - Qtd: {quantidade}")
    