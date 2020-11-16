num1 =int(input("Enter first number"))
num2 =int(input("enter second number"))

print("Before Swapping, first number "+str(num1)+", second Number is "+str(num2)+" ")

num1 = num1+num2
num2 = num1-num2
num1 = num1-num2
print("After Swapping, first number "+str(num1)+", second Number is "+str(num2)+" ")
