num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   #print(digit)
   sum += digit ** 3
   #print(sum)
   temp //= 10
   #print(temp)
   
if num == sum:
   print("Armstrong number is ",num)
else:
   print(num,"is not an Armstrong number")