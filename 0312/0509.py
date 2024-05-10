'''d = []
score = 0
cnt = 0
for i in range(5):
    score = 0
    d.append(list(map(int, input().split())))
    for j in range(4):
        score += d[i][j]
    if score//4 >=80:
        print('pass')
        cnt += 1
    else:
        print('fail')

print(f"합격자는 {cnt}명")'''

# d = [[],[],[],[],[]]

# for i in range(5):
#     print(1, end=" ")
#     d[i].append(1)
#     for j in range(i):
#         y = d[i][j-1]+d[i][j]
#         d[i].append(y)
#         print(y, end=" ")
#     print()
# print(d)

'''n = int(input())

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
    print()'''