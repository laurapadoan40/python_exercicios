nota1 = int(input("Informe a nota do 1º bimestre (0-100): "))
nota2 = int(input("Informe a nota do 2º bimestre (0-100): "))
media = (nota1+nota2) / 2
if media >= 60:
    print(f"Você foi aprovado com a media de {media}")
else:
    print(f"Você não foi aprovado, sua media é {media}")
