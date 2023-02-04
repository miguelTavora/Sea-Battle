from batalha_naval_motor_45102 import novo_jogo
from batalha_naval_motor_45102 import get_dimensao_grelha
from batalha_naval_motor_45102 import get_numero_barcos
from batalha_naval_motor_45102 import get_barco
from batalha_naval_motor_45102 import roda_barco
from batalha_naval_motor_45102 import coloca_barco
from batalha_naval_motor_45102 import barcos_prontos
from batalha_naval_motor_45102 import valor_defesa
from batalha_naval_motor_45102 import valor_ataque
from batalha_naval_motor_45102 import tiro
from batalha_naval_motor_45102 import terminou
from batalha_naval_agente_45102 import coloca_barcos_aleatoriamente
from batalha_naval_agente_45102 import agente_joga


import pygame
import random
import time
import threading

#iniciar a biblioteca
pygame.init()

#definir o tamanho da janela para a seleção dos barcos
width = 700
height = 500

#clicar do rato
mouse_click = False

#posição do rato
position_mouse_x = None
position_mouse_y = None

#variavel que termina o jogo quando clica no x ou num botão específico para fechar
end = False

#lista que guarda cada valor da divisória dos pixeis em x
pixel_position_x = []#board game principal

#lista que guarda cada valor da divisória dos pixeis em y
pixel_position_y = []

#lista que guarda cada valor da divisória dos pixeis em x
pixel_division_x = []#para dar input dos barcos

#lista que guarda cada valor da divisória dos pixeis em y
pixel_division_y = []

#lista que guarda as divisorias do jogo para o agente em x
pixel_position_x_agent = []

#variável que guarda tudo do jogo
game = []


#lista que guarda o tipo de barco metido na grelha para não haver sobreposição de barcos
boats_placed = []


#variável que faz as transição entre janelas conforme a variação do seu valor
state = 4

#variável que diz que o jogador é o primeiro ou segundo a jogar
player = 0

#variável que diz que o jogador é o pc a jogar
player2 = 0

#variavel para gerar novas posições para os barcos
generator = True

#variavel para meter o agente sempre a jogar
enter = False

#variavel que muda apos o agente ter jogado 
played = False

#variavel que diz se pode ou não tocar musica
music = 0

#imagens usadas durante o jogo
back_menu = pygame.image.load('images/menu.png')
button_play = pygame.image.load('images/bt1.png')
button_settings = pygame.image.load('images/bt2.png')
button_credits = pygame.image.load('images/bt3.png')
button_quit = pygame.image.load('images/bt4.png')
settings = pygame.image.load('images/background_settings.png')
no_music = pygame.image.load('images/settings_no_music.png')
yes_music = pygame.image.load('images/settings_yes_music.png')
credits = pygame.image.load('images/credits.png')
back_credits = pygame.image.load('images/back_credits.png')


back_boats = pygame.image.load('images/barcos2a.png')
back_boats2 = pygame.image.load('images/barcos22.png')
back_boats3 = pygame.image.load('images/barcos23.png')
boat = pygame.image.load('images/icon6.png')
boat2 = pygame.image.load('images/icon4.png')
boat3 = pygame.image.load('images/icon3.png')
boat4 = pygame.image.load('images/icon2.png')
boat5 = pygame.image.load('images/icon.png')

back_game = pygame.image.load('images/back_game.jpg')
explusion = pygame.image.load('images/explusao.png')
ball = pygame.image.load('images/ball.png')
winner1 = pygame.image.load('images/win1.png')
winner2 = pygame.image.load('images/win2.png')

#player da música
music_1 = pygame.mixer.Sound('music/music_1.mp3')


#clock que conta o tempo para fazer as fps(frame per second, imagens por segundo)
clock = pygame.time.Clock()

#vaziavel que mostra tudo o que lhe é adicionado na janela
display = pygame.display.set_mode((400,600))


#função inicia a variavel jogo escolhe o jogador a jogar e roda os barcos
def start_variables():
    global game
    game = novo_jogo()
    build_window(back_boats,0,0)
    choose_player()
    rotate_boats()
    


#função para representar imagens a janela da imagem do jogo
def build_window(image,x,y):
    
    display.blit(image,(x,y))


