def calcularMedia(nota1,nota2,nota3,nota4):
    media = (nota1+nota2+nota3+nota4)/4
    return media

def resultado(media):
    if (media >= 5):
        return "Aprovado"
    else:
        return "Reprovado"
    
print("Calculadora de Média")

aluno_notas = []
aluno_notas.append(input("Digite o nome do aluno: "))

for i in range(4)
  nota = float(input(f"Digite a {i+1}ª nota: "))
  
m = calcularMedia(aluno_notas)
r = resultado(m)
print(f"Sua média é {m}, e você foi {r}")