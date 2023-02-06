#  da mesma forma que antes vamos utilizar variaveis para definir valores, sendo elas as variaveis:
#  dado - a quantidade de faces que o dado de dano possúi
#  quantidaded - representa quantos dados devem ser rolados para o seu dano
#  moda - é o modificador usado no ataque
#  vantagem - é o modificador utilizado quando for rolar o dano
#  margem - o menor valor necessário para que seja dado um ataque critico
#  multiplicador - por quantas vezes o tipo de dado sera multiplicado no caso de um critico

#  módulos utilizados:
from random import randint

# defs utilizadas:


def parametros():
    global dado, quantidaded, moda, vantagem, margem, multiplicador
    dado = int(input('Qual o tipo de dado? '))
    quantidaded = int(input('Quantos dados são? '))
    moda = int(input('Qual o seu modificador de ataque? '))
    vantagem = int(input('Qual o seu bonus de dano? '))
    margem = int(input('Qual sua margem para crítico? '))
    multiplicador = int(input('Qual o seu multiplicador de crítico? '))


def roll():
    global totald, ro
    totald = 0
    ro = randint(1, 20)
    if ro < (ac + moda):
        print('Seu ataque não acertou!')
        linha()
    if ro >= margem:
        for d in range(1, (quantidaded * multiplicador) + 1):
            dano = randint(1, dado)
            totald += dano
    else:
        for d in range(1, quantidaded + 1):
            dano = randint(1, dado)
            totald += dano


def acerto():
    global ac
    ac = int(input('Qual a defesa do seu oponente? '))


def linha():
    print('=-=' * 15)

# script principal:


dado = quantidaded = moda = vantagem = margem = multiplicador = resp = totald = ac = ro = 0
parametros()
acerto()
while True:
    linha()
    resp = int(input('''Selecione uma opção:
        [1] Rolar ataque
        [2] Redefinir valores
        [3] Redefinir defesa
        [0] Sair do programa
        Sua decisão: '''))
    linha()
    if resp == 1:
        roll()
        print(f'''Seu roll puro foi {ro}
        Seu ataque foi {ro+moda}
        Seu dano puro foi {totald}Seu dano foi {totald+vantagem}''')
    elif resp == 2:
        parametros()
    elif resp == 3:
        acerto()
    elif resp == 0:
        print('Até mais!')
        break
    else:
        print('comando incorreto, tente novamente!')

# script funcional utilizandos defs 06/02/2023
