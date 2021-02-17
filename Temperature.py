temp = eval(input('Enter a temperature in Celsius: '))

if temp < -273.15:
    print('invalid because it is below absolute zero')
elif temp == -273.15:
    print('absolute zero')
elif temp == 0:
    print('freezing point')
elif temp >0 and temp <100:
    print(' normal range')
elif temp == 100:
    print('at the boiling point')
else:
    print('above the boiling point')
