n=int(input("Enter value"))
a=2
p=0
while(n>a):
    if(n%a ==0):
        p=1
    break
a=a+1
if(p==1):
    print("it is not a prime number")
else:
    print("it is a prime number")

    
