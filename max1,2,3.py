list=[12,34,23,8,58,89,123,98]
i=0
max=0
smax=0
tmax=0
while i<len(list):
    if list[i]>max:
        max=list[i]
    i=i+1
j=0
while j<len(list):
    if list[j]>smax and list[j]!=max:
        smax=list[j]
    j=j+1
k=0
while k<len(list):
    if list[k]>tmax and list[k]!=smax and list[k]!=max:
        tmax=list[k]
    k=k+1
print(max,smax,tmax)