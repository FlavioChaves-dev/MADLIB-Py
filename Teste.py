print("Bem vindo ao Portal de Aprovados!")
print()
nome = input("Digite seu nome:")
nota = float(input("Digite sua nota:"))
if nota >= 7:
    print("Parabéns", nome, "você foi aprovado!")
else:
    print("Que pena", nome, "você não foi aprovado!")
if nota == 10:
    print("UAU!" ,nome, "você tirou uma otima nota!")


