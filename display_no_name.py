# display the number name #

##'zero', 'one', 'two', 'three',
##   0      1      2       3
l=[]
digits = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
n=int(input("Enter the no:"))
while n>0:
    r=n%10
    l.append(digits[r])
    n=n//10
l.reverse()
for dig in l:
    print(dig,end=' ')
