n=int(input())
su=0
tem=n
while n>0:
    r=n%10
    n=n//10
    su+=r
if tem%su==0:
    print(True)
else:
    print(False)