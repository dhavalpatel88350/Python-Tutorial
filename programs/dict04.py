a={'a':300,'b':100,'c':150,'d':60}
b=[]
for i,j in a.items():
    if j>100:
        b.append(i)
print("User less than 100 are::",b)