import random

def jogar(): #def serve para declaração uma função.

    print("***********************************")
    print("Bem vindo(a) ao jogo da Advinhação!")
    print("***********************************")

    numero_secreto = random.randrange(1,101) #Função adquirida pela importação da sua biblioteca correspondente.
    pontos = 1000

    print("Qual nível de dificuldade? ")
    print("(1) - Fácil  (2) - Médio  (3) - Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2): #Elif um else com if e espaço para condição.
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #Interpolação de String

        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Erro, você deve digitar um número entre 1 e 100.")
            continue #Sai da iteração e passa para próxima sem finalizar a execução do programa.

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print("Você digitou ", chute)

        if (acertou):
            print("Parabéns!! Você acertou o número secreto. Total de pontos: {}".format(pontos))
            break #Força a interrupção do programa.
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) #Função abs para retornar o número absoluto
            pontos = pontos - pontos_perdidos

    print(numero_secreto)
    print("Fim do jogo")

if (__name__ == "__main__"): #Esse teste verifica se o arquivo está sendo executado diretamente ou como módulo.
    jogar()