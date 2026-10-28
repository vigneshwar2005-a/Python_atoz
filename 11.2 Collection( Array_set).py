# Set

'''> Set - Set is a collection which is unordered, unchageable and unindexed. No Duplicate members.'''

set1={'apple','banana','mango'}
print(set1)

'''Once a set is created we cannot change its items but we can add new items using add method'''

set1.add('orange')
print(set1)

# add Sets

'''To add items from another set into the current set use the update method'''

set1={'apple','banana','mango'}
tropical={'lemon','pineapple','melon'}
set1.update(tropical)
print(set1)

# Remove items

set1.remove('apple')
print(set1)

# Join set

'''  union() and update() Joins all items from different sets
intersection() keeps only the duplicates
difference() Keep the items from the 1st set that are not in the other set (removes the duplicates)
symetric difference() keeps all items except the duplicates '''

set5={'apple','banana','cherry'}
set6={'google','microsoft','apple'}
set5.update(set6)
print(set5)


set7=set5.union(set6)
print(set7)

# Intersection - keeps only the duplicates

a={'apple','banana','mango'}
b={'apple','mango'}
c=a.intersection(b)
print(c)

d=a.difference(b)
print(d)

# Symetric difference

e=a.symmetric_difference(b)
print(e)

