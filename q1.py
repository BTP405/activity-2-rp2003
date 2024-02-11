def getPrimeNumbers(n):
  
def getPrimeNumbers(n):
    divisibleList=[];       #list is easier to use and
    #primeList=[];
    if(n==1):
        print("It is a Prime number");
    elif(n>1):
        #prime number is something that is divisible my any other number other that itself 
        for i in range(2,n+1):
            if(n%i==0):
                #print("It is a not a prime number");  
                divisibleList.append(i); 
            else:    #is prime
               primeList.append(i); 
               
    print(divisibleList);
    #print(primeList);
getPrimeNumbers(10);
