n=int(input("Enter a number : "))
f=1
if(n>1):
    for i in range(2,(n//2)+1):
        if(n%i==0):
            f=0
            break
else:
    f=0
if(f==1):
    print("The %d is a prime number."%(n))
else:
    print("The %d is not a prime number."%(n))