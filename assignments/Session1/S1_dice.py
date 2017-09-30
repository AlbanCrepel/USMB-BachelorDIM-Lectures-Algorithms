import random

playerPoints = 0
computerPoints = 0

playersTurn = False
wantsToStop = 0

while playerPoints < 100 and computerPoints < 100 :
	playersTurn = not playersTurn
	wantsToStop = 0
	diceValue = -1
	turnScore = 0

	if playersTurn:
		print "\n*** Player playing ***"
		while wantsToStop == 0 and diceValue != 1:
			diceValue = random.randint(1, 6)
			print "Value of the dice : " + str(diceValue)
			if diceValue != 1:
				turnScore += diceValue
				print "Your score : " + str(playerPoints + turnScore)
				wantsToStop = input("Do you want to stop (0 : no ; 1 : yes) ? ")
				if wantsToStop == 1:
					playerPoints += turnScore
			else:
				print "You lost " + str(turnScore) + " points"
				print "Your current score : " + str(playerPoints)

	else:
		print "\n*** Computer playing ***"
		while wantsToStop == 0 and diceValue != 1:
			diceValue = random.randint(1, 6)
			print "Value of the dice : " + str(diceValue)
			if diceValue != 1:
				turnScore += diceValue
				print "The computer's score : " + str(computerPoints + turnScore)
				wantsToStop = random.randint(0, 1)
				if wantsToStop == 1:
					print "The computer stops here"
					computerPoints += turnScore
				else:
					print "The computer wants to continue"
			else:
				print "The computer lost " + str(turnScore) + " points"
				print "The computer current score : " + str(computerPoints)


print "Final score | YOU : " + str(playerPoints) + " COMPUTER : " + str(computerPoints)
if playersTurn:
	print "You win"
else :
	print "The computer wins"
