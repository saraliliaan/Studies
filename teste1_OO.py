#class PrimeiraClasse:
#    nome = None
#    
#    def imprimir_mensagem(self):
#        print ("Olá, seja bem vindo!")
#
#objeto1 = PrimeiraClasse()
#objeto1.nome = "Aluno 1"
#
#print (objeto1)
#objeto1.imprimir_mensagem()

class FuncionarioTecnico:
    def __init__(self, status):
        self.status = status
        self.nivel = 'Técnico'
func1 = FuncionarioTecnico('Ativo')
func2 = FuncionarioTecnico('Licença Mestrado')
print(func1.nivel)
print(func2.nivel)
print(func1.status)
print(func2.status)