num1 = int(input("enter a number : "))
num2=1
while num1>0:
    print(num1, end=" ")
    num2=num1*num2
    num1=num1-1


print()
print(num2,end=" ")
