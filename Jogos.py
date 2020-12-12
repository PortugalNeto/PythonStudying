import forca
import adivinhacao
print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************\n")

print("(1) para Forca e (2) para Adivinhação!")
jogo = int(input("Qual o jogo? "))

if(jogo == 1):
    print("Jogando Forca!")
    forca.jogar()
elif(jogo == 2):
    print("Jogando Adivinhação!")
    adivinhacao.jogar()
