a=5
for row in range(a):
    for col in range(a):
        if row==0 or row==4 :
            print('#',end=' ')
        elif col==1 or col==4:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print(' ')