a=5
for row in range(a):
    for col in range(a):
        if row==4:
            print('#',end=' ')
        elif col==0:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print(' ')
