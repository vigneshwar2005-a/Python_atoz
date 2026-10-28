# For loop

'''A for loop is used for iterating over a sequence 
(list,tuple,Dictionary,stringand set).

With the for loop we can execute a set of statements, once for
each item in a list, tuple, set etc...'''

# Break statement 

''' With the break statement we can stop the loop before it has looped 
through all the items.'''

# Continue statement

''' With the continuue statement we can stop the current iteration of the 
loop, and continue with the next.'''

# for loop example

fruits = ['mango','banana','apple','cherry']

for x in fruits:
    print(x)

# Break statement 

fruits = ['mango','banana','apple','cherry']

for x in fruits:
    print(x)
    if x == 'banana':
        break

# continue statement 

fruits = ['mango','banana','apple','cherry']

for x in fruits:
    print(x)
    if x == 'banana':
        continue
    print(x)

# Nested for loop

adj = ['red','big','tasty']
fruits = ['apple','banana','cherry']
nos = ['10','20','30']

for i in adj:
    for x in fruits:
        for y in nos:
            print(i,x,y)
