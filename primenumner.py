num1 = int(input("Enter a Number : "))

for i in range(2,num1):
    if(num1%i==0):
        print("not a prime")
        break
    else:
        print("prime number")
        break
