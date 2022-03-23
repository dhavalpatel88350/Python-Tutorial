a=['abc','bcd','fgh','rhs','vs','zz','aaa','djj','ff','yy','bv']
i=0
b=[]
c=[]
d=[]
# for i in range(len(a)-1):
#     # print(ord(a[i][0]))
#     if ord(a[i][0]) < ord(a[i+1][0]):
#         b.append(a[i])
    
#     else:
#      c.append(a[i]) 
    
#     if ord(a[i][0]) <= ord(a[i+1][0]):
#         d.append(a[i])
     
# print(b)
# print(c)
# print(d)
for i in range(len(a)-1):
    if ord(a[i][0])<=ord(a[i+1][0]):
        print("yes")
    else:
        b.append(a[i+1])
print(b)

        