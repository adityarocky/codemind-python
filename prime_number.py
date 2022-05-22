x=int(input())
s=0
for i in range(2,x//2):
    if x%i==0:
        s+=1
if s==2:
    print("not a prime")
else:
    print("prime")
