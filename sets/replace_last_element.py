num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
# Write your code here
n = int(input())
m = tuple([n])
s = []
for i in num_list:
    a = i[:-1] + m
    s.append(a)
print(s)
