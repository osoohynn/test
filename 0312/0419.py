'''n = int(input())

for i in range(1, n+1):
    for j in range(i):
        print(']'*(n-j), end="")
    print()'''



'''num = 1
for i in range(1,5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()'''

'''n = int(input())
num = n

for i in range(n):
    for j in range(i):
        print(' ', end="")
    for j in range(n-i):
        print(num-j, end="")
    num-=1
    print()
'''
'''n = int(input())

for i in range(n//2+1):
    for j in range(i):
        print(' ', end="")
    for j in range(n-i-i):
        print('*', end="")
    for j in range(i):
        print(' ', end="")
    print()'''

'''n= int(input())

for j in range(n):
    print('*', end="")
print()
for j in range(n-2):
    print('*'+' '*(n-2)+'*', end="")
    print()
for j in range(n):
    print('*', end="")'''

'''n = int(input())

for i in range(n):
    for j in range(n-i-1):
        print(' ', end="")
    print('*'*n, end="")
    print()'''

n = int(input())

for i in range(n):
    for j in range(n-i-1):
        print('@', end="")
    print('*', end="")
    for j in range(i):
        print('@@', end="")
    print('*', end="")
    print()

for i in range(n-1, -1, -1):
    for j in range(n-i-1):
        print('@', end="")
    print('*', end="")
    for j in range(i):
        print('@@', end="")
    print('*', end="")
    print()

