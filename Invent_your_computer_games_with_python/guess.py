import random

guesses_taken = 0
print('Hello! What is your name?')
my_name = input()

number = random.randint(1, 20)

print(f"Well, {my_name}, I am thinking of a number between 1 and 20.")

for _ in range(6):
    print('Take a guess.') # Four spaces in front of "print"
    guess = int(input())
    guesses_taken += 1

    if guess < number:
        print('Your guess is too low.') # Eight spaces in front of "print"

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        print(f'Good job, {my_name}! You guessed my number in {guesses_taken} guesses!')
        break

if guess != number:
    print(f'Nope. The number I was thinking of was {number}.')