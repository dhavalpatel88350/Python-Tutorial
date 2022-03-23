a = ['hello','how', 'are', '',None]

for i in a:
    if i in a:
        continue
    else:
        print(i)