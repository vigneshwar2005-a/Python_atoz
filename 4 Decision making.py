# If-Else

x = 20 
y = 100

if(x>y):
    print('x is greater than y')
else:
    print('y is greater than x')

# Else-if ladder

temp = 70

if(temp>=30):
    print('very hot')
elif(temp<=25) and (temp>=20):
    print('hot')
elif(temp<=10) and (temp>=1):
    print('very cold')

# Nested if

a = 41

if(a>100):
    print('above 10')
    if(a>100):
        print('above 20')
    else:
        print('not above 100')
else:
    print('invalid data')




