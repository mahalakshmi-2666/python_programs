
num = int(input("Enter a number:"))
print("factors using for loop:",end="")
for i in range(1,num+1):
    if (num % i == 0):
        print(i,end=", ")


print("\nfactors using while loop:",end="")
i=1
while i <=num:
    if num % i == 0:
        print(i,end=",")
    i=i+1

