#função de novo jogo
def novo_jogo():

	grelha_1 = [[None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None]]

	grelha_2 = [[None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None],
				 [None,None,None,None,None,None,None,None,None,None]]

	frota_1 = [[[8,8,8],[None,8,None],[None,8,None]],[[6,6,6,6]],[[4,4,4]],[[2,2]],[[2,2]],[[1]],[[1]],[[1]]]

	frota_2 = [[[8,8,8],[None,8,None],[None,8,None]],[[6,6,6,6]],[[4,4,4]],[[2,2]],[[2,2]],[[1]],[[1]],[[1]]]

	jogo = (grelha_1,frota_1,grelha_2,frota_2)

	return jogo

#obter dimensão da grelha do jogo
def get_dimensao_grelha(jogo):

	nlinhas = len(jogo[0])

	ncolunas = len(jogo[0][0])

	return (nlinhas,ncolunas)

#função para obter todas as posições do jogo, usado direto o 19 porque na parte grafica estava a gerar erros
def get_numero_barcos(jogo):
	
	nbarcos = 19

	return nbarcos

#função para obter individualmente cada barco, esta função nunca é usada
def get_barco(jogo,numero_jogador,numero_barco):

	if(numero_jogador == 1):
		for a in range(len(jogo[1])):
			if(numero_barco == jogo[1][a][0][0]):
				barco = jogo[1][a]
				return barco

	elif(numero_jogador == 2):
		for a in range(len(jogo[3])):
			if(numero_barco == jogo[3][a][0][0]):
				barco = jogo[3][a]
				return barco

#função auxiliar para rodar uma lista em 90º
def roda_sentido_horario(matriz):

	resultado = list(map(list, zip(*matriz)))[::-1]

	return resultado

#função que quando de roda o barco incrementa o seu valor
def incrementa_valor_barco(matriz):

	number = 0

	for a in range(len(matriz)):
		for b in range(len(matriz[a])):
			if(matriz[a][b] != None):
				number = matriz[a][b]
				break


	if(number == 11):
		for c in range(len(matriz)):
			for d in range(len(matriz[c])):
				if(matriz[c][d] != None):
					matriz[c][d] = 8	
		return matriz


	elif(number > 7 and number < 11):
		for c in range(len(matriz)):
			for d in range(len(matriz[c])):
				if(matriz[c][d] != None):
					matriz[c][d] = matriz[c][d]+1			
		return matriz


	elif(number == 7 or number == 5 or number == 3):
		for c in range(len(matriz)):
			for d in range(len(matriz[c])):
				matriz[c][d] = matriz[c][d]-1	
		return matriz


	elif(number == 6 or number == 4 or number == 2):
		for c in range(len(matriz)):
			for d in range(len(matriz[c])):
				matriz[c][d] = matriz[c][d]+1	
		return matriz

#função de rodar os barcos
def roda_barco(jogo,numero_jogador, numero_barco):


	if(numero_jogador == 1):

		if(numero_barco == 8 or numero_barco == 9 or numero_barco == 10 or numero_barco == 11):
			rodado = roda_sentido_horario(jogo[1][0])
			jogo[1][0] = incrementa_valor_barco(rodado)

		elif(numero_barco == 6 or numero_barco == 7):
			rodado = roda_sentido_horario(jogo[1][1])
			jogo[1][1] = incrementa_valor_barco(rodado)

		elif(numero_barco == 4 or numero_barco == 5):
			rodado = roda_sentido_horario(jogo[1][2])
			jogo[1][2] = incrementa_valor_barco(rodado)

		elif(numero_barco == 2 or numero_barco == 3):
			rodado = roda_sentido_horario(jogo[1][3])
			jogo[1][3] = incrementa_valor_barco(rodado)
			rodado = roda_sentido_horario(jogo[1][4])
			jogo[1][4] = incrementa_valor_barco(rodado)

	elif(numero_jogador == 2):

		if(numero_barco == 8 or numero_barco == 9 or numero_barco == 10 or numero_barco == 11):
			rodado = roda_sentido_horario(jogo[3][0])
			jogo[3][0] = incrementa_valor_barco(rodado)

		elif(numero_barco == 6 or numero_barco == 7):
			rodado = roda_sentido_horario(jogo[3][1])
			jogo[3][1] = incrementa_valor_barco(rodado)

		elif(numero_barco == 4 or numero_barco == 5):
			rodado = roda_sentido_horario(jogo[3][2])
			jogo[3][2] = incrementa_valor_barco(rodado)

		elif(numero_barco == 2 or numero_barco == 3):
			rodado = roda_sentido_horario(jogo[3][3])
			jogo[3][3] = incrementa_valor_barco(rodado)
			rodado = roda_sentido_horario(jogo[3][4])
			jogo[3][4] = incrementa_valor_barco(rodado)

