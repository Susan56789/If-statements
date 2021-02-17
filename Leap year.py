year = eval(input('Write a year: '))

x = year % 4
y = year % 400

if x == 0 or y == 0:
    print('Leap year')
else:
    print('Not a leap year')
