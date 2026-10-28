'''Instead of writing many if else statement we
can use the match statement
This statement selects 1 of many code blocks to 
be executed'''

day = 20
match day:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunda y')
    case _:
        print('Looking forward to the weekend')


# Default value
''' Use the _ character as the last case value if you want
 a cold block to to execute when they are no other matches'''