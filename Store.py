item = eval(input('How many items are you buyimg? '))
# price in $
if item < 10:
    tprice = item * 12
    print('Total cost:', tprice)
elif item > 10 and item <= 99:
    tprice = item * 10
    print('Total cost:', tprice)
else:
    tprice = item * 5
    print('Total cost:', tprice)
