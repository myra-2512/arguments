def total_calc(bill,tip_perc):
    total=bill*(1+0.01*tip_perc)
    total=round(total,2)
    print(f"Please pay ${total}")

# specify only the bill amount
#default value of tip percentage is used

total_calc(150,20)


# Activity 2

def cube(num):
    return num*num*num

def by_three(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return False
    
print(by_three(9))
print(by_three(4))

#Activity 3 

def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print("Factorial of 0 is", factorial(0))
print("Factorial of 1 is", factorial(1))
print("Factorial of 2 is", factorial(2))
print("Factorial of 3 is", factorial(3))
print("Factorial of 4 is", factorial(4))
print("Factorial of 5 is", factorial(5))
print("Factorial of 10 is", factorial(10))