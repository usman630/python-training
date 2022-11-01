n = int(input())
s = set()
c = []
for i in range(1,n+1):
    a = input().split()
    b = set(a)
    if len(s) == 0:
        s = b
    else:
        s = s & b
for i in s:
    i = int(i)
    c.append(i)
print(sorted(c))


-------------
input:
3
6 5 7 8 9
1 2 3 4 5
5 67 34 23 

-----------
