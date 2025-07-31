
num = int(input("enter num:"))
if num <=1:
    print("not a prime num")
else:
    is_prime = True 
    for i in range(2,num):
        if num % i == 0:
            is_prime=False
            break
    if is_prime:
            print(num,"is a prime num")
    else:    
            print(num,"is not a prime num")


while True:
    num = int(input("enter number2:"))
    
    if num <= 1:
       print("Not a prime number")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, "is a prime number")
        else:
            print(num, "is not a prime number") 
def generate_fibonacci(n):
    a , b=0,1
    print ("fibonacci series:")
    for _ in range(n):
        print(a,end=" ")
        a,b =b,a+b
terms = int(input("enter the number of fibonaci terms to generate:"))
if terms <= 0:
    print("please enter a positive integer ")
else:
        generate_fibonacci(terms)

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: Factorial of the input number.

    Raises:
    ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Main program
try:
    number = int(input("Enter a non-negative integer: "))
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
except ValueError as e:
    print("Error:", e)
