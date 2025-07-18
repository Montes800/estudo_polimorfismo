#polimorfismo com herança
class Passaro:
    def voar(self):  # todo passaro voar
        print("voando...")

class Pardal(Passaro):  # herdando de Passaro (agora corrigido)
    def voar(self):
        print("Pardal voa")
        #super().voar()  # chama o voar da classe pai (Passaro)

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")  # sobrescreve o método voar da classe Passaro

def plano_de_voo(passaro):  # passaro objeto
    passaro.voar()  # metodo voar
# passaro define o metodo voar
# função que aceita qualquer objeto que implemente o método voar (polimorfismo)

class Aviao(Passaro):#exemplo ruim para herança do metodo voar
    def voar(self):
        print("Avião decolando...")
# Criando os objetos
#pardal = Pardal()
#avestruz = Avestruz()

# Chamando a função com os objetos
plano_de_voo(Pardal())     # exibir voa
plano_de_voo(Avestruz())   # exibir nao voa
plano_de_voo(Aviao())