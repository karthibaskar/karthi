numb = 11
  

if numb> 1: 
      
   # Iterate from 2 to n / 2  
   for i in range(2, numb//2): 
         
  
       if (numb % i) == 0: 
           print(numb, "is not a prime number") 
           break
   else: 
       print(numb, "is a prime number") 
  
else: 
   print(numb, "is not a prime number") 
