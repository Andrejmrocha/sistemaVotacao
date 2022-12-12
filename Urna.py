import Candidato


class Urna:

    def __init__(self, zona, sessao):
        self.zona = zona
        self.sessao = sessao
        self.Candidatos = []

    def novoCandidato(self, candidato):
        self.Candidatos.append(candidato)

    def getCandidato(self, numero):
        for i in self.Candidatos:
            if i.getNumero() == numero:
                return i
