
from batalha_naval_motor_45102 import valor_defesa
from batalha_naval_motor_45102 import valor_ataque





def string_dois_carateres(uma_string):
    
    while len(uma_string) < 2:
        uma_string = uma_string + ' '
    return uma_string






def get_grelha_string(jogo, numero_grelha, valor):

    separador  = '---|---|---|---|---|---|---|---|---|---|---|\n'
    uma_string = '   | A | B | C | D | E | F | G | H | I | J |\n' \
                 + separador
    aux  = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10']

    for n in range(10):
        uma_string = uma_string + aux[n] + ' |'

        for m in range(10):

            valor_grelha = valor(jogo, numero_grelha, n+1, m+1)
            if valor_grelha == None:
                valor_grelha = ' '
            uma_string = uma_string + ' ' \
                         + string_dois_carateres(str(valor_grelha)) + '|' 

        uma_string = uma_string + '\n'
        uma_string = uma_string + separador

    return uma_string





def get_jogo_string(jogo, numero_jogador):

    separador = '     '
    grelha_propria    = get_grelha_string(jogo, numero_jogador, valor_defesa)
    grelha_adversario = get_grelha_string(jogo, numero_jogador, valor_ataque)

    linhas1 = grelha_propria.split('\n')
    linhas2 = grelha_adversario.split('\n')

    resultado = ''
    for n in range(len(linhas1)):
        resultado = resultado + separador.join([linhas1[n], linhas2[n], '\n'])

    return resultado

