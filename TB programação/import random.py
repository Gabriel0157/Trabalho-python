import random

print("Olá, Qual é o seu nome?")
nome=input()
print("Seja Bem vindo", nome,"!")

print("Digite o valor inicial: ", end="")
vInicial=int(input())

print("Digite o valor final: ", end="")
vFinal=int(input())

print("Vou escolher um número entre", vInicial, "e", vFinal)
numeroEscolhido=random.randint(vInicial,vFinal)

print("Pronto! Já escolhi!")
print("Adivinhe o número: ", end="")
chute=int(input())

while chute!=numeroEscolhido:
    print("Errou!!!")
    if numeroEscolhido>chute:
        print("Dica: o número é maior!")
    else:
        print("Dica: o número é menor!")
        print("Digite novamente: ", end="")
        chute=int(input())
print("Parabéns! Eu realmente escolhi o número", numeroEscolhido)