# Iteration and the creation of sublists #

## [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]] 
list=[1,2,3,4,5,6]
i=0
n=[]
while i<len(list)-1:
    c=[list[i],list[i+1]]
    n.append(c)
    i=i+1
print(n)
