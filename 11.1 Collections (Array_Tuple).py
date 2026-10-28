# Tuples

''' ---> Tuple - Tuple is a collection which is ordered and unchageable. Allows Duplicate members. '''

# Access Tuple items

tuple1 = ('Apple','banana','cherry')
print(tuple1)

print(tuple1[1])

# Check if item exist

if 'Apple' in tuple1:
    print("yes")
else:
    print("no")

# Update tuple

'''Tuples are unchangeable, we can't change,add and remove items once it is created 
but you can change it using list '''

y = list (tuple1)
y[1]='orange'
x = tuple(y)
print(x)

#Join two tuples

tuple1=('apple','banana','cherry')
tuple2=('mange','grape','lemon')
tuple3=tuple1 + tuple2
print(tuple3)

