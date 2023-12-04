#Square of numbers#
##i/p :9119  o/p::811181
n=int(input("Enter the number:"))
i=0
a=str(n)
while i<len(a):
    print(int(a[i])**2,end="")
    i=i+1
    