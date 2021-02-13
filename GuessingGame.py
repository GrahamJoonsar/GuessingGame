import random

counter = 0

print("This is the guessing game.\nI have chosen a number between 1 and 100.\nTry to guess.")
number = int(random.randint(1, 100))

def game():
    global counter
    try:
        guess = int(input("\nGuess a number: "))
        if guess <= 100 and guess >= 1:
            counter += 1
            if guess == number:
                print("You got it!")
                print(f"It only took you {counter} guesses.")
            elif guess < number and guess > number - 10:
                print("Just a little higher!")
                game()
            elif guess > number and guess < number + 10:
                print("Just a little lower!")
                game()
            elif guess > number:
                print("Lower!")
                game()
            else:
                print("Higher!")
                game()
        else:
            print("That's not a number 1-100.")
            game()
    except ValueError:
        print("That's not a number.")
        game()
game()