# Function

'''A function is a block of code which only runs when it is called.
We can pass data, known as parameters, into a function.
A function can return data as a result '''

# Creating a function using def keyword

def myfunction():
    print("Hello python")
myfunction()

# Number of arguments

def function1(fname,lname):
    print(fname,lname)
function1('aaa','bbb')

# Passing a list as an arguement 

def function2(food):
    for x in food:
        print(x)
fruits = ['apple','mango','banana']
function2(fruits)


for x in range(1,10,1):
    print(x)

# Return values

def function3(X):
    return 5 * X
print(function3(3))
print(function3(25))

