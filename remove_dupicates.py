list=[1,2,2,5,8,4,4,8]
i=0
a=[]
c=5
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
        c=c+1
    i=i+1
print(a)
