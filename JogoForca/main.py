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
                vencedor = competidor
                perdedor = desafiante
                break
            elif chances == 0:
                print("\nSuas chances acabaram o vencedor é: " + desafiante)
                vencedor = desafiante
                perdedor = competidor
                break
            
            letra = input("\nDigite uma letra ou (2) para uma dica: ")
            while len(letra) != 1:
                print(("\nCampos vazios ou mais de uma letra não são permitidos: "))
                letra = input("\nDigite apenas uma letra: ")
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
                print("\nEssa palavra não tem essa letra")
                print("Erros: "+ str(erros))
                print("Tentativas restantes: "+ str(chances))


    try:
        arquivo = open("historico_partidas.txt","a")
        arquivo.write("\nPalavra: "+ palavraChave + "   Vencedor: " + vencedor +"   Perdedor: " + perdedor)
        arquivo.close()
        
    except:
        print("Arquivo não encontrado")

    print("\nO jogo acabou\n")


    try:
        arquivo = open("historico_partidas.txt", encoding="utf-8")
        historico = arquivo.read()
        print(historico)
    except:
        print("Arquivo não encontrado")


    while True:
        try:
            continuar = int(input("\nVocê deseja recomeçar o jogo? (1)Sim (0)Não"))
        
            if continuar == 0 or continuar == 1:
                break
            else:
                print("\nNúmero incorreto, digite (1) para continuar ou (0) para terminar o jogo")

        except:
            print("\nO valor digitado é inválido, digite (1) para continuar ou (0) para terminar o jogo")

    if continuar == 0:
        print("\nObrigado por jogar!!!")
        break




