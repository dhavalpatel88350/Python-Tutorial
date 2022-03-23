a=int(input("Enter Number:"))
b=int(input("Enter Number:"))
v=int(input("Enter Number:"))

choice=input("Enter Choice Number:")

if choice == '+':
    print("Addition is:",(a+b))
elif choice =='-':
    print("Subtraction is:",(a-b)-v)
elif choice =='*':
    print("Multiplication is:",(a*b))
elif choice =='/':
    print("Division is",a/b)
elif choice =='%':
    f=a+b
    k=f*v/100
    print(k+f)
elif choice =='**':
    print(a**b)
elif choice =='//':
    print(a//b)
else:
    print("Enter Valid Number")