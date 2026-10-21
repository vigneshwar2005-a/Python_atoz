import modulex
import datetime
import math
modulex.greeting('V')
modulex.emp.empdetails('V',189000)

# Built in 

#Python date

''' A date in python is not a datatype of its own but we can import a module 
named datetime to work with date as date object.'''

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.month)
print(x.day)
print(x.strftime('%A'))
print(x.strftime('%a'))

'''Week day as a number 0-6 where 0 = sunday'''
print(x.strftime('%w')) 

'''Day of the the month'''
print(x.strftime('%d'))

'''Shortform of the current month'''
print(x.strftime('%b'))

'''Fullform of the current monht '''
print(x.strftime('%B'))

'''Number of the month'''
print(x.strftime('%m'))

'''Year in shortform'''
print(x.strftime('%y'))

'''Year in fullform'''
print(x.strftime('%Y'))

y = math.sqrt(25)
z = math.ceil(1.4)
a = math.floor(2.6)
v = 'Heyvigneshwar' 

print(len(v))
print(a)
print(z)
print(y)