def con_list(l):
    s = []
    for i in l:
        s.append(int(i))
    return s
    
l = input().split(",")
ro = int(input())
n = con_list(l)
ro = ro%(len(n))
fp = n[0:ro]
sp = n[ro:]
sp.extend(fp)
print(sp)

-----------
#input
1,2,3,4,5
2
-----------
