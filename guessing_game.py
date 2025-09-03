import random


def exit():
    return False

def guessing_game():
    print("==================================================")
    print("Welcome to the Guessing Game!")
    print("==================================================")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.")
    print("--------------------------------------------------")

    guess_numer = random.randint(1, 100)
    tries = 0
    
    while True:
        try:
            user_guess = input("Enter your guess: ")
            user_guess = int(user_guess)
            tries +=1
            if user_guess > guess_numer:
                print("Too high!")
            elif user_guess < guess_numer:
                print("Too low!")
            else:
                print(f"Congratulations! You finally guessed the number in only {tries} attemps")
                new_game = input("Play again? Type 'exit' to exit the game.")
                if new_game == "exit":
                    return False
                guess_numer = random.randint(1, 100)
                tries = 0
        except:
            if user_guess == "exit":
                return False
            print("Pleace pick a number!")

def main():
    guessing_game()

if __name__ == "__main__":
    main()