def check_armstrong (number):
  sum = 0
  
  n = len(str(number))
  
sum += (num%10)**n 
sum+= number%10**n
number//= 10
