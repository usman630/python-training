n = input().split()
m = []
for i in n:
    m = m +[int(i)]
a = set(m)
if len(a)==1:
    print("True")
else:
    b = list(a)
    c = sorted(b)
    print(c)
 


------------
input
45 45 45 45 
output=True
-----------
40 20 40 20 40
output=[20,40]
