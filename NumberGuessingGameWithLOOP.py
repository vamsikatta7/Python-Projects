import random
input('Hey ! This is a guessing game. Hit Enter to continue')
num = int(input('Type any number of your choice: '))

input('Game Starts Now !! Hit enter ')
a = random.randint(1, num)

i = 0
b = None

while b != a:

    chances = int(3 - i)

    b = int(input('Enter a number '))
    if b == a:
        print('Your guess is correct')
        break
    else:
        print('Wrong Guess, Try again')
        i = i+1
        print("you have {} more chances".format(chances))
    if chances == 0:
        print('Sorry ! You ran out of turns')
        break

print('Thank you for playing')
