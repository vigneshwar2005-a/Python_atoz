# Collections(Array)

'''There are 4 types of collection

> List - List is a collection which is ordered and chageable. Allows Duplicate members.
 
> Tuple - Tuple is a collection which is ordered and unchageable. Allows Duplicate members. 

> Set - Set is a collection which is unordered, unchageable and unindexed. No Duplicate members.

> Dictionary - Dictionary is a collection which is ordered and chageable. No Duplicate members.'''

# List

list1=['ac',34,True,40.2,24,34,'ad','ac','ac']
for i in list1:
    print(i)

# Access items 

print(list1[2])

# Negative index: Mean starting from the end (-1 refers to the last item)

print(list1[-1])
print(list1[-2])

# Range of index

print(list1[2:8:2])

# Change  item value 

list=['apple','banana','cherry']
list[1]='mango'
print(list)

# Insert items

list.insert(2,'lemon')
print(list)

# Append items

list.append('orange')
print(list)

# Extend list

tropical = ['mango','pineapple','papaya']
list.extend(tropical)
print(list)

# Remove items

list.remove('mango')
print(list)

# sort list

list.sort()
print(list)

list.sort(reverse=True)
print(list)

# Reverse list

list.reverse()
print(list)

# Copy list

mylist=list.copy()
print(mylist)

list.