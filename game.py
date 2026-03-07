import random

secret_number = random.randint(1, 10)

print("Welcome to the Guessing Game!")
print("Guess a number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("🎉 Correct! You win!")
else:
    print("❌ Wrong! The number was", secret_number)
