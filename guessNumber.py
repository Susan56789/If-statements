from random import randint
num = randint(1, 10)
guess = eval(input('Guess a number:'))
if guess == num:
    print('You got it !')
else:
    print('Sorry. The number is ', num)
