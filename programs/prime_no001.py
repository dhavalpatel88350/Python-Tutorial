num=int(input("Enter Number::"))
if  num >1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            print(i,"time",num//i,"is",num)
            break
    else:
        print("This Is Prime Number.")
else:
    print("This is not A prime Number.")