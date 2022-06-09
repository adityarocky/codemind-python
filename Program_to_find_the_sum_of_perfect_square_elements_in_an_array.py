import math
x=int(input())
s=0
a=list(map(int,input().split()))
n=[]
for i in a:
    c=int(math.sqrt(i))
    if c*c==i:
        n.append(i)
for i in n:
    s+=i
print(s)    