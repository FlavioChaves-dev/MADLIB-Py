class Personagem:
    def __init__(self, nome, classe, nivel):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel

personagem = Personagem("Aragorn", "Guerreiro", 20)
personagem.nome = "Aragorn"
personagem.classe = "Guerreiro" 
personagem.nivel = 20

personagem2 = Personagem("Malenia", "cavaleira", 32)
personagem2.nome = "Malenia"
personagem2.classe = "Cavaleira" 
personagem2.nivel = 89

personagem3 = Personagem("Lorde", "tank", 35)
personagem3.nome = "Lorde"
personagem3.classe = "Tank" 
personagem3.nivel = 35

print(personagem2.nome)
print(personagem2.classe)
print(personagem2.nivel)