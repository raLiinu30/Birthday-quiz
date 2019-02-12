"""
birthday.py
Author: Rain 
Credit: Mr. Dennison
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""

name = input('Hello, what is your name? ')
month = input('Hi '+name+', what was the name of the month you were born in? ').lower()
year = int(input('And what year were you born in, '+name+'? '))
day = int(input('And the day? '))

winter = ['december', 'january', 'february']
spring = ['march', 'april', 'may']
summer = ['june', 'july','august']
fall = ['september', 'october', 'november' ]
eighties = range(1980, 1990)
nineties = range(1990, 2000)

if month == 2 and day == 11:
    print('Happy birthday!')
if month == 'october' and day == 31:
    print('You were born on Halloween!')
if month in winter and year in eighties:
    print(name+', you are a winter baby of the eighties.')
if month in spring and year in eighties:
     print(name+', you are a spring baby of the eighties.')
if month in summer and year in eighties:
     print(name+', you are a summer baby of the eighties.')
if month in fall and year in eighties:
     print(name+', you are a fall baby of the eighties.')
if month in winter and year in nineties:
    print(name+', you are a winter baby of the nineties.')
if month in spring and year in nineties:
     print(name+', you are a spring baby of the nineties.')
if month in summer and year in nineties:
     print(name+', you are a summer baby of the nineties.')
if month in fall and year in nineties:
     print(name+', you are a fall baby of the nineties.')
if month in winter and year > 2000:
    print(name+', you are a winter baby of the two thousands.')
if month in spring and year > 2000:
     print(name+', you are a spring baby of the two thousands.')
if month in summer and year > 2000:
     print(name+', you are a summer baby of the two thousands.')
if month in fall and year > 2000:
     print(name+', you are a fall baby of the two thousands.')
if month in winter and year < 1980:
    print(name+', you are a winter baby of the Stone Age.')
if month in spring and year < 1980:
     print(name+', you are a spring baby of the Stone Age.')
if month in summer and year < 1980:
     print(name+', you are a summer baby of the Stone Age.')
if month in fall and year < 1980:
     print(name+', you are a fall baby of the Stone Age.')
    