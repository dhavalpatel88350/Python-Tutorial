a=[None,'abc','bcd','','qwe',3,4,6,0]
b=[]
for i in a:
    if i == '' or i == None:
        continue
    b.append(i)
print(b)