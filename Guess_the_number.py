import random

num_in_guess = random.randint(1, 20)
print(num_in_guess)
attempts = 0

print("Welcome to the Game!")
print("I'm thinking of a number between 1 and 20.")

while True:
    guess = int(input("Enter a guess: "))
    attempts += 1 # attempts = 1
    print("Attempts: ", attempts)

    if guess < num_in_guess:
        print("Your guess is too low.")
    elif guess > num_in_guess:
        print("Your guess is too high.")
    else:
        print(f"Congrats!... You guessed the number in {attempts} attempts.")
        break