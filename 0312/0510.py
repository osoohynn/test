'''l = []
for i in range(4):
    l.append(list(map(int, input().split())))

s = 0'''

'''for i in range(4):
    r = 0
    for j in range(2):
        r += l[i][j]
        s += l[i][j]
    print(r//2, end=" ")
print()

for i in range(2):
    sp = 0
    for j in range(4):
        sp += l[j][i]
    print(sp//4, end=" ")
print()

print(s//8)'''

'''n, m = map(int, input().split())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))


total = []

for i in range(n):
    r = sum(d[i])
    total.append(r/m)

for i in range(m):
    r = 0
    for j in range(n):
        r += d[j][i]
    total.append(r/n)


print(sum(total))
'''
n, m = map(int, input().split())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))

for i in range(n):
    r = 0
    for j in range(m):
        print(d[i][j], end=" ")
    print()