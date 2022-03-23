a=int(input("enter number:"))

if a==3 or a==5 or a==7:
    print("this is prime number")

elif a%2==0 or a%3==0 or a%5==0 or a%7==0:
    print("this is NOT prime number")
else:
    print("this is  prime number")
