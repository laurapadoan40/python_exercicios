# Desafio
print("Cálculo de Grandezas Elétricas")
print("1. Tensão (em Volt)\n")
print("2. Resistência (em Ohm)\n")
print("3. Corrente (em Ampére)\n")
grandeza = (input("Escolha uma das grandezas:\n -1.\n -2.\n -3.\n"))
if grandeza == "1":
    resistencia1 = float(input("Informe a resistência: "))
    corrente1 = float(input("Informe a corrente: "))
    tensao1 = (corrente1 * resistencia1)
    print(f"A sua tensão é de {tensao1}")
elif grandeza == "2":
    tensao2 = float(input("Informe a tensao: "))
    corrente2 = float(input("Informe a corrente: "))
    resistencia2 = (tensao2 / corrente2)
    print(f"A sua resistência é de {resistencia2}")
elif grandeza == "3":
    resistencia3 = float(input("Informe a resistência: "))
    tensao3 = float(input("Informe a tensao: "))
    corrente3 = (tensao3 / resistencia3)
    print(f"A sua corrente é de {corrente3}")
else :
    print(f"Resposta inválida!!!")


