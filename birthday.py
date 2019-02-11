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
month = input('What is the name of the month were you were born in? ')
year = int(input('What year were you born in? '))
day = int(input('What day were you born in? '))

winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July','August']
fall = ['September', 'October', 'November' ]
eighties = range(1980, 1990)
nineties = (1990, 2000)


if month == 10 and day == 31:
    print('You were born on Halloween!')
elif month == 2 and day == 5:
    print('Happy birthday!')
elif month in winter and year in eighties:
    print(name+', you are a winter baby of the eighties.')
elif month in spring and year in eighties:
     print(name+', you are a spring baby of the eighties.')
elif month in summer and year in eighties:
     print(name+', you are a summer baby of the eighties.')
elif month in fall and year in eighties:
     print(name+', you are a fall baby of the eighties.')
elif month in winter and year in nineties:
    print(name+', you are a winter baby of the nineties.')
elif month in spring and year in nineties:
     print(name+', you are a spring baby of the nineties.')
elif month in summer and year in nineties:
     print(name+', you are a summer baby of the nineties.')
elif month in fall and year in nineties:
     print(name+', you are a fall baby of the nineties.')
elif month in winter and year > 2000:
    print(name+', you are a winter baby of the two thousands.')
elif month in spring and year > 2000:
     print(name+', you are a spring baby of the two thousands.')
elif month in summer and year > 2000:
     print(name+', you are a summer baby of the two thousands.')
elif month in fall and year > 2000:
     print(name+', you are a fall baby of the two thousands.')
elif month in winter and year < 1980:
    print(name+', you are a winter baby of the Stone Age.')
elif month in spring and year < 1980:
     print(name+', you are a spring baby of the Stone Age.')
elif month in summer and year < 1980:
     print(name+', you are a summer baby of the Stone Age.')
elif month in fall and year < 1980:
     print(name+', you are a fall baby of the Stone Age.')
    
    
    
    
    
    
    
    
    
    