from batalha_naval_motor_45102 import novo_jogo
from batalha_naval_motor_45102 import tiro

import random


#função para colocar os barcos do jogador e do pc na grelha aleatóriamente
def coloca_barcos_aleatoriamente(jogo,numero_jogador):

    if(numero_jogador == 1):
        rd_up = random.randint(0,7)
        rd_down = random.randint(0,7)

        jogo[0][rd_up][rd_down]   =     jogo[1][0][0][0]
        jogo[0][rd_up][rd_down+1] =     jogo[1][0][0][1]
        jogo[0][rd_up][rd_down+2] =     jogo[1][0][0][2]
        jogo[0][rd_up+1][rd_down] =     jogo[1][0][1][0]
        jogo[0][rd_up+1][rd_down+1]=    jogo[1][0][1][1]
        jogo[0][rd_up+1][rd_down+2]=    jogo[1][0][1][2]
        jogo[0][rd_up+2][rd_down]  =    jogo[1][0][2][0]
        jogo[0][rd_up+2][rd_down+1]=    jogo[1][0][2][1]
        jogo[0][rd_up+2][rd_down+2]=    jogo[1][0][2][2]

        if(jogo[1][1][0][0] == 6):
            rand = random.randint(0,9)
            rand_down = random.randint(0,6)
            if(jogo[0][rand][rand_down] != None or jogo[0][rand][rand_down+1] != None or jogo[0][rand][rand_down+2] != None or jogo[0][rand][rand_down+3] != None):
                found = False
                while not found:
                    new_rand = random.randint(0,9)
                    new_rand_2 = random.randint(0,6)
                    if(jogo[0][new_rand][new_rand_2] == None and jogo[0][new_rand][new_rand_2+1] == None and jogo[0][new_rand][new_rand_2+2] == None and jogo[0][new_rand][new_rand_2+3] == None):
                        jogo[0][new_rand][new_rand_2] = jogo[1][1][0][0]
                        jogo[0][new_rand][new_rand_2+1] = jogo[1][1][0][1]
                        jogo[0][new_rand][new_rand_2+2] = jogo[1][1][0][2]
                        jogo[0][new_rand][new_rand_2+3] = jogo[1][1][0][3]
                        found = True
            else:
                jogo[0][rand][rand_down] = jogo[1][1][0][0]
                jogo[0][rand][rand_down+1] = jogo[1][1][0][1]
                jogo[0][rand][rand_down+2] = jogo[1][1][0][2]
                jogo[0][rand][rand_down+3] = jogo[1][1][0][3]


        elif(jogo[1][1][0][0] == 7):
            rand = random.randint(0,6)
            rand_down = random.randint(0,9)
            if(jogo[0][rand][rand_down] != None or jogo[0][rand+1][rand_down] != None or jogo[0][rand+2][rand_down] != None or jogo[0][rand+3][rand_down] != None):
                found = False
                while not found:
                    new_rand = random.randint(0,6)
                    new_rand_2 = random.randint(0,9)
                    if(jogo[0][new_rand][new_rand_2] == None and jogo[0][new_rand+1][new_rand_2] == None and jogo[0][new_rand+2][new_rand_2] == None and jogo[0][new_rand+3][new_rand_2] == None):
                        jogo[0][new_rand][new_rand_2] = jogo[1][1][0][0]
                        jogo[0][new_rand+1][new_rand_2] = jogo[1][1][1][0]
                        jogo[0][new_rand+2][new_rand_2] = jogo[1][1][2][0]
                        jogo[0][new_rand+3][new_rand_2] = jogo[1][1][3][0]
                        found = True
            else:
                jogo[0][rand][rand_down] =   jogo[1][1][0][0]
                jogo[0][rand+1][rand_down] = jogo[1][1][1][0]
                jogo[0][rand+2][rand_down] = jogo[1][1][2][0]
                jogo[0][rand+3][rand_down] = jogo[1][1][3][0]

        if(jogo[1][2][0][0] == 4):
            rand = random.randint(0,9)
            rand_down = random.randint(0,7)
            if(jogo[0][rand][rand_down] != None or jogo[0][rand][rand_down+1] != None or jogo[0][rand][rand_down+2] != None):
                found = False
                while not found:
                    new_rand = random.randint(0,9)
                    new_rand_2 = random.randint(0,7)
                    if(jogo[0][new_rand][new_rand_2] == None and jogo[0][new_rand][new_rand_2+1] == None and jogo[0][new_rand][new_rand_2+2] == None):
                        jogo[0][new_rand][new_rand_2] = jogo[1][2][0][0]
                        jogo[0][new_rand][new_rand_2+1] = jogo[1][2][0][1]
                        jogo[0][new_rand][new_rand_2+2] = jogo[1][2][0][2]
                        found = True
            else:
                jogo[0][rand][rand_down] = jogo[1][2][0][0]
                jogo[0][rand][rand_down+1] = jogo[1][2][0][1]
                jogo[0][rand][rand_down+2] = jogo[1][2][0][2]


        elif(jogo[1][2][0][0] == 5):
            rand = random.randint(0,7)
            rand_down = random.randint(0,9)
            if(jogo[0][rand][rand_down] != None or jogo[0][rand+1][rand_down] != None or jogo[0][rand+2][rand_down] != None):
                found = False
                while not found:
                    new_rand = random.randint(0,7)
                    new_rand_2 = random.randint(0,9)
                    if(jogo[0][new_rand][new_rand_2] == None and jogo[0][new_rand+1][new_rand_2] == None and jogo[0][new_rand+2][new_rand_2] == None):
                        jogo[0][new_rand][new_rand_2] = jogo[1][2][0][0]
                        jogo[0][new_rand+1][new_rand_2] = jogo[1][2][1][0]
                        jogo[0][new_rand+2][new_rand_2] = jogo[1][2][2][0]
                        found = True
            else:
                jogo[0][rand][rand_down] =   jogo[1][2][0][0]
                jogo[0][rand+1][rand_down] = jogo[1][2][1][0]
                jogo[0][rand+2][rand_down] = jogo[1][2][2][0]

        if(jogo[1][3][0][0] == 2):
            for a in range(2):
                rand = random.randint(0,9)
                rand_down = random.randint(0,8)
                if(jogo[0][rand][rand_down] != None or jogo[0][rand][rand_down+1] != None):
                    found = False
                    while not found:
                        new_rand = random.randint(0,9)
                        new_rand_2 = random.randint(0,8)
                        if(jogo[0][new_rand][new_rand_2] == None and jogo[0][new_rand][new_rand_2+1] == None):
                            jogo[0][new_rand][new_rand_2] = jogo[1][3][0][0]
                            jogo[0][new_rand][new_rand_2+1] = jogo[1][3][0][1]
                            found = True
                else:
                    jogo[0][rand][rand_down] = jogo[1][3][0][0]
                    jogo[0][rand][rand_down+1] = jogo[1][3][0][1]

        elif(jogo[1][3][0][0] == 3):
            for a in range(2):
                rand = random.randint(0,8)
                rand_down = random.randint(0,9)
                if(jogo[0][rand][rand_down] != None or jogo[0][rand+1][rand_down] != None):
                    found = False
                    while not found:
                        new_rand = random.randint(0,8)
                        new_rand_2 = random.randint(0,9)
                        if(jogo[0][new_rand][new_rand_2] == None and jogo[0][new_rand+1][new_rand_2] == None):
                            jogo[0][new_rand][new_rand_2] = jogo[1][3][0][0]
                            jogo[0][new_rand+1][new_rand_2] = jogo[1][3][1][0]
                            found = True
                else:
                    jogo[0][rand][rand_down] =   jogo[1][3][0][0]
                    jogo[0][rand+1][rand_down] = jogo[1][3][1][0]


        if(jogo[1][5][0][0] == 1):
            for a in range(3):
                rand = random.randint(0,9)
                rand_down = random.randint(0,9)
                if(jogo[0][rand][rand_down] != None):
                    found = False
                    while not found:
                        new_rand = random.randint(0,9)
                        new_rand_2 = random.randint(0,9)
                        if(jogo[0][new_rand][new_rand_2] == None):
                            jogo[0][new_rand][new_rand_2] = 1
                            found = True
                else:
                    jogo[0][rand][rand_down] =   1

    elif(numero_jogador == 2):
        rd_up = random.randint(0,7)
        rd_down = random.randint(0,7)

        jogo[2][rd_up][rd_down]   =     jogo[3][0][0][0]
        jogo[2][rd_up][rd_down+1] =     jogo[3][0][0][1]
        jogo[2][rd_up][rd_down+2] =     jogo[3][0][0][2]
        jogo[2][rd_up+1][rd_down] =     jogo[3][0][1][0]
        jogo[2][rd_up+1][rd_down+1]=    jogo[3][0][1][1]
        jogo[2][rd_up+1][rd_down+2]=    jogo[3][0][1][2]
        jogo[2][rd_up+2][rd_down]  =    jogo[3][0][2][0]
        jogo[2][rd_up+2][rd_down+1]=    jogo[3][0][2][1]
        jogo[2][rd_up+2][rd_down+2]=    jogo[3][0][2][2]

        if(jogo[3][1][0][0] == 6):
            rand = random.randint(0,9)
            rand_down = random.randint(0,6)
            if(jogo[2][rand][rand_down] != None or jogo[2][rand][rand_down+1] != None or jogo[2][rand][rand_down+2] != None or jogo[2][rand][rand_down+3] != None):
                found = False
                while not found:
                    new_rand = random.randint(0,9)
                    new_rand_2 = random.randint(0,6)
                    if(jogo[2][new_rand][new_rand_2] == None and jogo[2][new_rand][new_rand_2+1] == None and jogo[2][new_rand][new_rand_2+2] == None and jogo[2][new_rand][new_rand_2+3] == None):
                        jogo[2][new_rand][new_rand_2] = jogo[3][1][0][0]
                        jogo[2][new_rand][new_rand_2+1] = jogo[3][1][0][1]
                        jogo[2][new_rand][new_rand_2+2] = jogo[3][1][0][2]
                        jogo[2][new_rand][new_rand_2+3] = jogo[3][1][0][3]
                        found = True
            else:
                jogo[2][rand][rand_down] = jogo[3][1][0][0]
                jogo[2][rand][rand_down+1] = jogo[3][1][0][1]
                jogo[2][rand][rand_down+2] = jogo[3][1][0][2]
                jogo[2][rand][rand_down+3] = jogo[3][1][0][3]


        elif(jogo[3][1][0][0] == 7):
            rand = random.randint(0,6)
            rand_down = random.randint(0,9)
            if(jogo[2][rand][rand_down] != None or jogo[2][rand+1][rand_down] != None or jogo[2][rand+2][rand_down] != None or jogo[2][rand+3][rand_down] != None):
                found = False
                while not found:
                    new_rand = random.randint(0,6)
                    new_rand_2 = random.randint(0,9)
                    if(jogo[2][new_rand][new_rand_2] == None and jogo[2][new_rand+1][new_rand_2] == None and jogo[2][new_rand+2][new_rand_2] == None and jogo[2][new_rand+3][new_rand_2] == None):
                        jogo[2][new_rand][new_rand_2] = jogo[3][1][0][0]
                        jogo[2][new_rand+1][new_rand_2] = jogo[3][1][1][0]
                        jogo[2][new_rand+2][new_rand_2] = jogo[3][1][2][0]
                        jogo[2][new_rand+3][new_rand_2] = jogo[3][1][3][0]
                        found = True
            else:
                jogo[2][rand][rand_down] =   jogo[3][1][0][0]
                jogo[2][rand+1][rand_down] = jogo[3][1][1][0]
                jogo[2][rand+2][rand_down] = jogo[3][1][2][0]
                jogo[2][rand+3][rand_down] = jogo[3][1][3][0]

        if(jogo[3][2][0][0] == 4):
            rand = random.randint(0,9)
            rand_down = random.randint(0,7)
            if(jogo[2][rand][rand_down] != None or jogo[2][rand][rand_down+1] != None or jogo[2][rand][rand_down+2] != None):
                found = False
                while not found:
                    new_rand = random.randint(0,9)
                    new_rand_2 = random.randint(0,7)
                    if(jogo[2][new_rand][new_rand_2] == None and jogo[2][new_rand][new_rand_2+1] == None and jogo[2][new_rand][new_rand_2+2] == None):
                        jogo[2][new_rand][new_rand_2] = jogo[3][2][0][0]
                        jogo[2][new_rand][new_rand_2+1] = jogo[3][2][0][1]
                        jogo[2][new_rand][new_rand_2+2] = jogo[3][2][0][2]
                        found = True
            else:
                jogo[2][rand][rand_down] = jogo[3][2][0][0]
                jogo[2][rand][rand_down+1] = jogo[3][2][0][1]
                jogo[2][rand][rand_down+2] = jogo[3][2][0][2]


        elif(jogo[3][2][0][0] == 5):
            rand = random.randint(0,7)
            rand_down = random.randint(0,9)
            if(jogo[2][rand][rand_down] != None or jogo[2][rand+1][rand_down] != None or jogo[2][rand+2][rand_down] != None):
                found = False
                while not found:
                    new_rand = random.randint(0,7)
                    new_rand_2 = random.randint(0,9)
                    if(jogo[2][new_rand][new_rand_2] == None and jogo[2][new_rand+1][new_rand_2] == None and jogo[2][new_rand+2][new_rand_2] == None):
                        jogo[2][new_rand][new_rand_2] = jogo[3][2][0][0]
                        jogo[2][new_rand+1][new_rand_2] = jogo[3][2][1][0]
                        jogo[2][new_rand+2][new_rand_2] = jogo[3][2][2][0]
                        found = True
            else:
                jogo[2][rand][rand_down] =   jogo[3][2][0][0]
                jogo[2][rand+1][rand_down] = jogo[3][2][1][0]
                jogo[2][rand+2][rand_down] = jogo[3][2][2][0]

        if(jogo[3][3][0][0] == 2):
            for a in range(2):
                rand = random.randint(0,9)
                rand_down = random.randint(0,8)
                if(jogo[2][rand][rand_down] != None or jogo[2][rand][rand_down+1] != None):
                    found = False
                    while not found:
                        new_rand = random.randint(0,9)
                        new_rand_2 = random.randint(0,8)
                        if(jogo[2][new_rand][new_rand_2] == None and jogo[2][new_rand][new_rand_2+1] == None):
                            jogo[2][new_rand][new_rand_2] = jogo[3][3][0][0]
                            jogo[2][new_rand][new_rand_2+1] = jogo[3][3][0][1]
                            found = True
                else:
                    jogo[2][rand][rand_down] = jogo[3][3][0][0]
                    jogo[2][rand][rand_down+1] = jogo[3][3][0][1]

        elif(jogo[3][3][0][0] == 3):
            for a in range(2):
                rand = random.randint(0,8)
                rand_down = random.randint(0,9)
                if(jogo[2][rand][rand_down] != None or jogo[2][rand+1][rand_down] != None):
                    found = False
                    while not found:
                        new_rand = random.randint(0,8)
                        new_rand_2 = random.randint(0,9)
                        if(jogo[2][new_rand][new_rand_2] == None and jogo[2][new_rand+1][new_rand_2] == None):
                            jogo[2][new_rand][new_rand_2] = jogo[3][3][0][0]
                            jogo[2][new_rand+1][new_rand_2] = jogo[3][3][1][0]
                            found = True
                else:
                    jogo[2][rand][rand_down] =   jogo[3][3][0][0]
                    jogo[2][rand+1][rand_down] = jogo[3][3][1][0]


        if(jogo[3][5][0][0] == 1):
            for a in range(3):
                rand = random.randint(0,9)
                rand_down = random.randint(0,9)
                if(jogo[2][rand][rand_down] != None):
                    found = False
                    while not found:
                        new_rand = random.randint(0,9)
                        new_rand_2 = random.randint(0,9)
                        if(jogo[2][new_rand][new_rand_2] == None):
                            jogo[2][new_rand][new_rand_2] = 1
                            found = True
                else:
                    jogo[2][rand][rand_down] =   1

#função para jogar automaticamente
def agente_joga(jogo,numero_jogador):

    linha = random.randint(0,9)
    coluna = random.randint(0,9)

    tiro(jogo,numero_jogador,linha+1,coluna+1)

    return(linha,coluna)


    










