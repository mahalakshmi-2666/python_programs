num = int(input("Enter a number:"))
temp = num
digits = len(str(num))
sum = 0
for digit in str(num):
    sum = sum + int(digit)**digits
if sum == num:
    print("Armstrong number")
else:
    print("Not a armstrong number")    

