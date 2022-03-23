def one():
    print("1.+")
    print("2.-")
    print("3.*")
    print("4./")
    choice=int(input("Enter your choice::"))
    a=int(input("enter a First no::"))
    b=int(input("enter a Second no::"))
    w=two(choice,a,b)
    return w

    
    
def two(choice,a,b):
    if choice==1:
        z=a+b
    elif choice==2:
        z=a-b
    elif choice==3:
        z=a*b
    elif choice==4:
        z=a/b
    else:
        print("invalid Input::")
    return z
obj=one()
print(obj)