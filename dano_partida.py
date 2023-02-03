from random import randint
from math import floor

dado = int(input('Qual o tipo de dado? '))
quantidaded = int(input('Quantos dados são? '))
moda = int(input('Qual o seu modificador de ataque? '))
vantagem = int(input('Qual o seu bonus de dano? '))
margem = int(input('Qual sua margem para crítico? '))
multiplicador = int(input('Qual o seu multiplicador de crítico? '))
totald = 0
while True:
    rol = randint(1,20)
    if rol >= margem:
        for d in range(1,(quantidaded*multiplicador)+1):
            dano = randint(1, dado)
            totald += dano
    else:
        for d in range(1, quantidaded+1):
            dano = randint(1, dado)
            totald += dano
    resposta = input(f'''===========================
Ataque: {floor((rol)+moda)}
Dano: {floor((totald)+vantagem)}
===========================
Atacar? [s/n] ''').upper().strip()[0]
    print('===========================')
    if resposta in 'Nn':
        break
print('Obrigado, até mais!')
