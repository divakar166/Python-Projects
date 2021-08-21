import random,time

choices = ['Rock','Paper','Scissor']
computer = c = 0
player = p = 0

def score_show():
	print('Score -  Computer : ' + str(c) + ' | Player : ' + str(p))

def show_choices(player_choice,computer_choice):
	print('Player choice : ' + player_choice)
	time.sleep(1)
	print('Computer choice : ' + computer_choice)
	print('...')
	time.sleep(1)

while True:
	score_show()
	computer_choice = random.choice(choices)
	player_choice = input('Choose Rock(r), Paper(p), Scissor(s) or Quit(q)')
	if player_choice == 'r':
		player_choice = 'Rock'
	elif player_choice == 'p':
		player_choice = 'Paper'
	elif player_choice == 's':
		player_choice = 'Scissor'
	elif player_choice == 'q':
		player_choice = 'Quit'
	else:
		print('Wrong command..!')
		continue

	if computer_choice == player_choice:
		print("It's a tie!")
	elif player_choice == 'Rock':
		if computer_choice == 'Paper':
			show_choices(player_choice,computer_choice)
			print('Computer Wins!')
			c += 1
		elif computer_choice == 'Scissor':
			show_choices(player_choice,computer_choice)
			print('Player Wins!')
			p += 1
	elif player_choice == 'Paper':
		if computer_choice == 'Rock':
			show_choices(player_choice,computer_choice)
			print('Player Wins!')
			p += 1
		elif computer_choice == 'Scissor':
			show_choices(player_choice,computer_choice)
			print('Computer Wins!')
			c += 1
	elif player_choice == 'Scissor':
		if computer_choice == 'Rock':
			show_choices(player_choice,computer_choice)
			print('Computer Wins!')
			c += 1
		elif computer_choice == 'Paper':
			show_choices(player_choice,computer_choice)
			print('Player Wins!')
			p += 1
	elif player_choice == 'Quit':
		score_show()
		if c > p:
			print('Aww...Computer Won!')
		elif c < p:
			print('Hurray..Player Won!')
		else:
			print("Huf..It's a Tie!")
		break