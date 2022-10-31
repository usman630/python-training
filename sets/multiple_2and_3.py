n = int(input())
s = []
c = []
for i in range(1,n+1):
    a = 2 * i
    s = s + [a]
#print(s)
for j in range(1,n+1):
    b = 3 * j
    c = c +[b]
#print(c)
s = set(s)
c = set(c)
x = s - c
y = s ^ c
w = list(x)
z = list(y)
u = sorted(w)
v = sorted(z)
print(u)
print(v)
    
