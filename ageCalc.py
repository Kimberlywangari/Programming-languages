SCT211-0060/2022
Njoroge Kimberly Wangari

from dateutil import relativedelta
import datetime
birthDateString = input('Enter birth date in formart dd-mm-yy: ')
birthDateObject = datetime.datetime.strptime(birthDateString, "%d-%m-%Y").date()
todayDate = datetime.datetime.now().date()

day = todayDate - birthDateObject
diff = relativedelta.relativedelta(todayDate, birthDateObject)
months = diff.years * 12 + diff.months
print('You are', diff.years, 'Years old.')
print('You are', months, 'Months old.')
print('You are', day.days, 'Days old.')

