a, b, c = map(int, input().split('.'))
age = 0

if b<=8 and c<=9:
    age = 2024-a
else:
    age = 2024-a-1

print(age)