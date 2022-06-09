n=int(input())
a=list(map(int,input().split()))
x=[]
for i in a:
    if i not in x and a.count(i)==1:
        x.append(i)
if x==[]:
    print("-1")
else:
    print(max(x))