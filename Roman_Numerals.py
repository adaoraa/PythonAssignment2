# create code for roman numerals from 1 - 100

integer = int(input('Enter a number between 1 and 100: '))
ones = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X'}
numeral = {integer-10: 'teen', integer-20: 'twenties', integer-30: 'thirties', integer-40: 'forties',
           integer-50: 'fifties', integer-60: 'sixties', integer-70: 'seventies', integer-80: 'eighties',
           integer-90: 'nineties'}

if integer in range(1, 11):  # 1-10
    print(ones[integer])

if integer in range(11, 21):  # 11-20
    print('X'+ones[(integer-10)])

if integer in range(21, 31):  # 21-30
    print('XX'+ones[(integer-20)])

if integer in range(31, 41) and integer != 40:  # 31-40
    print('XXX'+ones[(integer-30)])
elif integer == 40:
    print('XL')

if integer in range(41, 51) and integer != 50:   # 41-50
    print('XL'+ones[(integer-40)])
elif integer == 50:
    print('L')

if integer in range(51, 61):  # 51-60
    print('L'+ones[(integer-50)])

if integer in range(61, 71):  # 61-70
    print('LX'+ones[(integer-60)])

if integer in range(71, 81):  # 71-80
    print('LXX'+ones[(integer-70)])

if integer in range(81, 91) and integer != 90:  # 81-90
    print('LXXX'+ones[(integer-80)])
elif integer == 90:
    print('XC')

if integer in range(91, 101) and integer !=100:  # 91-100
    print('XC'+ones[(integer-90)])
elif integer == 100:
    print('C')
