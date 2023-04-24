## This python script will calculate the factorial of any given number entered.
## To use this script, kindly call the factorial function with the given number who's factorial you want to evaluate

def factorial(n):
    if n<2:
        return 1
    return n*factorial(n-1)

print(factorial(5))


    
    

    
    