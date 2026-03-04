#tipos de dados homogeneos
idade = 10 
nome  = "João"

print(idade)
print(nome)

#criação de uma classe, obstração de um tipo  de dados heterogêneo
class Aluno:
    def __init__(self, ):
        self.nome = nome
        self.idade = idade
        self.prouni = False


#crio uma variavel ou instancia de um objeto classe aluno
aluno = Aluno()
aluno.nome = "Maria"
aluno.idade = 20
aluno.prouni = True

aluno2 = Aluno()
aluno2.nome = "Maria"
aluno2.idade = 20
aluno2.prouni = True


aluno3 = Aluno()
aluno3.nome = "Maria"
aluno3.idade = 20
aluno3.prouni = True


print(aluno3.nome)
print(aluno3.idade)
print(aluno3.prouni)