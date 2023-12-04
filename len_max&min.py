#length of maximum and minimum

##3 [13, 15, 17]
##1 [0]
# n=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=0
# max=n[i]
# min=n[i]
# while i<len(n):
#     if n[i]>max:
#         max=n[i]
#     if n[i]<min:
#         min=n[i]
#     i=i+1
# print(len(max),max)
# print(len (min),min)


n=[[0],[1,3],[5,7],[9,11],[13,15,17]]
max=1
min=1
for i in range(len(n)):
    length=len(n[i])
    if length>max:
        max=length
    if length<min:
        min=length
print(max,n[max+1])
print(min,n[min-1])