#função que gera os eventos
def pygame_events():

    global end
    global position_mouse_x
    global position_mouse_y
    global mouse_click
    global generator
    global enter

    for event in pygame.event.get():

        #clicar no X da janela
        if event.type == pygame.QUIT:   
            end = True

        #quando há click do rato
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True

        #clicar no espaço
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                generator = True
            if event.key == pygame.K_RETURN:
                enter = True

    #posição do rato    
    (position_mouse_x, position_mouse_y) = pygame.mouse.get_pos()
    #print("mouse x",position_mouse_x)
    #print("mouse y",position_mouse_y)


#função que inicializa as divisorias dos quadrados no jogo
def division_values():
    global pixel_position_x
    global pixel_position_y
    global pixel_division_x
    global pixel_division_y
    global drag_positions
    global pixel_position_x_agent
    global game
    global boats_placed

    for a in range(11):
        pixel_position_x.append(34+a*53)
        pixel_position_y.append(35+a*33)
        pixel_division_x.append(44+a*54)
        pixel_division_y.append(71+a*36)
        pixel_position_x_agent.append(608+a*53)

    for a in range(get_numero_barcos(game)):
        boats_placed.append(0)
        boats_placed.append(0)
        boats_placed.append(0)

#função para gerar o jogador a jogar
def choose_player():

    global player
    global player2

    if random.random() > 0.5:
        player = 1
        player2 = 2

    else:
        player = 2
        player2 = 1

#função para rodar os barcos dada uma probabilidade
def rotate_boats():
    global game
    global player

    boat8 = random.random()

    boat6 = random.random()

    boat4 = random.random()

    boat2 = random.random()


    if boat8 > 0.75:
        roda_barco(game,player,8)

    elif boat8 > 0.5:
        roda_barco(game,player,8)
        roda_barco(game,player,8)

    elif boat8 > 0.25:
        roda_barco(game,player,8)
        roda_barco(game,player,8)
        roda_barco(game,player,8)

    if boat6 > 0.5:
        roda_barco(game,player,6)

    if boat4 > 0.5:
        roda_barco(game,player,4)

    if boat2 > 0.5:
        roda_barco(game,player,2)

#rodar barcos do pc
def rotate_boats_2():
    global game
    global player2

    boat8 = random.random()

    boat6 = random.random()

    boat4 = random.random()

    boat2 = random.random()


    if boat8 > 0.75:
        roda_barco(game,player2,8)

    elif boat8 > 0.5:
        roda_barco(game,player2,8)
        roda_barco(game,player2,8)

    elif boat8 > 0.25:
        roda_barco(game,player2,8)
        roda_barco(game,player2,8)
        roda_barco(game,player2,8)

    if boat6 > 0.5:
        roda_barco(game,player2,6)

    if boat4 > 0.5:
        roda_barco(game,player2,4)

    if boat2 > 0.5:
        roda_barco(game,player2,2)


#função que gere o menu principal
def menu_context():

    global position_mouse_x
    global position_mouse_y
    global mouse_click
    global end
    global state

    build_window(back_menu,0,0)

    if 98 < position_mouse_x < 303 and 330 < position_mouse_y < 363:
        build_window(button_play,90,325)

    if 98 < position_mouse_x < 303 and 330 < position_mouse_y < 363 and mouse_click:
        mouse_click = False
        display = pygame.display.set_mode((width, height))
        build_window(back_boats,0,0)
        state = 0

    if 96 < position_mouse_x < 303 and 409 < position_mouse_y < 450:
        build_window(button_settings,88,405)

    if 96 < position_mouse_x < 303 and 409 < position_mouse_y < 450 and mouse_click:
        build_window(settings,0,0)
        state = 5

    if 98 < position_mouse_x < 301 and 471 < position_mouse_y < 502:
        build_window(button_credits,91,463)

    if 98 < position_mouse_x < 301 and 471 < position_mouse_y < 508 and mouse_click:
        state = 6
        mouse_click = False

    if 96 < position_mouse_x < 306 and 540 < position_mouse_y < 572:
        build_window(button_quit,85,531)

    if 96 < position_mouse_x < 306 and 540 < position_mouse_y < 572 and mouse_click:
        end = True
        
    if mouse_click == True:
        mouse_click = False

