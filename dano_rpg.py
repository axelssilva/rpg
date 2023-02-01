from random import randint

#dados representa qual o formato de dado utilizado (d4, d6, d8,..),
#qtd representa a quantidade de dados utilizada na rolagem de dano,
#modificador representa a modificação de dano de acordo com o atributo utilizado para ataque (força, destreaza,...),
#teste é o modificador de teste utilizado no dano, por exemplo, luta, pontaria, etc
#margem é a margem de critico
#multiplicador é a quantidade de vezes em que é multiplicado o dano de acordo com o critico
#por fim, n é a quantidade de vezes que o dano será testado

dados = int(input(f'Qual o dado do seu dano? d '))
quantidade = int(input('Quantos dados de dano tem o seu ataque? '))
modificador = int(input('Qual o modificador de dano? '))
bonus = int(input('Bonus do teste de ataque: '))
margem = int(input('Qual o menor valor para crítico? '))
multiplicador = int(input('Qual o seu múltiplicador de crítico? '))
n = int(input('Quantos testes quer fazer? '))

#teste de ataque
for a in range(1,n+1):
    ataque = randint(1,21)
#dano
    if ataque >= margem:
        for b in range(1, quantidade + multiplicador + 1):
            danoc = randint(1,dados+1)+modificador
            danoc += danoc
    else:
        for b in range(1, quantidade+1):
            dano = randint(1, dados+1)+modificador
            dano  += dano
print(f'Sua média de dano é {dano+danoc}\nE sua média de ataque é {(ataque)+bonus}')
#não lembro se ao colocar ao fazer uma variável receber um laço o valor mostrado é a média ou o íltimo valor que a variável recebeu,
#logo é provavel que esteja incorreto
