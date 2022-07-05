n=int(input())
b=str(n)
c=0
for i in b:
    if b.count(i)==1:
        c+=1
if len(b)==c:
    print("Unique Number")
else:
    print("Not Unique Number")
    