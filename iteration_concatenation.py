# Iteration and concatenation process #

## ['12', '34', '56', '78']
list=['1','2','3','4','5','6','7','8']
i=0
c=[]
while i<len(list):
    c.append((list[i])+(list[i+1]))
    i=i+2
print(c)
