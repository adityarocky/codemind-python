n=int(input())
s=0
while n>0:
    r=n%10
    n=n//10
    s+=1
if s<10 or r==0:
    print("Invalid")
else:
    print("Valid")
    