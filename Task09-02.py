n = int(input())
def isPrime(n):
  if (n == 2) or (n == 3):
      print(n,"is  prime ")
      
  for i in range(2,n-1):
    
    if n % i == 0 :
      print(n,"is not prime ")
      break
  else:
   print(n,"is  prime ")
    

isPrime(n)


def primes(n):
  for j in range(2,n):  
  
    
   for i in range(2 , j):
        if j % i == 0 and i!= j :
          break
            
        
   else:
     print(j)

    

primes(n)
