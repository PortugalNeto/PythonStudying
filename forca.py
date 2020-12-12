import random
def jogar():



    imprime_mensagem_abertura()

    palavra_secreta = escolha_palavra_secreta()


    letras_acertadas = ["_" for letra in palavra_secreta]


    comprimento = len(palavra_secreta)
    print("A palavra secreta tem", comprimento, "letras!")
    print(letras_acertadas)
    enforcou = False
    acertou = False
    tentativas = 0

    while (not acertou and not enforcou):

        print("Jogando...")
        chute = input("Chute uma letra: ").lower().strip()
        index = 0
        tentativas += 1
        for letra in palavra_secreta:

            if (chute == letra):
                letras_acertadas[index] = letra

            index += 1
        print(letras_acertadas)
        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas

        if (acertou):
            print("Parabéns, você acertou!")
            break
        elif (enforcou):
            print("Você foi enforcado. A palavra era {}.".format(palavra_secreta))
            break

        print("Você ainda tem", 6 - tentativas, "tentativas para acertar a palavra.")

    print("Fim do Jogo!")

def imprime_mensagem_abertura():
    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************\n")

def escolha_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavra = []
    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)
    arquivo.close()
    palavra_secreta = palavra[random.randrange(0, 6)]
    return palavra_secreta

if (__name__ == "__main__"):
    jogar()

