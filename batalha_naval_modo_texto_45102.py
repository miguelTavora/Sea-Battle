
from random import choice

from batalha_naval_motor_45102 import novo_jogo
from batalha_naval_motor_45102 import barcos_prontos
from batalha_naval_motor_45102 import tiro
from batalha_naval_motor_45102 import terminou

# esta função poderia estar aqui neste ficheiro. só está num ficheiro
# à parte porque foi usada noutros contextos, nomeadamente, para fazer
# testes ao agente.
from batalha_naval_util_45102 import get_jogo_string

from batalha_naval_agente_45102 import coloca_barcos_aleatoriamente
from batalha_naval_agente_45102 import agente_joga





mensagem_inicial = '''
Batalha Naval - com o computador

Os barcos dos dois jogadores são colocados aleatoriamente.

O primeiro jogador a jogar é sorteado aleatoriamente.

Boa sorte!
'''

# Para disparar, escreve as coordenadas linha e coluna, separadas por uma
# vírgula, (por exemplo: c,8) seguidas de return. Ou só return para
# jogar aleatorimente.





# variáveis globais
jogador_humano     = 1
jogador_computador = 2
jogador            = None # representa o próximo jogador a jogar





def sortear_ordem():

    global jogador_humano
    global jogador_computador
    global jogador

    primeiro = choice([1, 2])
    if primeiro == 1:
        # próximo jogador a jogar
        jogador = jogador_humano
        palavra = 'primeiro'
    else:
        # próximo jogador a jogar
        jogador = jogador_computador
        palavra = 'segundo'

    print('''
Foi sorteado quem joga primeiro.

Tu és o ''' + palavra + ''' a jogar.
''')






def humano_coloca_barcos(jogo, jogador):

    
    repetir = True

    while repetir == True:

        coloca_barcos_aleatoriamente(jogo, jogador)
        print(get_jogo_string(jogo, jogador_humano))
        tecla = input('''
Os teus barcos foram colocados aleatoriemnte.

Queres repetir a colocação aleatória dos teus barcos?

Escreve r seguido de return para repetir e só return para continuar: ''')
    
        if tecla != 'r':
            repetir = False





def computador_coloca_barcos(jogo, jogador):

    coloca_barcos_aleatoriamente(jogo, jogador)





def converte_coordenadas(coordenadas):

    # índice da vírgula
    ivirgula = None
    for n in range(len(coordenadas)):
        if coordenadas[n] == ',':
            ivirgula = n

    linha_string  = coordenadas[0:ivirgula]
    coluna_string = coordenadas[ivirgula + 1:]

    print('"' + coluna_string + '"')

    linha  = int(linha_string)
    coluna = ord(coluna_string) - ord('A') + 1

    print(linha,coluna)

    return (linha, coluna)





def humano_joga(jogo):

    coordenadas = input(
        '''Introduz as coordenadas do tiro na forma letra e número
separados por vírgula e seguidos de return.
Ou carrega só em return para jogar aleatriamente.
Tiro: ''' )

    if coordenadas == '':

        agente_joga(jogo, jogador_humano)

    else:

        (linha, coluna) = converte_coordenadas(coordenadas)

        tiro(jogo, jogador_humano, linha, coluna)





def computador_joga(jogo):

    agente_joga(jogo, jogador_computador)
    print('O computador já jogou!')





def jogador_joga(jogo, jogador):

    if jogador == 1:
        humano_joga(jogo)
    else:
        computador_joga(jogo)





def proximo_jogador(jogador):
    
    if jogador == 1:
        return 2
    else:
        return 1





# jogo

print(mensagem_inicial)

input('Carrega em return para continuar...')

sortear_ordem()

input('Carrega em return para continuar...')

jogo = novo_jogo()

# nesta versão, com colocação aleatória dos barcos, a verificação de
# barcos prontos é desnecessária porque os barcos são todos
# colocados. Mas numa versão de colocação manual e individual dos
# barcos, esta verificação é importante porque o jogo não pode começar
# enquanto os barcos não estiverem prontos.
while not barcos_prontos(jogo, jogador_humano):
    humano_coloca_barcos(jogo, jogador_humano)

while not barcos_prontos(jogo, jogador_computador):
    computador_coloca_barcos(jogo, jogador_computador)

fim      = False
vencedor = None
while not fim:

    print(get_jogo_string(jogo, jogador_humano))

    jogador_joga(jogo, jogador)

    (fim, vencedor) = terminou(jogo)

    jogador = proximo_jogador(jogador)


# mostrar a última jogada
print(get_jogo_string(jogo, jogador_humano))

# fim do jogo
if vencedor == jogador_humano:

    print('''

FROTA AO FUNDO!!!

PARABÉNS!!! GANHASTE!!! :-)

''')

else:

    print('''

FROTA AO FUNDO!!!

PERDESTE!!! :-( Tenta outra vez...

''')
