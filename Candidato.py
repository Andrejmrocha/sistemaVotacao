class Candidato:

    def __init__(self, nome, numero, partido):
        self.nome = nome
        self.numero = numero
        self.partido = partido

    def toString(self):
        return self.nome + " - " + self.numero + " (" + self.partido + ") "