#função que gere os settings
def context_settings():

    global position_mouse_x
    global position_mouse_y
    global mouse_click
    global music
    global music_played
    global state

    
    if 360 < position_mouse_x < 372 and 250 < position_mouse_y < 264 and mouse_click:
        build_window(yes_music,0,233)
        mouse_click = False
        if music < 2:
            music = 1
        else:
            music = 4



    if 125 < position_mouse_x < 138 and 252 < position_mouse_y < 262 and mouse_click:
        mouse_click = False
        build_window(no_music,0,233)
        if music < 2:
            music = 0
        else:
            music = 3

    if 110 < position_mouse_x < 292 and 461 < position_mouse_y < 516 and mouse_click and music != 0:
        mouse_click = False
        if music == 1:
            threading.Thread(target=thread_music(),args= ()).start()
            music = 2

        elif music == 3:
            stop_mixer()

        elif music == 4:
            play_mixer()


    if 140 < position_mouse_x < 262 and 551 < position_mouse_y < 581 and mouse_click:
        state = 4

    if mouse_click:
        mouse_click = False

#funções para a musica
def thread_music():

    pygame.mixer.Sound.play(music_1)


def play_mixer():

    pygame.mixer.unpause()


def stop_mixer():

    pygame.mixer.pause()

#função que gere os creditos
def context_credits():

    global position_mouse_x
    global position_mouse_y
    global mouse_click
    global state

    build_window(credits,0,0)

    if 206 < position_mouse_x < 378 and 557 < position_mouse_y < 584:
        build_window(back_credits,0,538)

    if 206 < position_mouse_x < 378 and 557 < position_mouse_y < 584 and mouse_click:
        mouse_click = False
        state = 4

#função para quando se clica r ele gera novos barcos com outras posições
def regeneration():
    global game

    game = novo_jogo()
    rotate_boats()

    build_window(back_boats,0,0)



#função para representar graficamente os barcos na grelha para escolha de posições que é gerado aleatoriamente
def input_boats_on_grid():

    global game
    global player
    global boats_placed
    global pixel_division_x
    global pixel_division_y
    global generator

    coloca_barcos_aleatoriamente(game,player)

    count = 0
    placed = False
    size = get_dimensao_grelha(game)

    counter = 0

    if(player == 1):
        for a in range(size[0]):
            for b in range(size[1]):
                if( game[0][a][b] != None):
                    boats_placed[counter*3] = b
                    boats_placed[counter*3+1] = a
                    boats_placed[counter*3+2] = game[0][a][b]
                    counter += 1

    else:
        for a in range(size[0]):
            for b in range(size[1]):
                if( game[2][a][b] != None):
                    boats_placed[counter*3] = b
                    boats_placed[counter*3+1] = a
                    boats_placed[counter*3+2] = game[2][a][b]
                    counter += 1


  
    for a in range(get_numero_barcos(game)):

        if(boats_placed[a*3+2] > 7):
            build_window(boat,pixel_division_x[boats_placed[a*3]],pixel_division_y[boats_placed[a*3+1]])


        elif(boats_placed[a*3+2] > 5):
            build_window(boat2,pixel_division_x[boats_placed[a*3]],pixel_division_y[boats_placed[a*3+1]])


        elif(boats_placed[a*3+2] > 3):
            build_window(boat3,pixel_division_x[boats_placed[a*3]],pixel_division_y[boats_placed[a*3+1]])


        elif(boats_placed[a*3+2] > 1):
            build_window(boat4,pixel_division_x[boats_placed[a*3]],pixel_division_y[boats_placed[a*3+1]])


        else:
            build_window(boat5,pixel_division_x[boats_placed[a*3]],pixel_division_y[boats_placed[a*3+1]])

#função que exibe a interação quando se clica no botão de continuar ele muda de cor e também permite mudar a janela
def interaction_button():

    global position_mouse_x
    global position_mouse_y
    global mouse_click
    global state
    global game
    global player
    global player2


    if(525 < position_mouse_x < 692 and 461 < position_mouse_y < 486):
        build_window(back_boats2,0,438)
    else:
        build_window(back_boats3,0,438)

    if(525 < position_mouse_x < 692 and 461 < position_mouse_y < 486 and mouse_click):
        rotate_boats_2()
        coloca_barcos_aleatoriamente(game,player2)
        if(barcos_prontos(game,player) and barcos_prontos(game,player2)):
            display = pygame.display.set_mode((1161, 400))
            build_window(back_game,0,0)
            mouse_click = False
            state = 1

