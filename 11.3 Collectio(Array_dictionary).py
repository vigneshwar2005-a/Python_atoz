#Dictionary 

'''It is used to data value in key value pairs
It is ordered, changeable, and do not allow duplicate keys'''

a = {'brand':'Ford','model':'Mustang','Year':2026}
# Here the brand model and year is key values
print(a)

# Duplicate keys not allowed
a = {'brand':'Ford','model':'Mustang','Year':2026, 'Year':2007}
print(a)

# duplicate values are allowed

a = {'brand':'Ford','model':'Mustang','Year':2026, 'Year2':2026}
print(a)

# Get keys

x=a.keys()
print(x)

# Get values

y=a.values()
print(y)

# Get items

z=a.items()
print(z)

# Adding items

thisdic = {'brand':'Ford','model':'Mustang','Year':2026}
thisdic['color']='Red'
print(thisdic)

