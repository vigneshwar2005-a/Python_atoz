# String Handling

'''String in python are arrays of bytes representing unicode characters
It does not have character datatype.
A single chr is simply a string with a length of 1.'''

a = 'Welcome'
print(a[1]) # 1 is defined as the index

# Looping thru a string 

for x in 'welcome':
    print(x)

# String length

a = 'welcome'
print(len(a))


# Slicing strings ( we can return a range of chr using slice syntax)

b = 'Hello python'
c = 'HELLO PYTHON'
print(b[2:5])
print(b.upper())
print(c.lower())
print(b.replace('H','j'))

# Split()

''' This method splits into substring
 if it finds instances of the seperator'''

x = 'Hello, Python Java'
print(x.split(' '))

# Remove whitespaces 

'''strip() Method removes any whitespace from the
 begining or the end'''

y = ' Hello python '
print(y.strip())

# String concatenation

l = 'welcome to '
m = 'python'
c = l + m 
print (c)

# Count

text = 'programming'
print (text.count('m'))

# Find

print(text.find('g'))

# Capitalize

print(text.capitalize())

# Casefold

text2 ='PROGRAMMING'
print(text2.casefold())

# center

text3 = 'excel'
center_text=text3.center(11)
print(center_text)

center_text1=text3.center(15,'*')
print(center_text1)


str= 'Programming'
print(str.find('z'))

print(str.index('i'))



str