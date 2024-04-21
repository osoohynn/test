'''for i in range(1, 5):
    for j in range(1, 5):
        print(f"({i}, {j})", end=" ")
    print()'''

'''
for i in range(1, 3):
    for j in range(1, 3):
        print('* '*i*j)'''

'''X = int(input())
N = int(input())
sum = 0
for i in range(N):
    a, b = map(int, input().split())
    sum = sum + a*b

if sum == X:
    print('Yes')
else:
    print('No')'''


'''for i in range(1, 11):
    print('@@'*i)'''

'''a, b = map(int, input().split())

for i in range(b):
    print('|'*a)'''

sum = 0
a, b, c = map(int, input().split())
for i in range(a+1):
    if i%b == c:
        sum += i
print(sum)
