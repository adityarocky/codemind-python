x=int(input())
a=list(map(int,input().split()))
s=0
o=0
for i in range(len(a)):
    if i%2==0:
        s+=a[i]
    else:
        o+=a[i]
if s-o==0:
    print('YES')
else:
    print('NO')
        