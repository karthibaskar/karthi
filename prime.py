numbr = 11
  

if numbr> 1: 
      
   
   for i in range(2, numbr//2): 
         
  
       if (numbr % i) == 0: 
           print(numbr, "is not a prime number") 
           break
   else: 
       print(numbr, "is a prime number") 
  
else: 
   print(numb, "is not a prime number") 
