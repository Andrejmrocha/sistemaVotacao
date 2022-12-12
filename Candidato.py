class Candidato:

    def __init__(self, nome, numero, partido):
        self.nome = nome
        self.numero = numero
        self.partido = partido
        self.votos = 0

    def toString(self):
        return self.nome + " - " + self.numero + " (" + self.partido + ") "

    def getNome(self):
        return self.nome

    def getNumero(self):
        return self.numero

    def setVoto(self):
        self.votos += 1

    def getVotos(self):
        return self.votos
