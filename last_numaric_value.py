# difference between element (n+1th-nth)#
##[1, 1, 1, 1, 1, 1, 1, 1, 1]
# a=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# for i in range(len(a)-1):
#     n=a[i+1]-a[i]
#     b.append(n)
# print(b)


##[2, 2, 2]
x=[2,4,6,8]
y=[]
for i in range(len(x)-1):
    n=x[i+1]-x[i]
    y.append(n)
print(y)