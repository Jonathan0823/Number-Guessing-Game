import random
quit = ""
low = 1
high = 100
while True:
    if quit == "n":
        break
    else:
        guesses = 0
        answer = random.randint(low, high)
        isRunning = True

        print("\n\n====Number Guessing Game====")
        print(f"Guess a number between {low} and {high}")

        while isRunning:
            guess = input("Enter your guess: ")

            if guess.isdigit():
                guess = int(guess)
                guesses += 1
                if guess > answer:
                    print("Lower")
                elif guess < answer:
                    print("Higher")
                else:
                    print(f"You guessed it in {guesses} guesses")
                    isRunning = False
            else:
                print("Invalid input")
            
        quit = input("Would you like to play again? (y/n): ").lower()
        
print("Bye")