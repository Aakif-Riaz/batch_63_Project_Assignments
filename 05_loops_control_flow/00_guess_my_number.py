def guess_the_number():
    import random

    secret_number = random.randint(1,99)

    guess = int(input("Guess the secret number: "))

    while guess != secret_number:
        if guess < secret_number:
            print("Your Guess is too low. Try again.")
        if guess > secret_number:
            print("Your Guess is too high. Try again.")

        guess = int(input("Try again: "))
    
    else:
        print(f"Congrats! You guessed the right number: {secret_number}")

guess_the_number()