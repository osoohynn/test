'''def plus(a, b):
    return a+b
def minus(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b

a,b=map(int, input().split())
print(plus(a, b))
print(minus(a, b))
print(mul(a, b))
print(div(a, b))'''

'''def calculator(a, b) :
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return [sum, sub], mul, div

reslist = calculator(10, 2)
print(reslist)'''

'''def division(a, b) :
	if b == 0 :
		return '안돼'
	else :
		res = a / b
		
	print("division")
	return res

result = division(10, 3)
print(result)

result = division(10, 0)
print(result)'''

# print('o'.join('frreg'))

'''n = int(input())

for i in range(4):
    print(input().upper())'''

# print(input().index())

'''a = ['12,300', '800', '3,000', '400']
b = []

for i in a:
    b.append(int(i.replace(',','')))
print(sum(b))'''

'''a = list(map(int, input().split()))
mx = a.pop(a.index(max(a)))
if mx<sum(a):
    print(sum(a)+mx)
else:
    mx = sum(a)-1
    print(sum(a)+mx)'''

'''a = list(map(int, input().split()))
d = [i for i in a if i>0]
print(len(d))'''

'''cnt = 0
n = int(input())
d = list(map(int, input().split()))
for i in range(n-1):
    if d[i]!=2:
        if d[i]+1 == d[i+1]:
            cnt+= 1
        else:
            continue
    else:
        if d[i+1] == 0:
            cnt+=1
        else:
            continue

if d[n-2]!=2:
    if d[n-2]+1 == d[n-1]:
        cnt+= 1
else:
    if d[n-1] == 0:
        cnt+=1
print(cnt)'''

'''d = {'A+':4.3, 'A0':4.0, 'A-':3.7,'B+': 3.3, 'B0': 3.0, 'B-': 2.7, 'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 'D0': 1.0, 'D-': 0.7}

print(d[input()])'''

'''d = [350.34, 230.90, 190.55, 125.30, 180.90]

t = int(input())

for i in range(t):
    a = list(map(int, input().split()))
    o = []
    for j in range(len(a)):
        o.append(a[j]*d[j])
    print(f"${sum(o):.2f}")'''

cnt = 0
def plusNum(n ,cnt):
    cnt += 1
    return n + num

num = 3
print(plusNum(17, cnt))
print(cnt)