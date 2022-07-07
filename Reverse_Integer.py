a=int(input())
rev=0
t=a
if a<0:
    a=a*-1
    while a>0:
        r=a%10
        rev=rev*10+r
        a=a//10
else:
    while(a>0):
        r=a%10
        rev=rev*10+r
        a=a//10
if t<0:
    print(-rev)
else:
    print(rev)
        