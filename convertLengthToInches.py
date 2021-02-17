length = eval(input('Enter the length in centimeters: '))
if length < 0:
    print('The entry is invalid')
else:
    print((length/2.54), 'inches')
