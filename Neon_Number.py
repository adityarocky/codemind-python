m=int(input())
s=0
i=m*m
while i>0:
    r=i%10
    i=i//10
    s+=r
if s==m:
    print("Neon Number")
else:
    print("Not Neon Number")