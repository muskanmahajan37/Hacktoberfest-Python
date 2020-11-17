n=int(input("enter value"))
factorial= 1
if(n<0):
    print("Negative no cannot be choosen")
elif(n==0):
    print("factorial of zero is one")
else:
  while (n>0):
    factorial= factorial*n
    n=n-1
    print("factorial of number is :", factorial)
    
