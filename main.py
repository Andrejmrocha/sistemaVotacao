from Urna import *
from Candidato import *

urna2022 = Urna(10, 123)

while True:

    print("1 - Cadastrar candidato")
    print("2 - Ver candidatos")
    print("3 - Iniciar eleição")
    print("4 - Verificar votos")
    print("5 - Validar vencedor")
    print("6 - Encerrar aplicativo")
    escolha = input()

    if escolha == "1":
        nome = input('Nome:\n')
        numero = input('Número:\n')
        partido = input('Partido:\n')
        urna2022.novoCandidato(Candidato(nome, numero, partido))

    elif escolha == "2":
        for i in urna2022.Candidatos:
            print(i.toString())

    elif escolha == "3":
        while True:
            voto = input("Número do candidato:\n")
            if voto == "break":
                break
            print(urna2022.getCandidato(voto).toString())
            print('Confirma: ')
            escolha = input('s ou n:\n')
            if escolha == 's':
                urna2022.getCandidato(voto).setVoto()

    elif escolha == "4":
        for i in urna2022.Candidatos:
            print(i.toString() + ': ')
            print(str(i.getVotos()) + ' voto(s)')

    elif escolha == "5":
        maisVotado = urna2022.Candidatos[0]
        i = 0
        while i < len(urna2022.Candidatos):

            if i == len(urna2022.Candidatos) - 1:
                break

            elif maisVotado.getVotos() > urna2022.Candidatos[i+1].getVotos():
                i += 1

            else:
                maisVotado = urna2022.Candidatos[i+1]
                i += 1
        print(maisVotado.getNome() + ' foi o mais votado, ' + str(maisVotado.getVotos()) + ' votos.')

    elif escolha == "6":
        break
