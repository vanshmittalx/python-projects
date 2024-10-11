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