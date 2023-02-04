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



jogo = novo_jogo()

#print(jogo)

'''print("tamanho das linhas 1º jogador ",len(jogo[0]))

print("tamanho da colunas 1º jogador ",len(jogo[0][0]))


print("tamanho das linhas 2º jogador ",len(jogo[2]))

print("tamanho da colunas 2º jogador ",len(jogo[2][0]))


print("tamanho da frota 1º jogador ",len(jogo[1]))

print("tamanho da frota 2º jogador ",len(jogo[3]))


tamanho_grelha = get_dimensao_grelha(jogo)

print(tamanho_grelha)


numero_barcos = get_numero_barcos(jogo)

print(numero_barcos)

barco_8 = get_barco(jogo,1,8)

print(barco_8)

barco_8_2 = get_barco(jogo,2,8)

print(barco_8_2)


barco_6 = get_barco(jogo,1,6)

print(barco_6)

barco_6_2 = get_barco(jogo,2,6)

print(barco_6_2)

barco_4 = get_barco(jogo,1,4)

print(barco_4)

barco_4_2 = get_barco(jogo,2,4)

print(barco_4_2)


barco_2 = get_barco(jogo,1,2)

print(barco_2)

barco_2_2 = get_barco(jogo,2,2)

print(barco_2_2)


barco_1 = get_barco(jogo,1,1)

print(barco_1)

barco_1_2 = get_barco(jogo,2,1)

print(barco_1_2)'''

'''print(jogo[1][0])
roda_barco(jogo,1,8)
print(jogo[1][0])
roda_barco(jogo,1,8)
print(jogo[1][0])
roda_barco(jogo,1,8)
print(jogo[1][0])
roda_barco(jogo,1,8)
print(jogo[1][0])
roda_barco(jogo,1,6)
print(jogo[1][1])
roda_barco(jogo,1,6)
print(jogo[1][1])
roda_barco(jogo,1,6)
print(jogo[1][1])
roda_barco(jogo,1,4)
print(jogo[1][2])
roda_barco(jogo,1,4)
print(jogo[1][2])
roda_barco(jogo,1,4)
print(jogo[1][2])
roda_barco(jogo,1,2)
print(jogo[1][3])
print(jogo[1][4])
roda_barco(jogo,1,2)
print(jogo[1][3])
print(jogo[1][4])
roda_barco(jogo,1,2)
print(jogo[1][3])
print(jogo[1][4])'''


'''print(jogo[3][0])
roda_barco(jogo,2,8)
print(jogo[3][0])
roda_barco(jogo,2,8)
print(jogo[3][0])
roda_barco(jogo,2,8)
print(jogo[3][0])
roda_barco(jogo,2,8)
print(jogo[3][0])
roda_barco(jogo,2,6)
print(jogo[3][1])
roda_barco(jogo,2,6)
print(jogo[3][1])
roda_barco(jogo,2,6)
print(jogo[3][1])
roda_barco(jogo,2,4)
print(jogo[3][2])
roda_barco(jogo,2,4)
print(jogo[3][2])
roda_barco(jogo,2,4)
print(jogo[3][2])
roda_barco(jogo,2,2)
print(jogo[3][3])
print(jogo[3][4])
roda_barco(jogo,2,2)
print(jogo[3][3])
print(jogo[3][4])
roda_barco(jogo,2,2)
print(jogo[3][3])
print(jogo[3][4])'''

#print(jogo[0])


##### Falta testes ao coloca barco para o segundo player
'''coloca_barco(jogo,1,8,0,0)

print(jogo[0])

for i in jogo[0]:
	print(*i)
roda_barco(jogo,1,2)

print(jogo[0])'''




'''coloca_barco(jogo,2,1,1,1)
coloca_barco(jogo,2,1,2,1)
coloca_barco(jogo,2,1,3,1)
coloca_barco(jogo,2,2,4,1)
coloca_barco(jogo,2,2,5,1)
coloca_barco(jogo,2,4,6,1)
coloca_barco(jogo,2,6,7,1)
coloca_barco(jogo,2,8,7,6)

for i in jogo[2]:
	print(*i)


print(barcos_prontos(jogo,2))'''



