x=int(input())
a=list(map(int,input().split()))
n=[]
for i in a:
    if i not in n and a.count(i)==1:
        n.append(i)
if n==[]:
    print("-1")
else:
    print(*n)
