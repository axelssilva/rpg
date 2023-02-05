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
def parâmetros():
    global dado, quantidaded, moda, vantagem, margem, multiplicador
    dado = int(input('Qual o tipo de dado? '))
    quantidaded = int(input('Quantos dados são? '))
    moda = int(input('Qual o seu modificador de ataque? '))
    vantagem = int(input('Qual o seu bonus de dano? '))
    margem = int(input('Qual sua margem para crítico? '))
    multiplicador = int(input('Qual o seu multiplicador de crítico? '))


def roll():
    global totald, rol
    totald = 0
    rol = randint(1, 20)
    if rol >= margem:
        for d in range(1, (quantidaded * multiplicador) + 1):
            dano = randint(1, dado)
            totald += dano
    else:
        for d in range(1, quantidaded + 1):
            dano = randint(1, dado)
            totald += dano

#script principal:
dado = quantidaded = moda = vantagem = margem = multiplicador = resp = totald = 0
parâmetros()
while True:
    print('=-=' * 30)
    resp = int(input('''Selecione uma opção:
        [1] Rolar ataque
        [2] Redefinir valores
        [0] Sair do programa
        Sua decisão: '''))
    print('=-='*30)
    if resp == 1:
        roll()
        print(f'Seu roll puro foi {rol}\nSeu ataque foi {rol+moda}\nSeu dano puro foi {totald}\nSeu dano foi {totald+vantagem}')
    elif resp == 2:
        parâmetros()
    elif resp == 0:
        print('Até mais!')
        break
    else:
        print('comando incorreto, tente novamente!')

#sacript funcional utilizandos defs 05/02/2023