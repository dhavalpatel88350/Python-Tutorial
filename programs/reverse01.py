number = int(input("Enter the integer number: "))  
t=number
# Initiate value to null  
revs_number = 0  
  
# reverse the integer number using the while loop  
def revs():  
    while (number > 0):  
        # Logic  
        remainder = number % 10  
        # print(remainder)
        revs_number = (revs_number * 10) + remainder  
        # print(revs_number)
        number = number // 10   
    print("The reverse number is : {}".format(revs_number))  
z=revs()
print(z)