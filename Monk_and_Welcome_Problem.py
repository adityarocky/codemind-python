x=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(x):
    d=a[i]+b[i]
    c.append(d)
print(*c)    