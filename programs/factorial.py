num =int(input("Enter NO::"))
factorial = 1
i=1

# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
while i<=num:

   factorial = factorial*i
   # i=i+1
   print("The factorial of",i,num,"is",factorial)