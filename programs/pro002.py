student=int(input("how many Students:"))
i=1
n=[]
s=[]
while i<=student:
    name=input("Enter student Name:")
    n.append(name)
    sub=int(input("Enter subject No:"))
    i=i+1
    j=1
    total=0
    while j<=sub:
        m=int(input("enter marks:"))
        s.append(m)
        total=total+m
        j=j+1
    print(total)
print(n)
print(s)