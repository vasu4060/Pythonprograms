num1 = int(input("enter a number : "))

num2 = 0
num3=0

while num1>0:
    num2=num1%10
    num3=num3*10+num2
    num1=num1//10
   
print(num3)
