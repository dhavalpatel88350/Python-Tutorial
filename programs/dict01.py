# a={'a':3,'b':6,'c':7}
a=['a','b','c']
b=[3,4,5]
d={}

# c=dict(zip(a,b))
for i in range(len(a)):
  d[a[i]]=b[i]
print(d)



