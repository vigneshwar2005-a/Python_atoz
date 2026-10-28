# Arithmetic operator

a = 100
b = 200

c = a + b
print(c)

d = a - b
print(d)

e = a / b
print(e)

f = a * b
print(f)

g = a % b
print(g)

# Assignment operator

a = 19
b = 21

b += a
c -= a
d *= a

print (b)
print (c)
print (d)

# Membership operator

my_list= [10,20,30,40,50]
print('membership operator')
print (20 in my_list)

my_list= [10,20,30,40,50]
print('membership operator')
print (60 not in my_list)

# Identity operator 

a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = a 
print('Identity operator')
print(a is c)
print(a is b)
print(a is not c)
print(a is not b)