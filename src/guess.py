# this is a guess the number game
import random
print('Hello. What is your name?')
name = input()
random_number = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

# ask the player to guess 6 times
for guess_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < random_number:
        print('Your guess is too low')
    elif guess > random_number:
        print('Your guess is too high')
    else:
        break  # the user guessed the right answer

if guess == random_number:
    print('Good job, ' + name + '! You guessed my number in ' +
          str(guess_taken) + ' guesses')
else:
    print('Nope the number I was thinking of was ' + str(random_number))
