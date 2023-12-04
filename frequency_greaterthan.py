# extract all elements whose frequency is greater than k #
##[4, 3]
list=[4,6,4,3,3,4,3,4,3,8]
k=3
a=[]
for i in list:
    n=list.count(i)
    if n>k:
        if i not in a:
            a.append(i)
print(a)


##[4,3,6]
# list=[4,6,4,3,3,4,3,4,6,6]
# k=2
# a=[]
# for i in list:
#     n=list.count(i)
#     if n>k:
#         if i not in a:
#             a.append(i)
# print(a)