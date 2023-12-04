# if we enter number one of the present in list item/elements [1,1,2,3,4,5,1,2] 1 o expect that number remaing elements will print  n=[1,1,2,3,4,5,1,2] #

##[2, 3, 4, 5, 2]
# n=[1,1,2,3,4,5,1,2]
# a=int(input("Enter the number:"))
# i=0
# b=[]
# while i<len(n):
#     if n[i]!=a:
#         b.append(n[i])
#     i=i+1
# print(b)



## i/p : 7 , o/p : [5,6,8,9,10]
x=[5,6,7,8,9,10]
n=int(input("Enter th enumber:"))
k=[]
for i in x:
    if i !=n:
        k.append(i)
print(k)