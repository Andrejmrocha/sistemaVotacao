from Urna import *
from Candidato import *

urna2022 = Urna(10, 123)

while True:

    print("1 - Cadastrar candidato")
    print("2 - Ver candidatos")
    print("3 - Iniciar eleição")
    print("4 - Encerrar aplicativo")
    escolha = input()

    if escolha == "1":
        nome = input('Nome:\n')
        numero = input('Número:\n')
        partido = input('Partido:\n')
        urna2022.novoCandidato(Candidato(nome, numero, partido))

    elif escolha == "2":
        for i in urna2022.Candidatos:
            print(i.toString())

    elif escolha == "4":
        break


