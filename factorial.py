num = int(input("Enter a number:"))

def for_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
        
    print(f"Factorial of {n} using for loop :",fact)

for_factorial(num)


def while_factorial(n):
    fact = 1
    var = n
    while var > 1:
        fact *= var
        var -= 1
    print(f"factorial of {n} using while loop:{fact}")

while_factorial(num)


def recursion_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursion_factorial(n-1)


print(f"factorial of {num} using recursion:{recursion_factorial(num)}")
