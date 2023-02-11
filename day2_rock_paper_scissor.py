f = open('input1_day2_2022.txt','r')
lista = f.read().rsplit('\n')
player1 = [ x[0] for x in lista if len(x) ==3] # make sure the lines have the same format
player2 = [ x[-1] for x in lista if len(x) ==3]
# A=rock, B=paper, C=Scissor
# X = rock, Y=paper, Z=Scissor
# rock win = 1 + 6
# paper win = 2 + 6
# scissor win = 3 + 6
# rock withdraw = 1 + 3
# paper wd = 2 + 3
# scissor wd = 3 + 3
# rock lost = 1
# paper lost = 2
#scissor lost = 3
acu_score = 0
for count, value in enumerate(player2):
	if value == 'X':
		acu_score = acu_score + 1
		if player1[count] == 'A':
			acu_score = acu_score + 3
		elif player1[count] == 'C':
			acu_score = acu_score + 6
	elif value == 'Y':
		acu_score = acu_score + 2
		if player1[count] == 'A':
			acu_score = acu_score + 6
		elif player1[count] == 'B':
			acu_score = acu_score + 3
	elif value == 'Z':
		acu_score = acu_score + 3
		if player1[count] == 'B':
			acu_score = acu_score + 6
		elif player1[count] == 'C':
			acu_score = acu_score + 3
print ('Acumulate score: {}'.format(acu_score))