n = int(input())

for i in range(n):
    l = [0 for i in range(i+1)]
for i in range(n):
    l[i] = [1 for i in range(i+1)]


for i in range(n):
    for j in range(i):
        if j == 0:
            l[i][j] = 1
        else:
            l[i][j] = l[i-1][j-1]+l[i-1][j]

for i in l:
    for j in i:
        print(j, end=" ")
    print()