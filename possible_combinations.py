# possible combinations these digits
## 1 2 3
## 1 3 2
## 2 1 3
## 2 3 1
## 3 1 2
## 3 2 1

# a=[1,2,3]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             if(a[i]!=a[j] and a[j]!=a[k] and a[k]!=a[i]):
#                 print(a[i],a[j],a[k])
#             k=k+1
#         j=j+1
#     i=i+1



## 0 9 5
## 0 5 9
## 9 0 5
## 9 5 0
## 5 0 9
## 5 9 0

n=[0,9,5]
i=0
while i<len(n):
    j=0
    while j<len(n):
        k=0
        while k<len(n):
            if (n[i]!=n[j] and n[j]!=n[k] and n[k]!=n[i]):
                print(n[i],n[j],n[k])
            k=k+1
        j=j+1
    i=i+1