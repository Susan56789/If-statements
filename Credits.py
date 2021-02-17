credits = eval(input('How many credits have you taken?'))
if credits <=23:
    print('You are a freshman')
elif credits >=24 and credits <=53:
    print('You are a sophomore')
elif credits >=54 and credits <=83:
    print('You are a junior')
elif credits >= 84:
    print('You are a senior ')
else:
    print('Invalid')
