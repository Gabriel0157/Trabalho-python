import random

ptsJogador = 0
print("Olá, Qual é o seu nome? ", end="")
nome = input()
print("Seja bem vindo", nome)
print("Escolha um nível de dificuldade: ", end="")
print("\nMENU")
print("1-Fácil (4 tentativas)")
print("2-Médio (6 tentativas)")
print("3-Difícil (7 tentativas)")
print("0-Sair")
dificuldade = int(input())

vInicial = 1
vFinalFacil = 10
vFinalMedio = 50
vFinalDificil = 100


if dificuldade == 1:
    tentativas=4
    contador=0
    print("Ok, vou escolher um número entre", vInicial, "e", vFinalFacil)
    numeroEscolhido = random.randint(vInicial, vFinalFacil)
    print("...")
    print("Pronto! Já escolhi!")
    print("Adivinhe o número: ", end="")
    print( )
    chute = int(input())
    while chute!=numeroEscolhido:
        contador=contador+1
        while contador!=tentativas:
            print("Errou!!!")
            if numeroEscolhido > chute:
                print("Dica: o número é maior!")
            elif numeroEscolhido<chute:
                print("Dica: o número é menor!")
            print("Digite novamente: ", end="")
            chute=int(input())
            print( )
        if contador==tentativas: 
            print("Você não tem mais tentativas!")
    if chute==numeroEscolhido:
        print("Parabéns! Eu realmente escolhi o número", numeroEscolhido)
        ptsJogador= ptsJogador+10
        print("Você ganhou", ptsJogador, "pontos!")

if dificuldade == 2:
    tentativas=6
    contador=0
    print("Ok, vou escolher um número entre", vInicial, "e", vFinalMedio)
    numeroEscolhido = random.randint(vInicial, vFinalMedio)
    print("...")
    print("Pronto! Já escolhi!")
    print("Adivinhe o número: ", end="")
    print( )
    chute = int(input())
    while chute!=numeroEscolhido:
        contador=contador+1
        while contador!=tentativas:
            print("Errou!!!")
            if numeroEscolhido > chute:
                print("Dica: o número é maior!")
            elif numeroEscolhido<chute:
                print("Dica: o número é menor!")
            print("Digite novamente: ", end="")
            chute=int(input())
            print( )
        if contador==tentativas: 
            print("Você não tem mais tentativas!")
    if chute==numeroEscolhido:
        print("Parabéns! Eu realmente escolhi o número", numeroEscolhido)
        ptsJogador= ptsJogador+25
        print("Você ganhou", ptsJogador, "pontos!")
        
if dificuldade == 3:
    tentativas=7
    contador=0
    print("Ok, vou escolher um número entre", vInicial, "e", vFinalDificil)
    numeroEscolhido = random.randint(vInicial, vFinalDificil)
    print("...")
    print("Pronto! Já escolhi!")
    print("Adivinhe o número: ", end="")
    print( )
    chute = int(input())
    while chute!=numeroEscolhido:
        contador=contador+1
        while contador!=tentativas:
            print("Errou!!!")
            if numeroEscolhido > chute:
                print("Dica: o número é maior!")
            elif numeroEscolhido<chute:
                print("Dica: o número é menor!")
            print("Digite novamente: ", end="")
            chute=int(input())
            print( )
        if contador==tentativas: 
            print("Você não tem mais tentativas!")
    if chute==numeroEscolhido:
        print("Parabéns! Eu realmente escolhi o número", numeroEscolhido)
        ptsJogador= ptsJogador+50
        print("Você ganhou", ptsJogador, "pontos!")
        
if dificuldade == 0:
    print("Jogo Finalizado!")
