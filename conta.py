class Conta: 
    def __init__(self):
        self.numero = 0
        self.titular = ""
        self.saldo = 0.0
        self.CPF = ""

conta1 = Conta()
conta1.numero = 123
conta1.titular = "João"
conta1.saldo = 1000.0
conta1.CPF = "CPF 123.456.789-00"

conta2 = Conta()
conta2.numero = 789
conta2.beneficiario = "Flavio"
conta2.saldo = 589.89
conta2.CPF = "987.654.321-00"
print()

print("Bem vindo ao Banco do Brasil!")
print()
print("Nº da conta:",conta1.numero)
print("Titular conta:",conta1.titular)  
print("Saldo Atual:", conta1.saldo)
print("CPF:", conta1.CPF)

print()

print("Beneficiario do titular:",conta2.beneficiario)
print()
print("Nº da conta:", conta2.numero)
print("Saldo Atual:", conta2.saldo)
print("CPF:", conta2.CPF)