#  da mesma forma que antes vamos utilizar variaveis para definir valores, sendo elas as variaveis:
#  dado - a quantidade de faces que o dado de dano possúi
#  quantidaded - representa quantos dados devem ser rolados para o seu dano
#  moda - é o modificador usado no ataque
#  vantagem - é o modificador utilizado quando for rolar o dano
#  margem - o menor valor necessário para que seja dado um ataque critico
#  multiplicador - por quantas vezes o tipo de dado sera multiplicado no caso de um critico
#  n - a quantidade de vezes em que sera testado

#  módulos utilizados:
from random import randint
from math import floor

#  variáveis:
dado = int(input('Qual o tipo de dado? '))
quantidaded = int(input('Quantos dados são? '))
moda = int(input('Qual o seu modificador de ataque? '))
vantagem = int(input('Qual o seu bonus de dano? '))
margem = int(input('Qual sua margem para crítico? '))
multiplicador = int(input('Qual o seu multiplicador de crítico? '))
n = int(input('Quantas vezes quer testar? '))
rold = randint(1, dado)

#  contadores:
totald = 0
ataque = 0

#  script:
for t in range(1, n+1):
    rol = randint(1,20)
    if rol >= margem:
        for d in range(1,(quantidaded*multiplicador)+1):
            dano = randint(1, dado)
            totald += dano
    else:
        for d in range(1, quantidaded):
            dano = randint(1, dado)
            totald += dano
    ataque += rol

#  saidas:
print(f'''===========================
A sua média de ataque é {floor((ataque/n)+moda)}
A sua média de dano é {floor((totald/n)+vantagem)}
===========================''')

#  o script está funcional usando laço for, o próximo passo é atualizar o mesmo para o fromato while,
#  a ideia é poder repetir o script quantas vezes desejar 
#  02/02/2023
