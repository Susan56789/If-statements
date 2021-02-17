# multiplication game program for kids

from random import randint
x = randint(1, 10)
y = randint(1, 10)
print('Question: ', x, '*', y)
answer = eval(input('Answer:'))

if answer == (x*y):
    print('Right !')
else:
    print('Wrong. The answer is :', x*y)