'''print(valor_defesa(jogo,1,0,1))

jogo[0][2][1] = 5

print(valor_defesa(jogo,1,3,2))

jogo[0][3][1] = 0

print(valor_defesa(jogo,1,4,2))

jogo[0][7][1] = -5

print(valor_defesa(jogo,1,8,2))'''


'''print(valor_defesa(jogo,2,0,1))

jogo[2][1][1] = 5

print(valor_defesa(jogo,2,2,2))

jogo[2][2][1] = 0

print(valor_defesa(jogo,2,3,2))

jogo[2][6][1] = -5

print(valor_defesa(jogo,2,7,2))'''

'''print(valor_ataque(jogo,1,0,1))

jogo[2][1][1] = 5

print(valor_ataque(jogo,1,2,2))

jogo[2][2][1] = 0

print(valor_ataque(jogo,1,3,2))

jogo[2][6][1] = -5

print(valor_ataque(jogo,1,7,2))'''


'''print(valor_ataque(jogo,2,0,1))

jogo[0][1][1] = 5

print(valor_ataque(jogo,2,2,2))

jogo[0][2][1] = 0

print(valor_ataque(jogo,2,3,2))

jogo[0][6][1] = -5

print(valor_ataque(jogo,2,7,2))'''


'''print(jogo[2][0][0])

tiro(jogo,1,1,1)

print(jogo[2][0][0])

jogo[2][4][4] = 1

tiro(jogo,1,5,5)

print(jogo[2][4][4])'''

'''print(jogo[0][0][0])

tiro(jogo,2,1,1)

print(jogo[0][0][0])

jogo[0][4][4] = 1

tiro(jogo,2,5,5)

print(jogo[0][4][4])'''

'''print(terminou(jogo))

jogo[0][1][1] = -1
jogo[0][2][1] = -1
jogo[0][3][1] = -1
jogo[0][4][1] = -2
jogo[0][5][1] = -2
jogo[0][6][1] = -2
jogo[0][7][1] = -2

jogo[0][0][2] = -4
jogo[0][1][2] = -4
jogo[0][2][2] = -4
jogo[0][3][2] = -6
jogo[0][4][2] = -6
jogo[0][5][2] = -6
jogo[0][6][2] = -6

jogo[0][0][3] = -8
jogo[0][1][3] = -8
jogo[0][2][3] = -8
jogo[0][3][3] = -8
jogo[0][4][3] = -8

print(terminou(jogo))'''

'''print(terminou(jogo))


jogo[2][1][1] = -1
jogo[2][2][1] = -1
jogo[2][3][1] = -1
jogo[2][4][1] = -2
jogo[2][5][1] = -2
jogo[2][6][1] = -2
jogo[2][7][1] = -2

jogo[2][0][2] = -4
jogo[2][1][2] = -4
jogo[2][2][2] = -4
jogo[2][3][2] = -6
jogo[2][4][2] = -6
jogo[2][5][2] = -6
jogo[2][6][2] = -6

jogo[2][0][3] = -8
jogo[2][1][3] = -8
jogo[2][2][3] = -8
jogo[2][3][3] = -8
jogo[2][4][3] = -8

print(terminou(jogo))'''



'''roda_barco(jogo,1,8)
roda_barco(jogo,1,6)
roda_barco(jogo,1,4)
roda_barco(jogo,1,2)

print(jogo[1][0])


coloca_barcos_aleatoriamente(jogo,1)



#print(jogo[0])

for i in jogo[0]:
	print(*i)

count = 0
for a in range(len(jogo[0])):
	for b in range(len(jogo[0][a])):
		if(jogo[0][a][b] != None):
			count += 1
print(count)'''


'''roda_barco(jogo,2,8)
roda_barco(jogo,2,6)
roda_barco(jogo,2,4)
roda_barco(jogo,2,2)


coloca_barcos_aleatoriamente(jogo,2)



#print(jogo[0])

for i in jogo[2]:
	print(*i)

count = 0
for a in range(len(jogo[2])):
	for b in range(len(jogo[2][a])):
		if(jogo[2][a][b] != None):
			count += 1
print(count)'''


agente_joga(jogo,1)
agente_joga(jogo,1)
agente_joga(jogo,1)
agente_joga(jogo,1)
agente_joga(jogo,1)

agente_joga(jogo,2)
agente_joga(jogo,2)
agente_joga(jogo,2)
agente_joga(jogo,2)
agente_joga(jogo,2)


print(jogo[2])













