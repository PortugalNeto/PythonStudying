def jogar():

    import random

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************\n")

    nivel = input("Enter your level: easy, medium or difficult. ")
    if (nivel == "easy"):
        tries = 7
    elif (nivel == "médio"):
        tries = 5
    elif (nivel == "difícil"):
        tries = 3
    numero_secreto = random.randrange(1, 101)

    for rodada in range(1, tries + 1):
        print("Tentativa {} de {}\n".format(rodada, tries))
        guess = int(input("Digite um número inteiro entre 1 e 100: "))
        print("Você digitou", guess_str, "\n")

        if (guess < 1 or guess > 100):
            print("Você deve digitar um número entre 1 e 100!\n")
            continue

        if (guess == numero_secreto):
            print("Você acertou!")
            break
        else:
            if(guess > numero_secreto):
                print("Seu chute foi acima do número certo..\n")
            elif(guess < numero_secreto):
                print("Seu chute foi abaixo do número certo..\n")
    print("Fim do jogo. O número correto é", numero_secreto)
