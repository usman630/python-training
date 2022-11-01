a=input().split(",")
b=int(input())
s=[]
pair_set=set()
for i in a:
    i=int(i)
    s=s+[i]
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        if s[i]+s[j]==b:
            pair=(s[i],s[j])
            pair_1=tuple(sorted(pair))
            pair_set.add(pair_1)

for i in sorted(pair_set):
    print(i)
    
--------
#input
5,3,7,9,5
12
------
    
