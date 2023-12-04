# remove duplicate in a list
##[1, 2, 3]
list=[1,2,3,1,2,2]
n=[]
for i in list:
    if i not in n:
        n.append(i)
print(n)