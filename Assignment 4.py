def check_even_odd(x):
    for i in x:
        if i % 2 == 0:
            print(i,"is even")
        else:
            print(i,"is odd")
check_even_odd([1,2,3,4,5,6,7,8,9,10])