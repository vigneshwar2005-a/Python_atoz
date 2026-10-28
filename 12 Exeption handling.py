# Exception handling 

''' It is a mechanism used to manage run time error, Known as exceptions,
That disturb the normal flow of the program'''

# Try block 

''' This block contains the code that might potentially raise an exception '''

# Except block 

''' If an exception occurs within the try block, The program jumos to the corresponding except block '''

# Else Block ( Optional ) 

''' This block Executes only if no exceptions are raised within the try block '''

# Finally block ( Optional )

''' This block always excutes, Whether an exception occured or not'''

# Raise Statement

''' It is used to explicitly trigger an exception '''


try :
    a = 100
    b = 0
    c = a/b 
    print (c)
    nos = [10,20,30,40,50]
    print (nos[2])
except Exception as e:
    print(e)

# Else block

else:
    print('division successful')

finally:
    print('sucessful')


# Raise
 
''' We can choose to throw an exception if an condition ocours
To throw ( Raise ) use the Raise keyword '''

x = -1
if x < 0:
    raise Exception('sorry no number below zero')