#função para colocar os barcos na grelha, esta função nunca é usada pois é utilizada a função do agente
def coloca_barco(jogo, numero_jogador, numero_barco, linha, coluna):

	if(numero_jogador == 1):
		if(numero_barco == 8 or numero_barco == 9 or numero_barco == 10 or numero_barco == 11):
			if(linha < 9 and coluna < 10 and linha > 0 and linha > 0):
				jogo[0][linha-1][coluna-2] =   jogo[1][0][0][0]
				jogo[0][linha-1][coluna-1] =     jogo[1][0][0][1]
				jogo[0][linha-1][coluna] =   jogo[1][0][0][2]
				jogo[0][linha][coluna-2] =     jogo[1][0][1][0]
				jogo[0][linha][coluna-1] =       jogo[1][0][1][1]
				jogo[0][linha][coluna] =     jogo[1][0][1][2]
				jogo[0][linha+1][coluna-2] =   jogo[1][0][2][0]
				jogo[0][linha+1][coluna-1] =     jogo[1][0][2][1]
				jogo[0][linha+1][coluna] =   jogo[1][0][2][2]

		elif(numero_barco == 7):
			if(linha > 0 and linha < 8 and coluna > 0 and coluna < 11):
				jogo[0][linha-1][coluna-1] = jogo[1][1][0][0]
				jogo[0][linha][coluna-1] =   jogo[1][1][1][0]
				jogo[0][linha+1][coluna-1] = jogo[1][1][2][0]
				jogo[0][linha+2][coluna-1] = jogo[1][1][3][0]


		elif(numero_barco == 6):
			if(coluna < 8 and coluna > 0 and linha > 0 and linha < 11):
				jogo[0][linha-1][coluna-1] =   jogo[1][1][0][0]
				jogo[0][linha-1][coluna] = jogo[1][1][0][1]
				jogo[0][linha-1][coluna+1] = jogo[1][1][0][2]
				jogo[0][linha-1][coluna+2] = jogo[1][1][0][3]

		elif(numero_barco == 5):
			if(linha > 0 and linha < 9 and coluna > 0 and coluna < 11):
				jogo[0][linha-1][coluna-1] = jogo[1][2][0][0]
				jogo[0][linha][coluna-1] =   jogo[1][2][1][0]
				jogo[0][linha+1][coluna-1] = jogo[1][2][2][0]


		elif(numero_barco == 4):
			if(coluna > 0 and coluna < 9 and linha > 0 and linha < 11):
				jogo[0][linha-1][coluna-1] =   jogo[1][2][0][0]
				jogo[0][linha-1][coluna] = jogo[1][2][0][1]
				jogo[0][linha-1][coluna+1] = jogo[1][2][0][2]


		elif(numero_barco == 3):
			if(linha > 0 and linha < 10 and coluna > 0 and coluna < 11):
				jogo[0][linha-1][coluna-1] = jogo[1][3][0][0]
				jogo[0][linha][coluna-1] =   jogo[1][3][1][0]

		elif(numero_barco == 2):
			if(coluna < 10 and coluna > 0 and linha > 0 and linha < 11):
				jogo[0][linha-1][coluna-1] =   jogo[1][3][0][0]
				jogo[0][linha-1][coluna] = jogo[1][3][0][1]

		elif(numero_barco == 1):
			if(coluna < 11 and coluna > 0 and linha > 0 and linha < 11):
				jogo[0][linha-1][coluna-1] = numero_barco

	elif(numero_jogador == 2):
		if(numero_barco == 8 or numero_barco == 9 or numero_barco == 10 or numero_barco == 11):
			if(linha < 9 and coluna < 10 and linha > 0 and linha > 0):
				jogo[2][linha-1][coluna-2] =   jogo[3][0][0][0]
				jogo[2][linha-1][coluna-1] =     jogo[3][0][0][1]
				jogo[2][linha-1][coluna] =   jogo[3][0][0][2]
				jogo[2][linha][coluna-2] =     jogo[3][0][1][0]
				jogo[2][linha][coluna-1] =       jogo[3][0][1][1]
				jogo[2][linha][coluna] =     jogo[3][0][1][2]
				jogo[2][linha+1][coluna-2] =   jogo[3][0][2][0]
				jogo[2][linha+1][coluna-1] =     jogo[3][0][2][1]
				jogo[2][linha+1][coluna] =   jogo[3][0][2][2]

		elif(numero_barco == 7):
			if(linha > 0 and linha < 8 and coluna > 0 and coluna < 11):
				jogo[2][linha-1][coluna-1] = jogo[3][1][0][0]
				jogo[2][linha][coluna-1] =   jogo[3][1][1][0]
				jogo[2][linha+1][coluna-1] = jogo[3][1][2][0]
				jogo[2][linha+2][coluna-1] = jogo[3][1][3][0]


		elif(numero_barco == 6):
			if(coluna < 8 and coluna > 0 and linha > 0 and linha < 11):
				jogo[2][linha-1][coluna-1] =   jogo[3][1][0][0]
				jogo[2][linha-1][coluna] = jogo[3][1][0][1]
				jogo[2][linha-1][coluna+1] = jogo[3][1][0][2]
				jogo[2][linha-1][coluna+2] = jogo[3][1][0][3]

		elif(numero_barco == 5):
			if(linha > 0 and linha < 9 and coluna > 0 and coluna < 11):
				jogo[2][linha-1][coluna-1] = jogo[3][2][0][0]
				jogo[2][linha][coluna-1] =   jogo[3][2][1][0]
				jogo[2][linha+1][coluna-1] = jogo[3][2][2][0]


		elif(numero_barco == 4):
			if(coluna > 0 and coluna < 9 and linha > 0 and linha < 11):
				jogo[2][linha-1][coluna-1] =   jogo[3][2][0][0]
				jogo[2][linha-1][coluna] = jogo[3][2][0][1]
				jogo[2][linha-1][coluna+1] = jogo[3][2][0][2]


		elif(numero_barco == 3):
			if(linha > 0 and linha < 10 and coluna > 0 and coluna < 11):
				jogo[2][linha-1][coluna-1] = jogo[3][3][0][0]
				jogo[2][linha][coluna-1] =   jogo[3][3][1][0]

		elif(numero_barco == 2):
			if(coluna < 10 and coluna > 0 and linha > 0 and linha < 11):
				jogo[2][linha-1][coluna-1] =   jogo[3][3][0][0]
				jogo[2][linha-1][coluna] = jogo[3][3][0][1]

		elif(numero_barco == 1):
			if(coluna < 11 and coluna > 0 and linha > 0 and linha < 11):
				jogo[2][linha-1][coluna-1] = numero_barco

