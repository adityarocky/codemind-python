n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    d=len(str(i))
    if d%2==0:
        c+=1
print(c)        