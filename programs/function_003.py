def student():
    n=int(input("Enter Student Number::"))
    o=studentname(n)
    return o
def studentname(n):
    i=1
    b=[]
    
    while i<=n:
        name=input("Enter Student Name::")
        sub=int(input("How many Subject::"))
        b.append(name)
        
        i=i+1
        w = subject(sub)
        print(w)

    return b

def subject(sub):
    k=[]
    for i in range(sub):
        m=int(input("marks::"))
        k.append(m)
    return k

obj=student()
print(obj)