#função que permite saber se os barcos já estão todos colocados na grelha
def barcos_prontos(jogo,numero_jogador):

	counter = 0

	if(numero_jogador == 1):
		for a in range(len(jogo[0])):
			for b in range(len(jogo[0][a])):
				if(jogo[0][a][b] != None):
					counter+= 1
		if(counter == 19):
			return True
		else:
			return False
	elif(numero_jogador == 2):
		for a in range(len(jogo[2])):
			for b in range(len(jogo[2][a])):
				if(jogo[2][a][b] != None):
					counter+= 1
		if(counter == 19):
			return True
		else:
			return False

#função permite saber o valor de uma dada linha e coluna na grelha no proprio jogo
def valor_defesa(jogo,numero_jogador,linha,coluna):

	if(numero_jogador == 1):
		if(jogo[0][linha-1][coluna-1] == None):
			return None

		elif(jogo[0][linha-1][coluna-1] == 0):
			return 0

		elif(jogo[0][linha-1][coluna-1] > 0):
			return jogo[0][linha-1][coluna-1]

		elif(jogo[0][linha-1][coluna-1] < 0):
			return jogo[0][linha-1][coluna-1]


	elif(numero_jogador == 2):
		if(jogo[2][linha-1][coluna-1] == None):
			return None

		elif(jogo[2][linha-1][coluna-1] == 0):
			return 0

		elif(jogo[2][linha-1][coluna-1] > 0):
			return jogo[2][linha-1][coluna-1]

		elif(jogo[2][linha-1][coluna-1] < 0):
			return jogo[2][linha-1][coluna-1]

#função que permite saber o valor de uma dada linha e coluna do jogo adversário
def valor_ataque(jogo,numero_jogador, linha, coluna):


	if(numero_jogador == 1):
		if(jogo[2][linha-1][coluna-1] == None):
			return None

		elif(jogo[2][linha-1][coluna-1] == 0):
			return 0

		elif(jogo[2][linha-1][coluna-1] > 0):
			return jogo[2][linha-1][coluna-1]

		elif(jogo[2][linha-1][coluna-1] < 0):
			return jogo[2][linha-1][coluna-1]


	elif(numero_jogador == 2):
		if(jogo[0][linha-1][coluna-1] == None):
			return None

		elif(jogo[0][linha-1][coluna-1] == 0):
			return 0

		elif(jogo[0][linha-1][coluna-1] > 0):
			return jogo[0][linha-1][coluna-1]

		elif(jogo[0][linha-1][coluna-1] < 0):
			return jogo[0][linha-1][coluna-1]

#permite mudar o valor da grelha de um jogador numa dada posição
def tiro(jogo,numero_jogador,linha,coluna):

	if(numero_jogador == 1):
		if(jogo[2][linha-1][coluna-1] == None):
			jogo[2][linha-1][coluna-1] = 0


		elif(jogo[2][linha-1][coluna-1] > 0):
			jogo[2][linha-1][coluna-1] = jogo[2][linha-1][coluna-1]*(-1)

	elif(numero_jogador == 2):
		if(jogo[0][linha-1][coluna-1] == None):
			jogo[0][linha-1][coluna-1] = 0


		elif(jogo[0][linha-1][coluna-1] > 0):
			jogo[0][linha-1][coluna-1] = jogo[0][linha-1][coluna-1]*(-1)

#função que permite saber se o jogo já terminou
def terminou(jogo):
	counter_1 = 0

	counter_2 = 0

	for a in range(len(jogo[0])):
		for b in range(len(jogo[0][a])):
			if(jogo[0][a][b] != None):
				if(jogo[0][a][b] < 0):
					counter_1 += 1

			if(jogo[2][a][b] != None):
				if(jogo[2][a][b] < 0):
					counter_2 += 1

	if(counter_1 == 19):
		return (True,2)

	elif(counter_2 == 19):
		return (True,1)

	else:
		return (None,None)

