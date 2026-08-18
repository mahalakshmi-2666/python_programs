n=int(input("Enter a number:"))
i = 2
factors = [ ]
while n > 1:
    if n % i == 0:
        factors.append(i)
        n = n // i
    else:
        i=i+1

factors_dict = {f"{x}^{factors.count(x)}" for x in factors}
count = 0
for f in factors_dict:
    print(f,end="") 
    count += 1
    if count < len(factors_dict):
        print(" x ",end ="")

   