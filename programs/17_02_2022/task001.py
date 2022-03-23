import re
numuser=input("Enter Number::")
pattern ="[6-9][0-9]{9}"
if(re.search(pattern,numuser)): 
     
    emailuser=input("Enter email::")
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
    if(re.search(regex,emailuser)):   
        print("Valid Email:: Email is:",emailuser)  
        print ("Valid Number:: Number is",numuser)  
        
    else:   
        print("Invalid Email")   
  
else :
    print ("Invalid Number") 
  

  