#função principal do jogo
def game_interaction():

    global pixel_position_x
    global pixel_position_y
    global pixel_position_x_agent
    global position_mouse_x
    global position_mouse_y
    global mouse_click
    global game
    global player
    global enter
    global state
    global played
    pixel_x = 0
    pixel_y = 0
    value_a_x = 0
    value_a_y = 0

    if(player == 1):
        if(mouse_click and 34 < position_mouse_x < 564 and 35< position_mouse_y < 365):
            mouse_click = False
            for a in range(11):
                if pixel_x != 0 and pixel_y != 0:
                    break

                if pixel_position_x[a] > position_mouse_x and pixel_x == 0:
                    pixel_x = pixel_position_x[a-1]+7
                    value_a_x = a

                if pixel_position_y[a] > position_mouse_y and pixel_y == 0:
                    pixel_y = pixel_position_y[a-1]+2
                    value_a_y = a
   

            if(valor_ataque(game,player,value_a_y,value_a_x) == None):
                build_window(ball,pixel_x,pixel_y)
                tiro(game,player,value_a_y,value_a_x)

            elif(valor_ataque(game,player,value_a_y,value_a_x) == 0):
                build_window(ball,pixel_x,pixel_y)
                tiro(game,player,value_a_y,value_a_x)

            elif(valor_ataque(game,player,value_a_y,value_a_x) > 0):
                build_window(explusion,pixel_x,pixel_y)
                tiro(game,player,value_a_y,value_a_x)

            elif(valor_ataque(game,player,value_a_y,value_a_x) < 0):
                build_window(explusion,pixel_x,pixel_y)
                tiro(game,player,value_a_y,value_a_x)

            (nlinhas,ncolunas) = agente_joga(game,2)
            if(valor_defesa(game,player,nlinhas+1,ncolunas+1) == None):
                build_window(ball,pixel_position_x_agent[ncolunas]+7,pixel_position_y[nlinhas]+2)


            elif(valor_defesa(game,player,nlinhas+1,ncolunas+1) == 0):
                build_window(ball,pixel_position_x_agent[ncolunas]+7,pixel_position_y[nlinhas]+2)


            elif(valor_defesa(game,player,nlinhas+1,ncolunas+1) > 0):
                build_window(explusion,pixel_position_x_agent[ncolunas]+7,pixel_position_y[nlinhas]+2)


            elif(valor_defesa(game,player,nlinhas+1,ncolunas+1) < 0):
                build_window(explusion,pixel_position_x_agent[ncolunas]+7,pixel_position_y[nlinhas]+2)


            if(terminou(game) != (None,None)):
                if(terminou(game)[1] == 2):
                    build_window(winner2,650,54)
                    state = 2
                else:
                    build_window(winner1,75,54)
                    state = 2

            print()
            for i in game[0]:
                print(*i)

            print()
            print()
            for i in game[2]:
                print(*i)



    
    else:
        if played == False:
            (nlinhas,ncolunas) = agente_joga(game,1)
            if(valor_defesa(game,player,nlinhas+1,ncolunas+1) == None):
                build_window(ball,pixel_position_x_agent[ncolunas]+7,pixel_position_y[nlinhas]+2)
                played = True

            elif(valor_defesa(game,player,nlinhas+1,ncolunas+1) == 0):
                build_window(ball,pixel_position_x_agent[ncolunas]+7,pixel_position_y[nlinhas]+2)
                played = True

            elif(valor_defesa(game,player,nlinhas+1,ncolunas+1) > 0):
                build_window(explusion,pixel_position_x_agent[ncolunas]+7,pixel_position_y[nlinhas]+2)
                played = True

            elif(valor_defesa(game,player,nlinhas+1,ncolunas+1) < 0):
                build_window(explusion,pixel_position_x_agent[ncolunas]+7,pixel_position_y[nlinhas]+2)
                played = True

            if(terminou(game) != (None,None)):
                build_window(winner2,650,54)
                state = 2
            

        if(mouse_click and 34 < position_mouse_x < 564 and 35< position_mouse_y < 365 and played):
            mouse_click = False
            for a in range(11):
                if pixel_x != 0 and pixel_y != 0:
                    break

                if pixel_position_x[a] > position_mouse_x and pixel_x == 0:
                    pixel_x = pixel_position_x[a-1]+7
                    value_a_x = a

                if pixel_position_y[a] > position_mouse_y and pixel_y == 0:
                    pixel_y = pixel_position_y[a-1]+2
                    value_a_y = a
   
            if(valor_ataque(game,player,value_a_y,value_a_x) == None):
                build_window(ball,pixel_x,pixel_y)
                tiro(game,player,value_a_y,value_a_x)
                played = False

            elif(valor_ataque(game,player,value_a_y,value_a_x) == 0):
                build_window(ball,pixel_x,pixel_y)
                tiro(game,player,value_a_y,value_a_x)
                played = False

            elif(valor_ataque(game,player,value_a_y,value_a_x) > 0):
                build_window(explusion,pixel_x,pixel_y)
                tiro(game,player,value_a_y,value_a_x)
                played = False

            elif(valor_ataque(game,player,value_a_y,value_a_x) < 0):
                build_window(explusion,pixel_x,pixel_y)
                tiro(game,player,value_a_y,value_a_x)
                played = False

            if(terminou(game) != (None,None)):
                if(terminou(game)[1] == 1):
                    build_window(winner2,650,54)
                    state = 2
                else:
                    build_window(winner1,75,54)
                    state = 2
            

            print()
            for i in game[0]:
                print(*i)

            print()
            print()
            for i in game[2]:
                print(*i)

