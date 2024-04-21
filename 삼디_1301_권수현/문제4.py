a, b  = map(int, input().split())
e = ''
k = ''

if a == 100:
    e = '만점입니다!'
elif a >= 90:
    e = 'A'
elif a>=80:
    e = 'B'
elif a >= 70:
    e = 'C'
elif a>= 60:
    e = 'D'
else:
    e = 'E'

if b == 100:
    k = '만점입니다!'
elif b >= 90:
    k = 'A'
elif b >=80:
    k = 'B'
elif b >= 70:
    k = 'C'
elif b >= 60:
    k = 'D'
else:
    k = 'E'

print(f"엄성민 : {e}")
print(f"권지용 : {k}")