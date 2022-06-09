x=int(input())
a=list(map(int,input().split()))
es=0
os=0
for i in a:
    if i%2==0:
        es+=1
    else:
        os+=1
print(es,os)        