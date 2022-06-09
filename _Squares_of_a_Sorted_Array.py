n=int(input())
x=list(map(int,input().split()))
x.sort()
y=[]
for i in x:
    c=i*i
    y.append(c)
y.sort()
print(*y)