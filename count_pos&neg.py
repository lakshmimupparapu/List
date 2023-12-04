# count positive and negative numbers in a list #

## pos=2
## neg=0 
list=[2,-7,5,-64,-14]
pos=0
neg=0
for i in list:
    if i>0:
        pos=pos+1
print("pos"+"="+str(pos))
print("neg"+"="+str(neg))
