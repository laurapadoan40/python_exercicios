def calcularMedia(nota1, nota2, nota3, nota4):
    media = (nota1, nota2, nota3, nota4)/4
    return media

def resultado(media):
    if (media >= 5):
        return "Aprovado"
    else:
        return "Reprovado"
    
print("Calculadora de Média")
n1 = float(input("Digite a 1º nota: "))
n2 = float(input("Digite a 2º nota: "))
n3 = float(input("Digite a 3º nota: "))
n4 = float(input("Digite a 4º nota: "))
