grade = eval(input('What is your score?'))

if grade >= 70:
    print('Your grade is A')
elif grade >60 and grade <= 69:
    print('Your grade is B')
elif grade > 50 and grade <=59:
    print('Your grade is C')
elif grade >40 and grade <=49:
    print('Your grade is D')
else:
    print('Your grade is F')
