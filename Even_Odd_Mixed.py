n=int(input())
e=0
o=0
res=0
while n>0:
    r=n%10
    res=res*10+r
    if res%2==0:
        e+=1
    else:
        o+=1
    n=n//10
if(e==0):
    print('Odd')
elif(o==0):
    print('Even')
else:
    print('Mixed')
