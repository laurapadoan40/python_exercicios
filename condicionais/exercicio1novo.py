# Entrada de Dados 
n = int(input("Digite quantos números você quer calcular a média: "))
soma = 0 
iteracao = 1 
while iteracao <= n:
    numero = float(input("Digite um número: "))
    soma += numero
    iteracao += 1
print(f"O valor da média é: {soma/n}")
