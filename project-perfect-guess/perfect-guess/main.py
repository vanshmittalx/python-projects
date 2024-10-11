'''
This program is a game which generates a random number between 1 and 100, and lets the user guess it. if the guess is higher than the number it tells the user to guess lower and vice-versa. when the user guesses the number it tells how many guesses it took to guess the number.
'''

from random import randint

play = True
guess_count = 0
number = randint(1,100)
while play == True:
    guess = int(input("Guess a number between 1 and 100: "))
    guess_count = guess_count + 1
    if guess == number:
        print("You win!")
        print(f"Thank you for playing , number of guesses: {guess_count}")
        play = False
        break
    elif guess<number:
        print("higher guess please")
    else:
        print("lower guess please")
