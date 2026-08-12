# Prime Number Checker

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number.")
else:
    is_prime = True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a Prime number.")
    else:
        print(num, "is NOT a Prime number.")

# Print all prime numbers up to num
print("\nPrime numbers up to", num, ":")

for n in range(2, num + 1):
    is_prime = True
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(n, end=", ")