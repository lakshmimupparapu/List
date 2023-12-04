## First n numbers of prime numbers ##
## Enter a number:8
## 2 3 5 7 11 13 17 19 

n=int(input("Enter a number:"))
i=1
s=0
while i>0:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==2:
        s=s+1
        print(i,end=" ")
    if s==n:
        break
    i=i+1 

