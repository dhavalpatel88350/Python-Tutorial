var1=input("Which categary:")
var2 = int(input("How many products:"))
e=10
g=20
f=30
total=0
i=1
if var1 == 'electonic':
    while i<=var2:
        name = int(input("product price:"))
        total=total+name
        i=i+1
        

    # print(name)
    k =total+total*e/100
    print("Total Bill :",name,k)
  



if var1 == 'furniture':
    while i <= var2:
        name = int(input("product price:"))
        total = total+name
        i = i+1

    # print(name)
    k = total+total*g/100
    print("Total Bill :", k)
if var1 == 'glossary':
    while i <= var2:
        name = int(input("product price:"))
        total = total+name
        i = i+1
    # print(name)
    k = total+total*f/100
    print("Total Bill :", k)
