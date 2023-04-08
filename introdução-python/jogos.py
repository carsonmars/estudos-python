import forca
import advinhacao

def escolha_jogo():
    print("***********************************")
    print("Escolha o seu jogo!")
    print("***********************************")

    print("(1) Forca      (2) Advinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        advinhacao.jogar()
    else:
        print("Desculpe, ainda não tem essa opção!")

if(__name__ == "__main__"): #Esse teste verifica se o arquivo está sendo executado diretamente ou como módulo.
    escolha_jogo()