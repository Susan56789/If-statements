temp = eval(input('Enter the temperature: '))
unit = input('What unit?Celsius or Fahrenheit: ')

if unit == 'Celsius':
    print('Converted to Fahrenheit is: ', ((9/5)*temp+32))
else:
    print('Converted to Celsius is:', ((9/5)*(temp-32)))