#função que gere a interactividade quando o jogo acaba
def vicorious_interaction():

    global position_mouse_x
    global position_mouse_y
    global mouse_click
    global state
    global end
    global generator
    global player

    if(terminou(game)[1] == 1):
        if(player == 1):
            if(mouse_click and 196 < position_mouse_x < 253 and 289< position_mouse_y < 315):
                mouse_click = False
                state = 0
                display = pygame.display.set_mode((700,500))
                generator = True

            elif(mouse_click and 327 < position_mouse_x < 382 and 289< position_mouse_y < 315):
                end = True

            elif(mouse_click):
                mouse_click = False
        else:
            if(mouse_click and 769 < position_mouse_x < 826 and 289< position_mouse_y < 315):
                mouse_click = False
                state = 0
                display = pygame.display.set_mode((700,500))
                generator = True

            elif(mouse_click and 911 < position_mouse_x < 969 and 289< position_mouse_y < 315):
                end = True

            elif(mouse_click):
                mouse_click = False

    else:
        if(player == 1):
            if(mouse_click and 769 < position_mouse_x < 826 and 289< position_mouse_y < 315):
                mouse_click = False
                state = 0
                display = pygame.display.set_mode((700,500))
                generator = True

            elif(mouse_click and 911 < position_mouse_x < 969 and 289< position_mouse_y < 315):
                end = True

            elif(mouse_click):
                mouse_click = False

        else:
            if(mouse_click and 196 < position_mouse_x < 253 and 289< position_mouse_y < 315):
                mouse_click = False
                state = 0
                display = pygame.display.set_mode((700,500))
                generator = True

            elif(mouse_click and 327 < position_mouse_x < 382 and 289< position_mouse_y < 315):
                end = True

            elif(mouse_click):
                mouse_click = False

#função que gere as janelas
def manage_window():
    global state
    global generator

    if(state == 0):
        if generator:
            regeneration()
            input_boats_on_grid()
            generator = False

        else:
            interaction_button()


    elif(state == 1):
        game_interaction()

    elif(state == 2):
        vicorious_interaction()

    elif(state == 4):
        menu_context()

    elif(state == 5):
        context_settings()

    elif(state == 6):
        context_credits()
        


#função de loop do jogo
def game_loop():
    global end
    division_values()
    start_variables()
        

    while not(end):
        pygame_events()
        manage_window()

        #funciona igual ao flip() mas dá para atualizar apenas uma parte do ecrã passando argumentos
        pygame.display.update()


        # esperar o tempo necessário para cumprir o frame rate
        # só deve ser chamado uma vez por frame
        clock.tick(30)

    pygame.quit()
    quit()

game_loop()


