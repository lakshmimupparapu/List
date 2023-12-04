#string in expanded form#

# i/p : 12, o/p : 0 + 0 + 10 + 2
num=int(input("enter the number:"))
i=0
a=num
while i<num:
    r=num%1000
    m=r%100
    n=m%10
    i=i+1
print("'",num-r,"+",r-m,"+",m-n,"+",n,"'")
