from random import randint

print ('Hello! I am TheGAME. What is your name?')
print ('Enter your name: ')
name = raw_input()
print ('Nice to meet you, ' + name)
print (name + ' likes icecream') 
number = randint(0,20)
print ('\nWell... I am thinking of a number from 0 to 20.')
print ('Try guessing it! You\'ve got only 4 guesses.')
guessNumber = 0

while guessNumber < 4:
    print ('\nGuess a number.')
    guess = raw_input()
    guess = int(guess)
    guessNumber = guessNumber + 1

    if guess <= number - 3:
       print ('Your guess is too low.')
    if guess >= number + 3:
       print ('Your guess is too high.')
    if (guess > number - 3) & (guess < number + 3) & (guess != number):
       print ('You are near my number')
    if guess == number:
       break

if guess == number:
    guessNumber = str(guessNumber)
    print ('Hurray! You guessed my number in ' + guessNumber + ' guesses.')

if guess != number:
    number = str(number)
    print ('Oops, bad luck! My number was ' + number)

print ('\nThanks for playing!')
