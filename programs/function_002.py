var=input("Enter categary::")
def evanodd():
        a=int(input("enter number:"))
        if a%2==0:
            q=("even")
        else:
            q=("odd")
        return q
def palindrome():
    
        number = int(input("Enter the integer number: "))
        t = number
        # Initiate value to null
        revs_number = 0

        # reverse the integer number using the while loop

        while (number > 0):
            # Logic
            remainder = number % 10
            # print(remainder)
            revs_number = (revs_number * 10) + remainder
            # print(revs_number)
            number = number // 10
        # Display the result
        if(t == revs_number):
            w=("palindrome")
        else:
            w=("not palindrome")
            return w
def factorial():
        num = int(input("Enter NO::"))
        factorial = 1
        if num < 0:
            k=("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
            k=("The factorial of 0 is 1")
        else:
            for i in range(1, num+1):
                factorial = factorial*i
            k=("The factorial of", num, "is", factorial)
            return k      
def armstrong():
    num = int(input("Enter a number: "))
    sum = 0
    temp = num
    while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10
    if num == sum:
        rp=("Armstrong number is ", num)
    else:
        rp=(num, "is not an Armstrong number")
    return rp

if var == 'evanodd':
    
    print(evanodd())
if var == 'palindrome':
     
    print(palindrome())
if var =='factorial':
   
    print(factorial())
if var == 'armstrong':
    print(armstrong())
