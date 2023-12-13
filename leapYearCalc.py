sct211-0060/2022
Njoroge Kimberly

import math
while True:
    try:
        year = int(input('Enter year: '))
        break
    except:
        print('Invalid. Retry.')
        continue
temp = math.ceil(year/100) * 100

if temp == year:
    if (year % 400) != 0:
        print(year, 'is not a leap year')
    else:
        print(year, 'is a leap year')
else:
    if (year % 4) != 0:
        print(year, 'is not a leap year')
    else:
        print(year, 'is a leap year')