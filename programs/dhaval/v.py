n=10
for row in range(n):
    for col in range(n):
        if ((row + col == n - 1 and row < n / 2) or(row == col and row < n / 2)):
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print(' ')
