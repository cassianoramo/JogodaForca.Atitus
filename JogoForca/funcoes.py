import os

def limpaTela():
    os.system("cls")


def jogoForca():
    print("Jogo da Forca!!!")

def convertAst(palavra):
    return '*' * len(palavra)