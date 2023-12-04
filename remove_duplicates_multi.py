# 
## 90
list=[6,1,3,5,6,3,1]
i=0
c=[]
p=1
while i<len(list):
    if list[i] not in c:
        c.append(list[i])
        p=p*list[i]
    i=i+1
print(p)
