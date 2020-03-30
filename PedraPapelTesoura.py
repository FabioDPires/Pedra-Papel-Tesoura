import random

print(("#BEM VINDO AO JOGO PEDRA PAPEL TESOURA"))
#uNome=(input("Indique o seu ultimo nome"))
#print("0-Pedra")
nome=input("Indique o seu nome")
nomes=nome.split(" ")
pNome=nomes[0]
uNome=nomes[1]
print("0-Pedra")
print("1-Papel")
print("2-Tesoura")
novopNome=pNome.replace(pNome[0],pNome[0].upper())
novouNome=uNome.replace(uNome[0],uNome[0].upper())
escolha=input("Indique a sua escolha")
escolhaComputador=random.randrange(0,2,1)
print(("Escolha do Computador",escolhaComputador))
if(int(escolha)==escolhaComputador):
    print("EMPATE!")
else:

    if(int(escolha)==0):
        if(escolhaComputador==1):
            print("O computador ganhou")
        if(escolhaComputador==2):
            print(("O utilizador ganhou"))
            print("SR ",novouNome," ",novopNome)

    if(int(escolha)==1):
        if(escolhaComputador==2):
            print("O computador ganhou")
        if(escolhaComputador==0):
            print(("O utilizador ganhou"))
            print("SR ", novouNome," ", novopNome)

    if(int(escolha)==2):
        if(escolhaComputador==0):
            print("O computador ganhou")
        if(escolhaComputador==1):
            print(("O utilizador ganhou"))
            print("SR ", novouNome," ", novopNome)