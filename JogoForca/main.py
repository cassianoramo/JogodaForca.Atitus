from funcoes import limpaTela,jogoForca,convertAst

while True:
    limpaTela()
    jogoForca()

    while True:
        desafiante = input("Digite o nome do desafiante: ").strip()
        competidor = input("Digite o nome do competidor: ").strip()
        if competidor == '' or desafiante == '':
            print("Os campos desafiante e competidor não podem estar em branco")
        else:
            break
    limpaTela()
    jogoForca()

    while True:
        palavraChave = input("Desafiante digite a palavra-chave: ").strip()
        if palavraChave.isalpha():
            break
        else:
            print("Você deve digitar uma palavra")
        
    asterisco = convertAst(palavraChave)

    dadosDicas = []
    dicas =["Desafiante digite a primeira dica: ","Desafiante digite a segunda dica: ","Desafiante digite a terceira dica: "]
    
    for dica in dicas:
        while True:   
            dica = input(dica) 
            if dica.isalpha():
                dadosDicas.append(dica)
                break
            else:
                dica = ''
                print("Valor invalido digite a dica novamente: ")
                
    limpaTela()
    jogoForca()


    print("Este é o tamanho da palavra-chave:\n\n"  + asterisco)


    input("Digite enter para iniciar")


    erros = 0
    chances = 5
    dicas = len(dicas)
    dados = 0
    letrasAcertadas = ["*" for i in range(len(palavraChave))]
        

    while True:
            if '*' not in letrasAcertadas:
                print("Parabéns o vencedor é: " + competidor)
                break
            elif chances == 0:
                print("Suas chances acabaram o vencedor é: " + desafiante)
                break
            
            letra = input("Digite uma letra ou (2) para uma dica: ")
            if letra == '2' and dicas != 0:
                print("A dica é: " + dadosDicas[dados]) 
                dados += 1
                dicas -= 1
                print("Dicas restantes: " + str(dicas))
            elif letra == '2'and dicas == 0:
                print("Você não tem mais dicas")
            elif letra in palavraChave:
                for i in range(len(palavraChave)):
                    if palavraChave[i] == letra:
                        letrasAcertadas[i] = letra
                        
                print("".join(letrasAcertadas))   
            else:
                erros += 1
                chances -=1
                print("Essa palavra não tem essa letra")
                print("Erros: "+ str(erros))
                print("Tentativas restantes: "+ str(chances))

    print("O jogo acabou")
    
    while True:
        try:
            continuar = int(input("Você deseja recomeçar o jogo? (1)Sim (0)Não"))
        
            if continuar == 0 or continuar == 1:
                break
            else:
                print("Numero incorreto, digite (1) para continuar ou (0) para terminar o jogo")

        except:
            print("O valor digitado é inválido, digite (1) para continuar ou (0) para terminar o jogo")

    if continuar == 0:
        break




