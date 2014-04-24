import random

f = open("highscore.txt", "r+")
highscore = int(f.read())
flag = True
score = 0
print "It's a coin guessing game. Your highscore is", highscore
while flag == True:
	guess = int(raw_input("Head(0) or tail(1)? >> "))
	if guess == random.randint(0, 1):
		score = score + 1
		print "You are correct. Score:", score
	else:
		print "You are wrong. Game over."
		flag = False
		if score > highscore:
			f.seek(0)
			f.truncate()
			f.write(str(score))
			highscore = score
print "Your Score:", score, " All time highscore:", highscore