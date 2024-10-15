"""n = int(input())
if n<0 and n%2==0:
    print('A')
elif n<0 and n%2!=0:
    print('B')
elif n>0 and n%2==0:
    print('C')
else:
    print('D')
"""
"""
n = int(input())
if n>=90:
    print('A')
elif n>=70:
    print('B')
elif n>=40:
    print("C")
else:
    print("D")"""

'''n = input()

if n=="A":
    print("best!!!")
elif n=="B":
    print("good!!")
elif n=="C":
    print("run!")
elif n=="D":
    print("slowly~")
else:
    print("what?")'''


'''n = int(input())
if n//3==1:
    print("spring")
elif n//3==2:
    print('summer')
elif n//3==3:
    print('fall')
else:
    print('winter')'''

'''n = 1
while n!=0:
    n=int(input())
    if n!=0:
        print(n)
    else:
        break
'''

'''n = int(input())

while n!=0 :
  n = n-1
  print(n)'''


'''c = int(input())
t = 0

while t<=c:
    print(t)
    t+=1'''

'''n = int(input())
for i in range(n+1) :
  print(i)'''


'''n = int(input())
s=0

for i in range(1, n+1):
    if i%2 ==0:
        s+=i

print(s)'''


'''n=1

while n!="q":
   n = input()
   print(n)'''

'''n = int(input())
i=0
t=0

while n>t:
    i+=1
    t+=i
    
print(i)'''


'''n, m = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, m+1):
        print(i,j)'''

'''n = input()

if n == "A":
    n = 10
elif n == "B":
    n = 11
elif n =="c":
    n = 12
elif n == "D":
    n = 13
elif n =="E":
    n = 14
elif n == "F":
    n = 15

for i in range(1, 16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
'''

'''n = int(input())

for i in range(1, n+1):
    if i%10==3 or i%10==6 or i%10==9:
        print("X", end=" ")
    else:
        print(i, end=" ")'''

'''r , g, b = map(int, input().split())
c = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
            c+=1
print(c)'''

'''a = int(input())

for i in range(1,10):
    print(f"{a} * {i} = {a*i}")'''
'''
T = int(input())

for i in range(T):
    a , b = map(int, input().split())
    print(a+b)'''

'''n = int(input())
sum = 0

for i in range(n):
    i += 1
    sum += i
    
print(sum)'''

'''N = int(input())
i = N

print()'''

'''n = int(input())

print(n*n-n)'''

'''age = 17
print(id(age))
age = 18
print(id(age))
grup = [18, 19, 20]
print(id(grup))
grup[2] = 23
print(id(grup))'''

'''a = int(input())

for i in range(1,a+1):
    s = a-i
    print(' '*s+'*'*i)'''

'''a = int(input())
b = input()

c = int(b[2])
d = int(b[1])
e = int(b[0])
f = int(b)

print(a*c)
print(a*d)
print(a*e)
print(a*f)'''

'''w, h, b = map(int, input().split())
s = w*h*b/8/1024/1024
print(f"{s:.2f} MB")'''

'''n = int(input())
count = 1
sum = 0

while True:
    sum += count
    count += 1
    if sum >= n:
        break
print(sum)    '''

'''n = int(input())
for i in range(1, n+1):
    if i%3==0:
        continue
    print(i, end=" ")'''

'''a, d, n = map(int, input().split())
y=a
for i in range(2, n+1):
    y += d
print(y)'''

'''a, m, d, n = map(int, input().split())
y=a
for i in range(2, n+1):
    y = y*m + d
print(y)'''

'''a, b, c = map(int, input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0:
    d+=1
print(d)
'''

''' = int(input())
a = input().split()'''

'''X = input()
N = input()

X = int(X)
N = int(N)
sum = 0

for i in range(N):
    a, b = map(int, input().split())
    sum = sum + a*b

if X == sum:
    print("Yes")
else:
    print("No")'''

'''n = int(input())
a = list(map(int, input().split()))
# print(a)

d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end=" ")'''

'''n = int(input())

a = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    print(a[i], end=" ")'''


'''n = int(input())

a = list(map(int, input().split()))
p = a[0]

for i in range(n):
    if a[i]< p:
        p = a[i]

print(p)'''

'''a=0
b=0

while True:
    a, b = map(int, input().split())
    
    # if a==0 & b==0:
    #     break
    print(a+b)'''


'''N = int(input())
a = list(map(int, input().split()))
v = int(input())
sum = 0

for i in range(N):
    if v==a[i]:
        sum += 1

print(sum)'''

'''N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i]<X:
        print(A[i], end=" ")'''


'''N = int(input())
A = list(map(int, input().split()))
min, max = A[0], A[0]

for i in range(N):
    if A[i]<min:
        min = A[i]

for i in range(N):
    if A[i]>max:
        max = A[i]

print(min, max)'''

'''a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
a6 = int(input())
a7 = int(input())
a8 = int(input())
a9 = int(input())

l = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
p = l[0]

for i in range(9):
    if l[i]>p:
        p=l[i]

print(p)
print(l.index(p)+1)'''

'''a, b = map(int, input().split())

print(a+b)'''

'''print(int(input())-543)'''

'''A, B, C = map(int, input().split())'''

'''print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)'''

'''print("""\    /\\
 )  ( ')
(  /  )
 \(__)|
""")'''

# print('''|\_/|
# |q p|   /}
# ( 0 )"""\\
# |"^"`    |
# ||_/=\\\__|
# ''')
'''
N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    print(a+b)'''

'''a = list(range(8))
print(a)'''

'''d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

n = int(input())
for i in range(n):
    x, y = input().split()
    d[int(x)][int(y)] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=" ")
    print()'''


'''d = []

for i in range(20):
    d.append([])

    for j in range(20):
        d[i].append(0)

for i in range(19):
    a = input().split()
    for j in range(19):
        d[i+1][j+1] = int(a[j])

n = int(input())

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)

    for j in range(1,20):
        
        if d[j][y]==0:
            d[j][y]=1
        else :
            d[j][y]=0

        if d[x][j]==0:
            d[x][j]=1
        else :
            d[x][j]=0

for i in range(1,20):
    for j in range(1, 20):
        print(d[i][j], end=" ")
    print()'''

'''for i in range(5):
    print(i)
    
    if i > 2:
        print("aaa")
    print(i)
print(1)'''

'''
h, w = map(int, input().split())
n = int(input())


list = []

for i in range(h+1):
    list.append([])
    for j in range(w+1):
        list[i].append(0)

for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d==0:
            list[x][y+j]=1
        else :
            list[x+j][y]=1

for i in range(1,h+1):
    for j in range(1,w+1):
        print(list[i][j], end=" ")
    print()'''
'''
n1, n2 = map(int, input().split())

l = list(range(n2, n1-1, -1))

print(l)'''

'''a, b = map(int, input().split())

if a>b:
    print(">")
elif a<b:
    print("<")
else :
    print("==")'''


# score = int(input())

# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else:
#     print("F")


'''y = int(input())

if y%4==0 and y%100!=0:
    print("1")
elif y%400==0:
    print("1")
else:
    print("0")'''

'''x = int(input())
y = int(input())

if x>0 and y>0:
    print("1")
if x>0 and y<0:
    print("4")
if x<0 and y>0:
    print("2")
if x<0 and y<0:
    print("3")'''

'''h, m = map(int, input().split())

if m-45<0:
    m=m+60-45
    if h-1<0:
        h=23
    else:
        h -= 1
    print(h,m)
else:
    m = m -45
    print(h,m)'''

'''h, m = map(int, input().split())
t = int(input())

u = (m + t)//60

if u >= 1:
    if h+u < 24:
        h += u
    else:
        h += u - 24     
    m = (m+t)-u*60
else:
    m = m+t

print(h, m)'''


''''a, b, c = map(int, input().split())

max = 0

if a == b == c:
    print(10000+a*1000)

if a == b and a!=c:
    print(1000+100*a)
if a == c and a!=b:
    print(1000+100*a)
if c == b and a!=c:
    print(1000+100*c)

if a != b and a != c and b!=c:
    if a>b:
        if a>c:
            max = a
        else:
            max = c
    else:
        if b>c:
            max = b
        else:
            max = c
    print(100*max)'''

'''n = int(input())

lc = 0

for i in range(n//4):
    lc += 1

print('long '*lc+'int')'''

'''import sys

n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)'''

'''T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")'''

'''while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break'''
'''
N, M = map(int, input().split())
basket = []

for i in range(N):
    basket.append(0)

for i in range(M):
    a, b, c = map(int, input().split())
    basket[a-1:b] = [c]*(b-a+1)

for i in range(N):
    print(basket[i], end=" ")'''

# d=[]
# for i in range(20) :
#   d.append([])
#   for j in range(20) : 
#     d[i].append(0)

# for i in range(19) :
#   a = input().split()
#   for j in range(19) :
#     d[i+1][j+1] = int(a[j])

# n = int(input())
# for i in range(n) :
#   x,y=input().split()
#   x=int(x)
#   y=int(y)
#   for j in range(1, 20) :
#     if d[j][y]==0 :
#       d[j][y]=1
#     else :
#       d[j][y]=0

#     if d[x][j]==0 :
#       d[x][j]=1
#     else :
#       d[x][j]=0

# for i in range(1, 20) :
#   for j in range(1, 20) :
#     print(d[i][j], end=' ')
#   print()

'''d = []
for i in range(12):
    d.append([])
    for j in range(12):
        d[i].append(0)

for i in range(10):
    a = input().split()
    for j in range(10):
        d[i+1][j+1] = int(a[j])


# for i in range(5):
#     if d[i][i+1] == 0 or d[i][i+1] == 2:
#         d[i][i+1] = 9
#     else :
#         d[i+1][i] = 9

x = 2
y = 2

while True:
    if d[x][y]==0:
        d[x][y]=9
    elif d[x][y]==2:
        d[x][y]=9
        break

    if (d[x][y+1]==1 and d[x+1][y]==1) or (x==9 and y==9):
        break

    if d[x][y+1]!=1:
        y += 1
    elif d[x+1][y]!=1:
        x+=1


for i in range(1, 11) :
  for j in range(1, 11) :
    print(d[i][j], end=' ')
  print()'''


# N, M = map(int, input().split())

'''d = list(range(1,N+1))


for i in range(M):
    a, b = map(int,input().split())
    d[a-1], d[b-1] = d[b-1], d[a-1]

for i in range(N):
    print(d[i], end=" ")'''

'''a = []
b = []

for i in range(28):
    n = int(input())
    a.append(n)


# print(a)

for i in range(1,31):
    
    if i not in a:
        b.append(i)

print(min(b))
print(max(b))

# print(a)'''

# 백준 3052 나머지

'''a = []
b = []

for i in range(10):
    n = int(input())
    a.append(n)

for i in range(10):
    b.append(a[i]%42)

sum = 0

for i in range(10):
    sum = b.count(b[i])

print(sum)'''
'''
N, M = map(int, input().split())

d = list(range(N))

for i in range(1,M+1):
    a, b =  map(int, input().split())

    d[a], d[b] = d[b], d[a]
    d[a+i], d[b-i] = d[b-i], d[a+i]

print(d)'''

'''s = input()
# n = int(input())

print(len(s))'''

'''n = int(input())

for i in range(n):
    g = input()
    print(g[0]+g[-1])'''

'''print(ord(input()))'''

'''n = int(input())
num = input()

sum = 0

for i in range(n):
    sum = sum + int(num[i])

print(sum)'''

'''a, b = map(int, input().split())
print(f"{(a*b/2):.1f}")'''

'''a = int(input())
print(a*24)'''

'''a, b, c = map(int, input().split())
print(f"{(a+b+c)/3:.2f}")'''

'''a, b = map(int, input().split())
print(a%b)'''

'''a = int(input())

print(f"{a*9/5+32:.3f}")'''

'''a = input()'''

'''a, b = map(int, input().split())

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a//b}")
print(f"{a} % {b} = {a%b}")'''

'''a = float(input())

if a == 1 or a== 3 or a==5 or a==7:
    print('oh my god')
else:
    print('enjoy')'''


'''a, b, c = map(int, input().split())
if a<b:
    if a<c:
        print(a)
    else:
        print(c)
else:
    if b<c:
        print(b)
    else:
        print(c)'''

'''a, b = map(int, input().split())

if a%2==1 and b%2==1:
    print("홀수+홀수=짝수")
elif a%2==1 and b%2==0:
    print("홀수+짝수=홀수")
elif a%2==0 and b%2==1:
    print("짝수+홀수=홀수")
elif a%2==0 and b%2==0:
    print("짝수+짝수=짝수")'''

'''a, b, c = map(int, input().split())

if a<=170 or b<=170 or c<=170 :
    print("CRASH")
else:
    print("PASS")'''

'''a, b, c = map(int, input().split())

if a>b>c or c>b>a:
    print(b)
elif a>c>b or b>c>a:
    print(c)
else:
    print(a)'''

'''a, b = input().split()
if int(b)==1 or int(b)==2:
    y = 1900+int(a[0:2])
else:
    y = 2000+int(a[0:2])

print(2012-y+1)'''

'''a = int(input())

if 2013-a <2000:
    print(2013-a-1900, 1)
else:
    print(2013-a-2000, 3)'''

'''a, b, c = map(int, input().split())

if b < 10 and c>=100:
    print(f"{a}0{b}{c}")
elif b < 10 and c>=10:
    print(f"{a}0{b}0{c}")
elif b < 10 and c<10:
    print(f"{a}0{b}00{c}")
elif b > 10 and c>=100:
    print(f"{a}{b}{c}")
elif b >10 and c>=10:
    print(f"{a}{b}0{c}")
else:
    print(f"{a}{b}00{c}")'''

'''a, b, c = map(int, input().split())

d = [a,b,c]
d.sort()

for i in range(3):
    print(d[i], end=" ")'''

'''a = int(input())

print("*"*a)'''

'''a, b = map(int, input().split())

if a%2==1:
    d = list(range(a, b+1, 2))
    for i in range(3):
        print(d[i], end=" ")
else:
    d = list(range(a+1, b+1, 2))
    for i in range(3):
        print(d[i], end=" ")'''

'''n, m = map(int, input().split())
f = 0

if n%3==0:
    f = n
elif (n+1)%3==0:
    f = n+1
else:
    f = n+2

sum = 0
for i in range(f,m+1,3):
    sum+=i
print(sum)'''

'''c = int(input())
s = list(map(int, input().split()))
sum = 0

for i in range(c):
    if s[i]%2==1:
        sum+=1
print(sum)'''

'''a, b, c, n = map(int, input().split())
p = a

for i in range(n-1):
    p = p*b+c

print(p)'''
'''
a, b = map(int, input().split())

sm = sum(range(a+1,b))
print(sm)'''

'''print("""강한친구 대한육군
강한친구 대한육군
""")'''

'''n= int(input())

for i in range(n , 0, -1):
    print(i)'''

'''b = list(input().split())

print(len(b))'''

'''while True:
    try:
        a, b = input().split()
        print(int(a)*b)
    except EOFError :
        break
'''

'''a, b = input().split()
# [::-1] : 역순

a = a[::-1]
b = b[::-1]

if int(a)>int(b):
    print(a)
else:
    print(b)'''

'''a = int(input())

for i in range(a, 0, -1):
    print(f"{'*'*i:>{a}}")'''

'''a = int(input())
b = int(input())

print(a+b)'''
'''
n = int(input())
d = list(map(int, input().split()))
sum = d[0]

for i in range(n):
    sum += d[i]

print(sum*2)'''

'''n = int(input())
d = []

for i in range(n):
    j = int(input())
    d.append(j)

d.sort()

for i in range(n):
    print(d[i])'''

'''print("""         ,r'"7
r`-_   ,'  ,/
 \. ". L_r'
   `~\/
      |
      |
""")'''

'''a = int(input())
N = a*2-1

for i in range(1, N,2):
    print(f"{'*'*i:^{a}}")
# print('*'*N)
for i in range(a, 0, -2):
    print(f"{'*'*i:^{a}}")'''

'''a = int(input())

print('*'*a)

for i in range(a-2):
    print(f"*{' '*(a-2)}*")
print('*'*a)'''

'''a = input()

print("welcome! "+a)'''

'''a, b = map(int, input().split())
print(f'{a/b:.1f}')
print(a//b)
print(a**b)'''

'''a = int(input())

for i in range(a):
    print('hello')'''

'''a = input()

print(len(a))'''

'''n = int(input())

for i in range(n):
    a = input()
    print(a[::-1])'''

'''a, b = map(int, input().split())

if a>b:
    print(b,a)
else:
    print(a,b)'''

'''n = int(input())

if n%3==0:
    print(1)
else:
    print(0)'''

'''a = int(input())

for i in range(1, a+1):
    print(' '*(a-i)+('*'*(i*2-1)))
for i in range(a-1, 0, -1):
    print(' '*(a-i)+('*'*(i*2-1)))'''

'''a, b = map(int, input().split())

print(a+b)'''

'''d = {1:400, 2:340, 3:170, 4:100, 5:70}
a, b = map(int,input().split())

if d[a]+d[b]>500:
    print('angry')
else:
    print('no angry')'''

'''a, b = map(int, input().split())

if b%a==0:
    print(f"{a}*{b//a}={b}")
elif a%b==0:
    print(f"{b}*{a//b}={a}")
else:
    print('none')'''

'''length = list(map(int, input().split()))
max = 0
l1 = 0
l2 = 0
a = length[0]
b = length[1]
c = length[2]

if a> b:
    if a > c:
        max = a
        l1 = b
        l2 = c
    else:
        max = c
        l1 = a
        l2 = b
else:
    if b > c:
        max = b
        l1 = a
        l2 = c
    else:
        max = c
        l1 = a
        l2 = b   

if l1+l2>max:
    print('yes')
else:
    print('no') '''

'''a, b, c = map(int, input().split())

if a+b>c:

    if a==b and b==c:
        print("정삼각형")
    elif a==b or a==c or b==c:
        print("이등변삼각형")
    elif a**2+b**2==c**2:
        print("직각삼각형")
    else:
        print("삼각형")
else:
    print("삼각형아님")'''

'''a, b = map(ord, input().split())

d = []

for i in range(a, b+1):
    d.append(chr(i))

for i in d:
    print(i, end=' ')'''

'''a, b = map(int, input().split())

if a> b:
    for i in range(a, b+1):
        print(i, end=" ")
else:
    for i in range(b, a+1):
        print(i, end=" ")'''

'''n = int(input())

for i in range(1, n+1):
    if n%i==0:
        print(i,end=" ")'''

'''n = int(input())

mul = 1

for i in range(1,n+1):
    mul *= i

print(mul)'''

'''n = int(input())
for i in range(1,n+1):
    print('*'*i)
for i in range(n-1,0,-1):
    print('*'*i)'''



'''for i in range(1,a-1):
    print(' '*(a-i-2)+('*'*(i*2-1)))'''

'''a = int(input())

for i in range(1,a+1):
    for j in range(1, a+1):
        print(j*i, end=" ")
    print()'''

'''a = int(input())

sum= 0

for i in range(1,a+1):
    if a%i==0:
        sum+=i
print(sum)'''

'''while True:

    print(input())'''

'''print("""       _.-;;-._
'-..-'|   ||   |
'-..-'|_.-;;-._|
'-..-'|   ||   |
'-..-'|_.-''-._|
""")'''

'''n = int(input())
car_l = list(input().split())
sum = 0

for i in range(5):
    if int(car_l[i][-1]) == n:
        sum += 1
print(sum)'''

'''R1, S = map(int, input().split())

R2 = S*2-R1
print(R2)'''

'''print("""(___)
(o o)____/
 @@      \\
  \ ____,/
  //   //
 ^^   ^^
""")'''

'''a = int(input())
b = int(input())

print(a+b)
print(a-b)
print(a*b)'''

'''print("""  ___  ___  ___
  | |__| |__| |
  |           |
   \_________/
    \_______/
     |     |
     |     |
     |     |
     |     |
     |_____|
  __/       \__
 /             \\
/_______________\\
""")'''

'''a,b = map(int, input().split())

print(abs(a-b))'''

'''a = list(map(int,input().split()))

for i in range(5):
    a[i] = a[i]**2

print(sum(a)%10)'''

'''a = input()
print(a.swapcase())'''

'''a = list(map(int, input().split()))

print(1-a[0], 1-a[1], 2-a[2], 2-a[3], 2-a[4], 8-a[5])'''

'''while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a > b:
        print('Yes')
    else:
        print('No')'''

'''a, b =map(int, input().split())
print(a*b)'''

'''a = input()
print(f""":fan::fan::fan:
:fan::{a}::fan:
:fan::fan::fan:
""")'''
'''
a = input()
print(a.upper())'''

'''a = int(input())

if a==1:
    print("YONSEI")
else:
    print("Leading the Way to the Future")'''

'''a = int(input())

print(a//5+1)'''

'''a, b = map(int, input().split())

print(a+b)'''

"""a, b = map(int, input().split())

'''if a == b:
    print(1)
else:
    print(0)'''

print((a+b)*(a-b))"""

'''a = int(input())

print(a-1946)'''

'''su = 0

for i in range(5):
    a = int(input())
    if a<40:
        a=40
    su += a

print(su//5)'''
# 49 12
# print(225-18+87+12)

'''a = []

for i in range(10):
    b = int(input())
    a.append(b%42)

print(len(set(a)))'''

'''N, M = map(int, input().split())

lis = list(range(1, N+1))

for i in range(M):
    a, b = map(int, input().split())
    lis2 = lis[a-1:b]
    lis2.reverse()
    lis[a-1:b] = lis2
    
for i in range(N):
    print(lis[i], end=" ")'''

'''N = int(input())
lis  = list(map(int, input().split()))
M = max(lis)

for i in range(N):
    lis[i] = lis[i]/M*100

print(sum(lis)/N)'''

'''S = input()
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(26):

    print(S.find(alp[i]), end=" ")
'''

'''T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    for i in range(len(S)):
        s = S[i]*R
        print(s,end="")
    print()'''

'''# A, B, C = 2, 2, 2 
# D, E, F = 3, 3, 3
# G, H, I = 4, 4, 4
# J, K, L = 5, 5, 5
# M, N, O = 6, 6, 6
# P, Q, R, S = 7, 7, 7, 7
# T, U, V = 8, 8, 8
# W, X, Y, Z = 9, 9, 9, 9

S = input()
s = []

for i in range(len(S)):

    # A, B, C = 2, 2, 2 
    # D, E, F = 3, 3, 3
    # G, H, I = 4, 4, 4
    # J, K, L = 5, 5, 5
    # M, N, O = 6, 6, 6
    # P, Q, R, S = 7, 7, 7, 7
    # T, U, V = 8, 8, 8
    # W, X, Y, Z = 9, 9, 9, 9
    s.append(S[i])

A, B, C = 2, 2, 2
D, E, F = 3, 3, 3
G, H, I = 4, 4, 4
J, K, L = 5, 5, 5
M, N, O = 6, 6, 6
P, Q, R, S = 7, 7, 7, 7
T, U, V = 8, 8, 8
W, X, Y, Z = 9, 9, 9, 9
print(s)'''

'''while True:
    try:
        s = input()
        print(s)
    except EOFError:
        break
    if s == 'p':
        break'''

'''S = input()
s = 0


for i in range(len(S)):
    if S[i]==S[-i-1]:
        s =1
    else:
        s = 0
        break

print(s)'''

'''s = list(map(str, input()))
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
res = 0

for i in s:
    for j in dial:
        if i in j:
            res += dial.index(j)+3

print(res)'''

# print(225-18+101)

'''n, m = map(int, input().split())
print(n//m)
print(n%m)'''

'''while True:
    S = input()
    if S == '#':
        break
    print(S.count('a')+S.count('e')+S.count('i')+S.count('o')+S.count('u')+S.count('A')+S.count('E')+S.count('I')+S.count('O')+S.count('U'))
'''
'''s =[]
for i in range(5):
    s.append(int(input()))

print(sum(s))'''

'''s = int(input())
r = []
for i in range(s):
    r.append(input().lower())

for i in r:
    print(i)'''

'''l1 = int(input())
l2 = int(input())
l3 = int(input())

if l1+l2+l3 == 180:
    if l1 ==60 and l2 == 60 and l3 == 60:
        print('Equilateral')
    elif l1 == l2 or l1 == l3 or l2 ==l3:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')'''

'''m = int(input())
d = int(input())

if m == 2 and d == 18:
    print('Special')

elif m < 2 or (m == 2 and d<18):
    print('Before')

else:
    print('After')'''

'''sco = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0': 2.0, 'D+':1.5, 'D0':1.0, 'F':0.0, 'P':0.0}

c1 = 0
c2 = 0

for i in range(20):
    Sn, Ss, Sg = input().split()
    
    if Sg == 'P':
        continue
    c1 += float(Ss)*sco[Sg]
    c2 += float(Ss)

print(c1/c2)'''

'''for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")
    print()'''

'''n = int(input())

dl =[]

for i in range(n):
    d = int(input())
    dl.append(d)

mx = dl[0]
mn = dl[0]

for i in range(n):

    if dl[i] >= mx:
        mx = dl[i]
    elif dl[i] <= mn:
        mn = dl[i]

print(f'최대값은 {mx}, 최소값은 {mn}')'''

'''count = 0
sm = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n%3!=0 and n%5!=0:
        count+=1
        sm += n

print(f"{count}개, 총 합은 {sm}")'''

'''word  = list(input())


ct = 0

print(word.count('a'))

'''

'''n = int(input())

mx = 0
mn = 1002

while n>0:
	a = int(input())
	if mx < a:
		mx = a
	if mn>a:
		mn = a
	
	n-=1
	
print(f"최대값은 {max}, 최소값은 {min}")'''

'''for i in range(10, 0, -1):
    print(i, end=",")
'''

'''S = list(input())

for i in range(len(S)//2):
    S[i], S[-1] = S[-1], S[i]

for i in S:
    print(i, end="")'''

'''n, m = map(int, input().split(','))
cnt = 0
for i in range(n, m):
    print(f"{i}+", end="")
    cnt += i
print(f"{m}= {cnt+m}")'''

'''for i in range(1, 6, 2):
	print(' '*((5-i)//2)+'*'*i+' '*((5-i)//2))'''

'''S = list(input())

for i in range(len(S)//2):
    S[i] = S[-1]

for i in S:
    print(i, end="")'''

'''for i in range(2, 6):
    for j in range(1, 6):
        print(i*j, end=" ")
    print()'''

'''a = input()

for i in range(len(a)-1, -1, -1):
    print(a[i], end="")'''

'''alist = [10, 20, 30, 40]
for a in range(len(alist)):
	print(a)
    '''

'''T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(str(a**b)[-1])'''

'''while True:
    a, b, c = input().split()
    if a=='#' and b=='0' and c=='0':
        break
    elif int(b) > 17 or int(c) >=80:
        print(a+' Senior')
    else:
        print(a+' Junior')'''

'''a= list(map(int, input().split()))
a.sort()
for i in a:
    print(i, end=" ")'''
    
'''x, y, w, h = map(int, input().split())

print(min(x, y, w-x, h-y))'''

'''N = int(input())
F = int(input())


N = N-int(str(N)[-2:-1])
N += N%F
print(N)'''

'''T = int(input())
ball = 1

for i in range(T):
    a, b = map(int, input().split())
    if a == ball:
        ball = b
    elif b == ball:
        ball = a

print(ball)'''

'''d = []
p = 0

for i in range(10):
    a, b = map(int,input().split())
    d.append(p-a+b)
    p += -a+b
print(max(d))'''

'''p= 0
d=[]
N = int(input())'''
'''
for i in range(N):
    a, b, c = map(int, input().split())

    if a == b == c:
        d.append(10000+a*1000)

    if a == b and a!=c:
        d.append(1000+100*a)
    if a == c and a!=b:
        d.append(1000+100*a)
    if c == b and a!=c:
        d.append(1000+100*c)

    if a != b and a != c and b!=c:
        p = max([a,b,c])
        d.append(100*p)
print(max(d))'''

'''N = int(input())

for i in range(1,N+1):
    print('*'*i+' '*(2*N-2*i)+'*'*i)
for i in range(1,N+1):
    print('*'*(N-i)+' '*(2*i)+'*'*(N-i))'''

'''N = int(input())

for i in range(1,N+1):
    for j in range(i):
        print('*', end="")
    print()

for i in range(1,N):
    for j in range(N-i):
        print('*',end="")
    print()'''

'''N = int(input())
for i in range(1,N+1):
    print('*'*N)'''

'''li = ['D', 'C', 'B', 'A', 'E']

for i in range(3):
    a = list(map(int, input().split()))
    print(li[sum(a)])'''

'''N, K =  map(int,input().split())
d = []

for i in range(1,N+1):
    if N%i==0:
        d.append(i)

if K <= len(d):
    print(d[K-1])
else:
    print(0)'''

'''import calendar as c

weekday_d = {0:'월', 1:'화', 2:'수', 3:'목', 4:'금', 5:'토', 6:'일'}
y, m, d = map(int, input().split('.'))
day = c.weekday(y,m,d)

if y == 2024 and 4<= m <= 6:
    print(f"{y}년{m}일{d}일은 {weekday_d[day]}요일 입니다.")
    print('방과후 수업 0')
else:
    print("해당 일은 방과 후 운영기간이 아닙니다.")'''

'''S1 = 0
S2 = 0
S3 = 0
a = 3

n = int(stdin.readline())
for i in range(n):
    k = int(stdin.readline())
    S1 += k


n = int(stdin.readline())
for i in range(n):
    k = int(stdin.readline())
    S2 += k


n = int(stdin.readline())
for i in range(n):
    k = int(stdin.readline())
    S3 += k


# print(S1)
# print(S2)
# print(S3)

if S1>0:
    print('+')
elif S1==0:
    print('0')
else:
    print('-')

if S2>0:
    print('+')
elif S2==0:
    print('0')
else:
    print('-')

if S3>0:
    print('+')
elif S3==0:
    print('0')
else:
    print('-')'''

'''S = input()

sn = len(S)

if 'c=' in S:
    sn -= 1
if 'c-' in S:
    sn -= 1
if 'dz=' in S:
    sn -= 1
if 'd-' in S:
    sn -= 1
if 'lj' in S:
    sn -= 1
if 'nj' in S:
    sn -= 1
if 's=' in S:
    sn -= 1
if 'z=' in S:
    sn -= 1

print(sn)'''
'''
while True:
    n = input()
    if int(n) == 0:
        break

    s = len(n)-1 +2

    for i in range(len(n)):
        if n[i] == '1':
            s += 2
        elif n[i] == '0':
            s += 4
        else:
            s += 3

    print(s)'''

'''wdl = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
w = input()

for i in wdl:
    w = w.replace(i, '8')
print(len(w))'''

'''word = input().upper()
w_l = list(set(word))
c_l = []

for i in w_l:
    count = word.count(i)
    c_l.append(count)

if c_l.count(max(c_l))>=2:
    print('?')
else:
    print(w_l[c_l.index(max(c_l))])'''

'''me = input()
d = input()

if len(me) > len(d):
    print('go')
else:
    print('no')'''

"""print('''NFC West       W   L  T
-----------------------
Seattle        13  3  0
San Francisco  12  4  0
Arizona        10  6  0
St. Louis      7   9  0

NFC North      W   L  T
-----------------------
Green Bay      8   7  1
Chicago        8   8  0
Detroit        7   9  0
Minnesota      5  10  1''')"""

'''import datetime
print(str(datetime.datetime.now())[:10])'''

'''
n = int(input())

if n%5==0:
    print(n//5)
else:
    print(n//5+1)'''

'''a, b = map(int, input().split())
print(b-a, b)'''

'''s = input()

if s == 'n' or s== 'N':
    print('Naver D2')
else:
    print('Naver Whale')'''

'''s = input()
cnt = 0

for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i== 'u':
        cnt += 1
print(cnt)'''

'''while True:
    s = input()
    if s == 'END':
        break
    print(s[::-1])'''
'''a = input()
b = input()
print(a+b)'''

'''money = int(input())
cnt = 0
for i in range(9):
    cnt += int(input())

print(money-cnt)'''

'''n = int(input())

for i in range(n):
    m = int(input())
    print('='*m)'''

'''cnt = 0
jh = input()
n = int(input())

for i in range(n):
    m = input()
    if jh == m:
        cnt += 1

print(cnt)'''

'''print(530000+1920000+149000)'''

'''a, b, c = map(int, input().split())
print(3*(b//a)*c)'''
'''
n = int(input())

for i in range(n):
    a = input()
    if 6<= len(a) <= 9:
        print('yes')
    else:
        print('no')'''

'''a, b = map(int, input().split())
if b == 1 or not(12<=a<=16):
    print(280)
else:
    print(320)'''

'''n = int(input())
d = 1
for i in range(1, n+1):
    d *= i
print(d)'''

'''n, m = map(int, input().split())

if n*100>=m:
    print('Yes')
else:
    print('No')'''

'''s = input()

if s == 'NLCS':
    print('North London Collegiate School')
elif s == 'BHA':
    print('Branksome Hall Asia')
elif s == 'KIS':
    print('Korea International School')
elif s == 'SJA':
    print('St. Johnsbury Academy')'''

'''n, a, b = map(int, input().split())

if n <= b:
    if a>b:
        print('Subway')
    elif a<b:
        print('Bus')
    elif a == b:
        print('Anything')
else:
    print('Bus')'''

'''s = input()

if s == 'M':
    print('MatKor')
elif s == 'W':
    print('WiCys')
elif s == 'C':
    print('CyKor')
elif s == 'A':
    print('AlKor')
elif s == '$':
    print('$clear')'''

'''a, b, c, d, e = map(int, input().split())

print(a*b-c*d*e)'''

'''a, b =map(int,input().split())
print(a*b/2)'''
'''
n = int(input())
for i in range(n):
    a,b,x = map(int, input().split())
    print(a*(x-1))'''

'''b = int(input())
print(b*10//11)'''

'''a, b = map(int, input().split())
y = a * b
q, w, e, r, t = map(int, input().split())
print(q-y, w-y, e-y, r-y, t-y)'''

'''n = int(input())
for i in range(1,n+1):
    a = input()
    print(f"{i}. {a}")'''

'''s,t,d = map(int, input().split())
y = d//(s*2)
print(y*t)'''

'''a, b = map(int, input().split())
c, d = map(int, input().split())

if a+d <= b+c:
    print(a+d)
else:
    print(b+c)'''

'''a, b, c = map(int, input().split())

if a*b/c >= a/b*c:
    print(int(a*b/c))
else:
    print(int(a/b*c))'''

'''s = list(input())
for i in s:
    i = int(i)
s.sort()
s.reverse()
for i in s:
    print(i, end="")'''

'''a = list(map(int, input().split()))
a.sort()
print(a[1])'''

'''t = int(input())
for i in range(t):
    g = int(input())
    if g%2 == 0:
        print('cubelover')
    else:
        print('koosaga')'''

'''n = int(input())
d = 1
for i in range(1, n+1):
    d *= i
for i in range(len(str(d))-1,-1, -1):
    if str(d)[i]!='0':
        print(str(d)[i])
        break'''

'''d = ['Soongsil',"Korea", 'Hanyang']
a = list(map(int, input().split()))
t = d[a.index(min(a))]

if sum(a) >=100 :
    print('OK')
else:
    print(t)'''

'''i = 0
while True:
    a = int(input())
    if a == -1:
        break
    i += a
print(i)'''

'''sm = 0
for i in range(4):
    o = int(input())
    sm += o
print(sm//60)
print(sm%60)'''

'''g = list(map(int, input().split()))
s = list(map(int, input().split()))

if sum(g)>=sum(s):
    print(sum(g))
else:
    print(sum(s))'''

'''a = int(input())
r = input()
b = int(input())

if r == '+':
    print(a+b)
elif r == '*':
    print(a*b)'''

'''while True:
    s = input()
    if s == '***':
        break
    print(s[::-1])'''

'''s = 'Monty Python'

print(s[-4:-1])

evennumbers = [2, 4, 6, 8, 10]
oddnumbers = [1, 3, 5, 7, 9]

numbers = evennumbers + oddnumbers
print(numbers)
print(numbers * 4)'''

'''date = '2024-04-30'

day = date[-2:]
print(day)'''

'''l = [10, 20, 30, 40, 50]

t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    if a == 1:
        l.insert(b, c)
        print(l)
    elif a == 2:
        l.pop(b)
        print(l)'''

'''name = input()
nu1,nu2 = input().split('-')
year = 0
gender = ''

if nu2[0] == '1' or nu2[0] == '2':
    year = 1900+int(nu1[:2])
elif nu2[0] == '3' or nu2[0] == '3':
    year = 2000+int(nu1[:2])

if nu2[0] == '1' or nu2[0] == '3':
    gender = '남자'
elif nu2[0] == '2' or nu2[0] == '4':
    gender = '여자'

print(f"{name[0]} {name[1:]} {year}년
 {nu1[2:4]}월 {nu1[4:6]}일 {gender}")'''


'''date = '2023-03-30'
date = date.split('0')
print(date)'''

'''date = '2023-03-30'
print(date.split('-')[1])'''

'''c, h = input().split('H')
print(int(c[1:])*12+int(h))'''


'''while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)'''

'''a, b, c = map(int, input().split())
if a*b-c>=0:
    print(a*b-c)
else:
    print(0)'''

'''h, m, s = map(int, input().split())
t = int(input())

h += t//3600
m += t//60-t//3600*60
s += t%60

if s>= 60:
    s -= 60
    m += 1
if m >= 60:
    m -= 60
    h += 1
if h >= 24:
    h %= 24

print(h, m, s)'''

'''al = [0]*26

s = input()

for i in s:
    al[ord(i)-97]+=1

for i in al:
    print(i, end=" ")'''

'''sm = 0
sl = []
cl = []
for i in range(4):
    s = int(input())
    sm += s
    sl.append(s)
for i in range(2):
    s = int(input())
    sm += s
    cl.append(s)

print(sm-min(sl)-min(cl))'''

'''a, b = map(int,input().split())

for i in range(a):
    s = list(input())
    s.reverse()

    for i in s:
        print(i, end="")
    print()'''

'''a = list(map(int, input().split()))
b = min(a)+max(a)
a.remove(min(a))
a.remove(max(a))
c = sum(a)
d = [b, c]
print(max(d)-min(d))'''

'''import random as r

a, b = map(int, input().split())
#if a%2==1:
#	a+=1
	
print(r.randrange(a+1, b+1, 2))'''

'''import random as r

a, b = map(int, input().split())
if a%2==1:
	a+=1
	
print(r.randrange(a, b+1, 2))'''

'''T = int(input())
print(T)

for i in range(T):
    a , b = map(int, input().split())
    print(a+b)
    i += 1'''


'''h, b, c, s = map(int, input().split())
s = h*b*c*s/8/1024/1024

print(f"{s:.1f} MB")'''

'''my = list(map(int, input().split()))
std = list(map(int, input().split()))

if my[1]<std[1] or (my[1] == std[1] and my[2] <= std[2]):
    a1 = std[0] - my[0]
else:
    a1 = std[0] - my[0]-1

a2 = std[0] - my[0] +1
a3 = a2 - 1

print(a1)
print(a2)
print(a3)'''

'''n, m ,k = map(int, input().split())

if k>=m:
    mx = k
else:
    mx = m

if n - m <= n-k:
    mx += n - m
else:
    mx += m

print(mx)'''

'''a = int(input())
b = int(input())
print(a*2+b*2*3.141592)'''

'''a, b = map(int, input().split())

if b == 1 or b == 2:
    print('NEWBIE!')
elif b<=a:
    print('OLDBIE!')
else:
    print('TLE!')'''

'''t = int(input())
n = list(map(int, input().split()))
m = 0
y = 0

for i in n:
    y+= (i//30+1)*10
    m+= (i//60+1)*15

if m==y:
    print(f'Y M {y}')
else:
    if m< y:
        print(f'M {m}')
    else:
        print(f'Y {y}')'''

'''city = ["서울", "대전", "대구", "부산"]
sale = [80, 60, 22, 50, 75]

print("인덱스와 데이터의 조합")
for i in enumerate(city) :
    print(i)
		
print("두 리스트이 데이터 조합")
for c, s in zip(city, sale) :
	print(c, "도시 /", s, "매출")'''

'''
a = [1, 2, 3]
d1, d2, d3 = a #리스트의 요소를 변수에 언팩 가능
print(d1, d2, d3)

print([i for i in range(60, 40, -1) if i%3==0])'''

'''city = ["서울", "대전", "대구", "부산"]
sale = [80, 60, 22, 50, 75]

for i in zip(city, sale) :
	print(list(i))
#둘 중 더 짧은 요소를 가진 것만큼 돈다.

print(zip(city, sale)[0])'''

'''a, b = map(int, input().split())
print(a*(b-1)+1)'''

'''d = []

for i in range(5):
    d.append(sum(map(int, input().split())))

print(d.index(max(d))+1, max(d))'''

'''while True:
    a = list(map(int, input().split()))
    if a[0] == a[1] == a[2] == 0:
        break
    if a.pop(a.index(max(a)))**2 == max(a)**2+min(a)**2:
        print('right')
    else:
        print('wrong')'''

    
'''n, m = map(int, input().split())
d1 = []
d2 = []

for i in range(n):
    d1.append(list(map(int, input().split())))
for i in range(n):
    d2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(d1[i][j]+d2[i][j], end=" ")
    print()'''

'''n = int(input())
a, b, c = map(int, input().split())
total = 0
if a<=n:
    total+=a
else:
    total+=n
if b<=n:
    total+=b
else:
    total+=n
if c<=n:
    total+=c
else:
    total+=n
print(total)'''

'''n = int(input())
f=1
for i in range(1,n+1):
    f *= i
print(f//604800)'''

'''n = int(input())
sl = []
for i in range(n):
    sl.append(input())
for i in sl:
    if 'S' in i:
        print(i)'''

''''s,d,i,l,n = map(int,input().split())
if n*4-s-d-i-l>=0:
    print(n*4-s-d-i-l)
else:
    print(0)'''

'''a = int(input())
b = int(input())
c = int(input())
print(a+b-c)
print(int(str(a)+str(b))-c)'''

'''arr = [0 for i in range(3)] #리스트에 3개의 요소 생성

for i in range(3) :
	print("%d번째 행: " %i, end="")
	arr[i] = list(map(int, input().split()))

print("결과확인")
for i in range(3) :
	for j in range(3) :
		print(arr[i][j], end=" ")
	print()'''

'''arr = [] #빈리스트 생성

for i in range(3) :
	print("%d번째 행: " %i, end="")
	arr.append(list(map(int, input().split())))
	
print("결과확인")
for i in range(3) :
    for j in range(3) :
        print(arr[i][j], end=" ")
    print()'''

'''arr = [[0 for j in range(3)] for i in range(3)]
print(arr)

for i in range(3) :
	for j in range(3) :
		arr[i][j] = int(input()) #요소 하나씩 입력
		
print("결과확인")
for i in range(3) :
    for j in range(3) :
        print(arr[i][j], end=" ")
    print()'''
'''
l = []
for i in range(4):
    l.append(list(map(int, input().split())))

for i in range(4):
    sp = 0
    for j in range(2):
        sp += l[j]
    print(sp//4, end=" ")
print()'''

'''for i in range(5):
    l = [[] for i in range(i+1)]
for i in range(5):
	  l[i].append(0)
print(l)

print(eval(input()))'''

'''s = input()
if len(s)==4:
    a = int(s[0:2])
    b = int(s[2:4])
elif len(s)==2:
    a = int(s[0])
    b = int(s[1])
elif len(s)==3:
    if int(s[1])==0:
        a=10
        b=int(s[-1])
    elif int(s[-1])==0:
        a = int(s[0])
        b = 10
print(a+b)'''

'''while True:
    a, b = map(int, input().split())
    if a==b==0:
        break
    if b%a==0:
        print('factor')
    elif a%b==0:
        print('multiple')
    else:
        print('neither')'''

'''t = int(input())
for i in range(t):
    t2 = int(input())
    a = list(map(int, input().split()))
    print(sum(a))'''

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

'''cnt = 0
n = int(input())
for i in range(31):
    if n == 2**i:
        print(1)
        cnt = 1
if cnt == 0:
    print(0)'''

'''while True:
    try:
        s = input()
        print(s)
    except EOFError:
        break'''

'''cnt = 0
def plusNum(n ,cnt):
    cnt += 1
    return n + num

num = 3
print(plusNum(17, cnt))
print(cnt)'''

'''cnt = 0
def plusNum(n ,cnt):
    cnt = cnt
    cnt += 1
    print(cnt)
    return n + num

num = 3
print(plusNum(17, cnt))
print(cnt)'''

'''cnt = []
def plusNum(n):
    cnt.append(1)
    return n + num

num = 3
print(plusNum(17))
print(plusNum(17))
print(plusNum(17))
print(sum(cnt))'''

'''cnt = 0
def plusNum(n):
    global cnt
    cnt += 1
    return n + num

num = 3
print(plusNum(17))
print(plusNum(17))
print(plusNum(17))
print(cnt)'''

'''cnt = 0
def plusNum(n):
    global cnt
    cnt += 1
    return n + num'''

'''m = 3
print(plusNum(17))
print(plusNum(17))
print(plusNum(17))
print(cnt)

cnt = 0
def plusNum(n ,cnt):
    cnt += 1
    return n + num

num = 3
print(plusNum(17, cnt))
print(plusNum(17, cnt))
print(plusNum(17, cnt))
print(cnt)'''

'''a, b, c = map(int, input().split())
d = b**2+c**2

for i in range(a):
    o = int(input())
    if o**2<=d:
        print('DA')
    else:
        print('NE')'''

# a<b<c

'''al = list(map(int, input().split()))
s = input()
al.sort()
for i in s:
    if i == 'A':
        print(al[0], end=" ")
    elif i == 'B':
        print(al[1], end=" ")
    else:
        print(al[2], end=" ")'''

'''t = int(input())
p = 0
for i in range(t):
    s = input()
    for i in s:
        cnt = 0
        if s.count(i) == 1:
            cnt += 1
        if cnt == 1:
            p += 1
    print(cnt)
print(p)'''

'''k = int(input())
for i in range(k):
    m = int(input())
    n = int(input())
    for j in range(n):
        q,p = map(int, input().split())
        m+=q*p
    print(m)'''

'''for i in range(1,int(input())+1):
    print(f'Case {i}: {sum(list(map(int, input().split())))}')'''

'''q = [0,0,0,0,0]
for i in range(int(input())):
    a,b = map(int, input().split())
    if a==0 or b==0:
        q[0]+=1
    elif a>0 and b>0:
        q[1]+=1
    elif a<0 and b>0:
        q[2]+=1
    elif a<0 and b<0:
        q[3]+=1
    elif a>0 and b<0:
        q[4]+=1

for i in range(4):
    print(f'Q{i+1}: {q[i+1]}')
print(f'AXIS: {q[0]}')'''

'''c3 = int(input())
c2 = int(input())
print(c2*2-c3)'''

'''for i in range(int(input())):
    print(f"Hello World, Judge {i+1}!")'''

'''a, b = map(int, input().split())
for i in range(a):
    print(input()[::-1])'''

'''s = input()
if s[0:3]=='555':
    print('YES')
else: 
    print('NO')'''

'''N, M = map(int, input().split())

lis = list(range(1, N+1))

for i in range(M):
    a, b = map(int, input().split())
    lis2 = lis[a-1:b]
    lis2.reverse()
    lis[a-1:b] = lis2
    
print(lis)'''

'''d = {'키':'값', '나':'권수현'}
print(d)'''

'''xx = []
yy = []

for i in range(3):
    a,b = map(int, input().split())
    xx.append(a)
    yy.append(b)

p = {}
for i in xx:
    p[xx.count(i)] = i
p2 = {}
for i in yy:
    p2[yy.count(i)] = i

print(p[min(p.keys())], p2[min(p2.keys())])'''

'''x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.extend(y)
print('x:', x)'''

'''t = int(input())
for i in range(t):
    s = list(input().split())
    s[0] = s[0].capitalize()
    for j in s:
        print(j, end=" ")'''

'''n = int(input())
score = input().split('0')
print(score)
# for i in range(n):
#     if score[i] == 1:
#         if score[i-1] == 1:

for i in score:
    i = int(i)

print(score)'''
'''
t = int(input())

for i in range(t):
    money = int(input())
    q = money//25
    d = (money%25)//10
    n = (money%25%10)//5
    p = money%25%10%5
    print(q,d,n,p)
'''
# 124//25 = 4
# 124%25 = 24//10 = 2

'''a = int(input())
b = int(input())
c = int(input())
d = str(a*b*c)

for i in range(10):
    print(d.count(str(i)))'''

'''n = int(input())

for i in range(n):
    s = 0
    cnt = 0
    sco = input()

    for j in sco:
        if j == 'O':
            cnt += 1
            s += cnt
        else:
            cnt = 0

    print(s)'''
'''
t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    b = a[1:]
    avg = sum(b)/a[0]
    cnt = 0
    for j in b:
        if j>avg:
            cnt += 1
    print(f"{(cnt/a[0])*100:.3f}%")'''

# t = int(input())
# for i in range(t):
#     n = int(input())
#     if n%2!=0 and 

'''s = input()
if s == '1 2 3 4 5 6 7 8':
    print('ascending')
elif s == '8 7 6 5 4 3 2 1':
    print('descending')
else:
    print('mixed')'''

'''t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    if c<=a:
        d = c
    else:
        d = c//a+1

    if c<=a:
        e = 1
    # elif c%a == 0:
    #     e = 
    else:
        e = c%a
    print(d, e)
    print(e*100+d)'''

'''t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    floor = n%h
    room = n//h+1
    print(floor, room)

    if floor == 0:
        room -= 1
        floor = h

    print(floor*100+room)'''

'''t = int(input())
gom = set()
cnt = 0
for i in range(t):
    s = input()
    if s != 'ENTER':
        if s not in gom:
            gom.add(s)
            cnt += 1
    elif s == 'ENTER':
        gom.clear()
print(cnt)
'''

# 오류 코드
'''t = int(input())
for i in range(t):
    s = list(input().split())
    s[0] = s[0].capitalize()
    for j in s:
        print(j, end=" ")'''


'''h, b, c, s = map(int, input().split())
s = h*b*c*a/1024/1024

print(f"{s:.2f} MB")'''

# 오류 코드
'''N = int(input())

for i in range(1,N+1):
    for j in range(i):
        print('*', end="")
    print()

for i in range(1,N+1):
    for j in range(N-i):
        print('*',end="")
    print()'''


'''while True:
    try:
        a, b = input().split()
        print(int(a)*b)
    except:
        break'''

# 오류 코드
'''T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    for i in range(len(S)+1):
        P = S[i]*R
        print(P,end="")'''



'''group_cnt = 0

t = int(input())
for i in range(t):
    cnt = 0
    word_list = []
    s = input()
    for j in range(len(s)):
        if s[j] in word_list:
            if s[j] != s[j-1]:
                cnt += 1
        word_list.append(s[j])
    
    if cnt == 0:
        group_cnt += 1
print(group_cnt)'''

'''import sys
input = sys.stdin.readline

cnt = 0

t = int(input())
for i in range(t):
    cnt += int(input()) - 1

cnt+=1
print(cnt)'''

'''e = []
for i in range(5):
    s = input()
    if "FBI" in s:
        e.append(i+1)
    
if len(e) == 0:
    print("HE GOT AWAY!")
else:
    print(*e)'''

'''t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    d = [i for i in a if i%2==0]
    print(sum(d), end=" ")
    print(min(d))'''


'''t = int(input())

for i in range(t):
    r, e, c = map(int, input().split())
    if r > e-c :
        print('do not advertise')
    elif r == e-c :
        print('does not matter')
    else:
        print('advertise')'''

'''n, m = map(int, input().split())
card = list(map(int, input().split()))
card.sort(reverse=True)
for i in range(len(card)):
    if card[i]+card[i+1]+card[i+2] <= m:
        print(card[i]+card[i+1]+card[i+2])
        break
    else:
        continue'''

'''a = int(input())
b = int(input())
print(a*b)'''

'''import sys

input = sys.stdin.readline

a, b = map(int, input().split())
lis1 = list(map(int,input().split()))
lis2 = list(map(int,input().split()))
print(*sorted(lis1+lis2))'''

'''# import sys
# input = 
d = []
t = int(input())
for i in range(t):
    a, b = input().split()
    a = int(a)
    d.append((a,b))

p = sorted(d, key= lambda item:item[0])

for i in p:
    print(i[0], i[1])'''

'''t = int(input())

for i in range(t):
    cla = list(map(int,input().split()))
    sco = list(sorted(cla[1:]))
    diff = []
    for j in range(cla[0]-1):
        diff.append(sco[j+1] - sco[j])
    print(f"Class {i+1}")
    print(f"Max {sco[-1]}, Min {sco[0]}, Largest gap {max(diff)}")'''

'''import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))'''

'''import sys

word = []
t = int(sys.stdin.readline())
for i in range(t):
    word.append(sys.stdin.readline().strip())
setWord = set(word)
word = list(setWord)
word.sort()
word.sort(key=len)
for i in word:
    print(i)'''

# n = int(input())
# lis = list(map(int, input().split()))
# cnt = 0
# for i in lis:
    
# print(cnt)

'''n = int(input())
lis = list(map(int, input().split()))
setLis = set(lis)
lis = list(setLis)
lis.sort()
print(*lis)'''

'''import sys
input = sys.stdin.readline

d = []
t = int(input())
for i in range(t):
    d.append(int(input()))
d.sort()
for i in d:
    print(i)'''

'''import sys
input = sys.stdin.readline()'''

'''a,b,v = map(int, input().split())
cnt = 0
while True:
    v -= a
    cnt += 1
    if v <= 0:
        break
    v += b'''


'''
print(cnt)'''

'''import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
for i in range(n):
    s = input().rstrip()
    if len(s)<m:
        continue
    else:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
d = dict(sorted(d.items(), key=lambda x:x[0]))
d = dict(sorted(d.items(),key=lambda x:-len(x[0])))
d = sorted(d.items(), key=lambda x:-x[1])
# d = sorted(d.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))
# print(d)
for i in d:
    print(i[0])'''

'''s = input().split('-')
for i in s:
    print(i[0],end="")'''

# import sys
# input = sys.stdin.readline

'''t = int(input())
for i in range(t):
    n, s = input().split()
    s = list(s)
    s.pop(int(n)-1)
    for i in s:
        print(i, end="")
    print()'''
'''
word_list = ['C','A','M','B','R','I','D','G','E']

s = list(input())
for i in word_list:
    while i in s:
        s.remove(i)

for i in s:
    print(i, end="")'''

# import sys
# input = sys.stdin.readline

'''t = int(input())
lis = []

for i in range(t):
    n = int(input())
    if n==0:
        lis.pop()
        continue
    lis.append(n)

print(sum(lis))'''

'''t = int(input())
lis = []

for i in range(t):
    x, y = map(int, input().split())
    lis.append([x, y])

lis.sort()
lis.sort(key=lambda x:x[1])
for i in lis:
    print(*i)'''

'''import sys
input = lambda: sys.stdin.readline().rstrip()

n, g = input().split()
d = set()

for i in range(int(n)):
    s = input()
    d.add(s)

if g == 'Y':
    print(len(d))
elif g== 'F':
    print(len(d)//2)
elif g == 'O':
    print(len(d)//3)'''

'''import sys
input = sys.stdin.readline

n = int(input())
meaList = list(map(int, input().split()))

print(max(meaList)*min(meaList))'''

'''import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    n = input()
    if n == '0':
        break
    for i in n:
        if i != '0':
            break
        else:
            n = n[1:]
    if n == n[::-1]:
        print("yes")
    else:
        print("no")'''

'''import sys
input = lambda: sys.stdin.readline().rstrip()

import math

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(math.lcm(a, b))'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n = list(input()[::-1])

for i in range(len(n)-1):
    if int(n[i])>=5:
        n[i+1] = int(n[i+1])+1
    n[i]='0'

for i in n[::-1]:
    print(i,end="")'''

'''a, b = map(int, input().split())
print(a/b)'''

'''while True:
    s = input()
    if s == '#':
        break
    a = s[0]
    b = s[2:].lower()
    print(a, b.count(a))'''

'''import sys
input = lambda: sys.stdin.readline().rstrip()

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())

lis = [a,b,c,d,e,f,g,h,i,j]
lis.sort()
lis2 = [lis.count(x) for x in lis]

print(sum(lis)//10)
print(lis[lis2.index(max(lis2))])'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''d = []
t = int(input())
for i in range(t):
    d.append(float(input()))

d.sort()
for i in d[:7]:
    print(f"{i:.3f}")'''


# t = int(input())
# for i in range(t):
#     k = int(input())
#     n =  int(input())
#     sum = 0
#     for i in range(k*n-n+1, k*n+1):
#         sum += i
#         print(i,'*')
#     print(sum)


'''arr = [
    1, 2, 3, #0
    1, 3, 6, #1
    1, 4, 10 #2
] # 1 3 => 6
  # 2 3 => 10'''


# k = 1
# n = 4

# d = [[0]*(n)]*(k+1)
# d = [[0]*(n) for x in range(k+1)]
# [[0,0,0],[0,0,0],[0,0,0]]


'''for i in range(n):
    d[0][i] = i+1
# print(d)

for i in range(1, k+1):
    for j in range(n):
        d[i][j]=sum(d[i-1][:j+1])
print(d[k][n-1])
'''
#k=0  1 2 3
#k=1  

'''arr2 = [
    1, 4, 10,20, #2
    1, 3, 6, 10, #1
    1, 2, 3, 4   #0
] # 2 4 => 20
  # 1 4 => 10
'''
# (k*n)+(k*n-1)+(k*n-2)
# for i in range(k*n-n+1, k*n):
#   sum += i

'''import sys
input = lambda: sys.stdin.readline().rstrip()


t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    d = [[0]*(n) for x in range(k+1)]

    for i in range(n):
        d[0][i] = i+1
    # print(d)

    for i in range(1, k+1):
        for j in range(n):
            d[i][j]=sum(d[i-1][:j+1])
    print(d[k][n-1])'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n = int(input())
sum = 1
for i in range(1,n+1):
    sum*=i
# print(sum)
# print(str(sum)[::-1])
cnt=0
for i in str(sum)[::-1]:
    if i != "0":
        break
    cnt += 1
print(cnt)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()
'''from collections import deque
queue = deque([])

t = int(input())
for i in range(t):
    s = input()
    if s[:4] == 'push':
        queue.append(s[5:])
    elif s == 'pop':
        if len(queue)>0:
            a = queue.popleft()
            print(a)
        else:
            print(-1)
    elif s == 'size':
        print(len(queue))
    elif s == 'front':
        print(queue[0]) if len(queue)>0 else print(-1)
    elif s == 'back':
        print(queue[-1]) if len(queue)>0 else print(-1)
    elif s == 'empty':
        print(0) if len(queue)>0 else print(1)'''

'''n = int(input())
s = list(map(int, input().split()))
t, p = map(int, input().split())

tSum = 0
for i in s:
    if i%t == 0:
        tSum += i//t
        continue
    tSum+= i//t+1

print(tSum)
print(n//p, n%p)'''

'''import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
okList = []
noOk = list(range(1,n+1))
i = 1
kk = 0
while True:
    if len(okList)==n:
        break
    # for i in 
    # kk = k*i + cnt
    # while kk>n:
    #     kk = kk-n
    # if kk not in okList:
    #     okList.append(kk)
    for i in range(k):  
        kk = kk+1
        # while kk>n:
        #     kk = kk-n

        # if kk in okList:
        #     kk+=1
        while True:
            while kk>n:
                kk = kk-n
            if kk in okList:
                kk+=1
            else: break
    okList.append(kk)
    i+=1

print(okList)'''

# 1 2 3 4 5 6 7
#     .         +3
#           .   +3
#   .           +3
#             . +3+2
#         .     +3+3

'''import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
okList = []
noOk = list(range(1,n+1))
i = 1
kk = 0
while True:
    if len(okList)==n:
        break
    for i in range(k):  
        kk = kk+1
        while True:
            while kk>n:
                kk = kk-n
            if kk in okList:
                kk+=1
            else: break
    okList.append(kk)
    i+=1

print('<', end="")
for i in okList[:-1]:
    print(f"{i}, ", end="")
print(f'{okList[-1]}>')'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n, k = map(int, input().split())
okList = []
noOk = list(range(1,n+1))
idx = 0
while noOk:
    idx += k - 1
    if idx >= len(noOk):
        idx %= len(noOk)
    okList.append(noOk.pop(idx))

print('<', end="")
for i in okList[:-1]:
    print(f"{i}, ", end="")
print(f'{okList[-1]}>')'''

'''import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
d1 = list(range(1,t+1))
d2 = []
n = list(map(int, input().split()))
for i in range(t):
    if n[i] == 0:
        d2.append(d1[i])
    else:
        d2.insert(-n[i], d1[i])
print(*d2)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''import math
for i in range(int(input())):
    a, b = map(int, input().split())
    print(math.lcm(a, b), math.gcd(a, b))'''

'''a, b = input().split()
a = a.replace('6', '5')
b = b.replace('6', '5')
mn = int(a)+int(b)
a = a.replace('5', '6')
b = b.replace('5', '6')
print(mn, int(a)+int(b))'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''for i in range(int(input())):
    n = input()
    n2 = n[::-1]
    if str(int(n)+int(n2)) == str(int(n)+int(n2))[::-1]:
        print("YES")
    else:
        print("NO")'''

'''T = int(input())
for i in range(T):
    a, b = input().split()
    a = int(a)
    b = int(b[-1])
    if a % 10 == 0:
        print(10)
    else:
        print(str(a**b)[-1])'''

'''import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    t = int(input())
    if t == 0:
        break
    d = []
    d2 = []
    for i in range(t):
        s = input()
        s2 = s.lower()
        d.append(s)
        d2.append(s2)
    print(d[d2.index(min(d2))])'''

'''for i in range(int(input())):
    print(sorted(list(map(int, input().split())))[-3])'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()
'''n = int(input())
a, b = 0, 1

for i in range(n):
  a, b = b, a + b
print(a)'''

'''a, b = input().split()

u = 0
for i in a:
    if i in b:
        u = b.index(i)
        u2 = a.index(i)
        break
# print(u)

for i in range(len(b)):
    for j in range(len(a)):
        if i == u:
            print(a[j],end="")
        elif j == u2:
            print(b[i], end="")
        else:
            print('.', end="")
    print()'''

'''import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for i in range(t):
    n = set(input())
    print(len(n))'''

'''import sys
input = lambda: sys.stdin.readline().rstrip()

i = 0
oneList = list(map(int,input().split()))
twoList = [1,2,3,4,5]
while True:
    if oneList[i+1] < oneList[i]:
        oneList[i+1], oneList[i] = oneList[i], oneList[i+1]
        print(*oneList)
    if oneList == twoList:
        break
    if i<3:
        i+=1
    else:
        i=0'''
    # print(i)

'''import sys
input = lambda: sys.stdin.readline().rstrip()

i = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    cnt = 0
    cnt += v//p*l
    if v%p >= l:
        cnt += l
    else:
        cnt += v%p
    print(f"Case {i}: {cnt}")
    i += 1'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''a, b, c = map(int, input().split())
cnt = (a+b)//c
total = cnt
while True:
    if cnt>=c:
        cnt = cnt//c
        total += cnt
        print(cnt, total)
    else:
        break
print(total)'''

'''n = 1000 - int(input())
a = n//500
b = n%500//100
c = n%100//50
d = n%50//10
e = n%10//5
f = n%5
print(a+b+c+d+e+f)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''d = []
for i in range(5):
    s = list(input())
    d.append(s)
# print(d)
for i in range(15):
    for j in range(len(d)):
        if len(d[j])<(i+1):
            continue
        print(d[j][i], end="")'''

'''d = [0]*10
num = list(map(int, input()))
for i in num:
    if d[i] == True:
        continue
    else:
        d[i] = num.count(i)
a = d.pop(6)
b = d.pop(8)
d.append(int((a+b)/2+(a+b)%2))
print(max(d))
'''
# import sys
# input = lambda: sys.stdin.readline().rstrip()
'''t = int(input())
d = list(input())'''
'''for i in range(t-1):
    s = input()
    for i in range(len(s)):
        if d[i] != s[i]:
            d[i] = '?'
        else:
            continue
for i in d:
    print(i,end="")'''
# 홀수 = 상근, 짝수 = 창영 
'''n = int(input())
if n%2==0:
    print("CY")
else:
    print("SK")'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''d = set()
t = int(input())
for i in range(t):
    a, b = input().split()
    if b == 'enter':
        d.add(a)
    elif b == 'leave':
        if a in d:
            d.remove(a)
        else:
            continue

for i in sorted(list(d), reverse=True):
    print(i)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n, m = map(int, input().split())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))
# print(d)
k = int(input())
for r in range(k):
    i, j, x, y = map(int, input().split())
    cnt = 0
    for p in range(i-1,x):
        cnt += sum(d[p][j-1:y])
    print(cnt)'''

'''import sys
input = lambda: sys.stdin.readline().rstrip()

ref = ['b', 'd', 'p', 'q', 'i', 'o', 'v', 'w', 'x']
while True:
    s = input()
    s1 = list(s)
    s2 = list(s)
    if s == '#':
        break
    result = ""
    for i in range(len(s2)):
        if s2[i] not in ref:
            result = "INVALID"
        if s2[i] == 'b':
            s2[i] = 'd'
        elif s2[i] == 'd':
            s2[i] = 'b'
        elif s2[i] == 'p':
            s2[i] = 'q'
        elif s2[i] == 'q':
            s2[i] = 'p'
    # print(s2)
    # print(s1)
    # print(s2)
    if result == "INVALID":
        print(result)
    else:
        for i in s2[::-1]:
            print(i, end="")
        print()'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''year = []
name = {}
for i in range(3):
    a,b,c = input().split()
    year.append(int(b)%100)
    name[int(a)]=c
name1 = sorted(name, reverse=True)
year.sort()
for i in year:
    print(i,end="")
print()
for i in name1:
    print(name[i][0], end="")'''

'''s = input()
if 'A' in s:
    s = s.replace('B', 'A')
    s = s.replace('C', 'A')
    s = s.replace('D', 'A')
    s = s.replace('F', 'A')
elif 'B' in s:
    s = s.replace('C', 'B')
    s = s.replace('D', 'B')
    s = s.replace('F', 'B')
elif 'C' in s:
    s = s.replace('D', 'C')
    s = s.replace('F', 'C')
else:
    s = 'A'*len(s)

print(s)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''s = input()
if s == s[::-1]:
    print("true")
else:
    print("false")'''

'''t = int(input())
d = []
for i in range(t):
    d.append(list(map(int, input().split())))
r = [0]*(d[-1][0])
d.sort(key=lambda x:-x[2])
# print(r)
cnt = 0
for i in d[:5]:
    if cnt == 3:
        break
    if r[i[0]-1]<2:
        print(i[0],i[1])
        r[i[0]-1] += 1
        cnt += 1
    else:
        continue'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()
'''n = int(input())
s = input()
for i in range(0,len(s),n):
    print(s[i],end="")'''
# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''word_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

t= int(input())

for j in range(t):
    a, b = map(int, input().split())
    s = input()
    for i in s:
        n = word_list.index(i)
        print(word_list[(n*a+b)%26], end="")
    print()'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()
'''a = int(input())
b = int(input())
for i in range(a):
    print("*"*b)'''
'''n, m = map(int, input().split())
cnt = 0
for i in range(n):
    s = input()
    if s.count("O") > s.count("X"):
        cnt += 1
print(cnt)'''
# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''cnt = 0
while True:
    try:
        a = input()
        cnt +=1
    except EOFError:
        break
print(cnt)'''

'''t = int(input())
for i in range(t):
    s = input()
    if s[0:10] == 'Simon says':
        print(s[10:])'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''t = int(input())
for j in range(t):
    n, k = map(int, input().split())
    n_list = list(map(int, input().split()))
    cnt = 0
    for i in n_list:
        cnt += i//k
    print(cnt)

'''

'''k = int(input())
a, b, c, d = map(int, input().split())

if a*k + b == c*k + d:
    print("YES",(a*k + b))
else:
    print("NO")'''


'''d = [64]
x = int(input())
while sum(d) > x:
    mn = d.pop(d.index(min(d)))
    d.extend([mn//2, mn//2])
    if sum(d)-(min(d)) >=x:
        d.pop(d.index(min(d)))

print(len(d))'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''for i in range(int(input())):
    a, b = map(int, input().split())
    if a % 10 == 0:
        print(10)
    else:
        b = (b % 4) + 4
        print((a ** b) % 10)'''

'''for i in range(int(input())):
    p = input()
    c1 = sorted(list(input()))
    c2 = sorted(list(input()))
    if c1 == c2:
        print("NOT CHEATER")
    else:
        print("CHEATER")'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()
'''S = input()
t = input()

stack = []
ex_len = len(t)

for i in range(len(S)):
    stack.append(S[i])
    if ''.join(stack[-ex_len:]) == t:
        for _ in range(ex_len):
            stack.pop()

# 결과 출력
print(''.join(stack))'''

'''t = int(input())
tl = sorted(list(map(int, input().split())))
print(sum([sum(tl[:i+1]) for i in range(t)]))'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''d2 = []
n, k = map(int, input().split())
d1 = list(range(1, n+1))
i = 0
while 1:
    if sum(d1) == 0:
        break
    i += k-1
    while i >= len(d1):
        i -= len(d1)
    d2.append(d1.pop(i))

print("<",end="")
for i in d2[:-1]:
    print(i, end=", ")
print(f"{d2[-1]}>")'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''t = int(input())
for i in range(t):
    a = sorted(list(map(int, input().split())))
    if a[2]**2 == a[0]**2 + a[1]**2:
        print(f"Scenario #{i+1}:")
        print('yes\n')
    else:
        print(f"Scenario #{i+1}:")
        print("no\n")'''

'''h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t = h2*3600+m2*60+s2 - (h1*3600+m1*60+s1)
if t < 0:
    t += 60*60*24
h = t//3600 
m = (t%3600)//60 
s = t%60
print("%02d:%02d:%02d" % (h,m,s))'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''d = {}
t = int(input())
for i in range(t):
    w,W = input().split()
    d[W] = w
s = input()
p = ""
for i in s:
    p += d[i]
y,u = map(int, input().split())
print(p[y-1:u])'''

'''d = []
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a <= b:
        d.append(b)

if len(d) > 0:
    print(min(d))
else:
    print(-1)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''def num(n, s):
    if s == 1:
        return int(str(n)[s-1])
    return int(str(n)[s-1]) + num(n, s-1)

n = int(input())
s = len((str(n)))
print(num(n,s))'''

'''def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''d = []
for i in range(5):
    a = int(input())
    if a in d:
        d.remove(a)
    else:
        d.append(a)

print(d[0])'''

# a,b = map(int, input().split())
# for i in range(b):
#     d = []
#     for i in range(1,a+1):
#         if a%i==0:
#             d.append(i)
    # for j in range(2,a//2):
    #     if a%j==0:
    #         q=j; p=a//j
    # a = int(str(q)+str(p))
# print(a)

# a = input()
# d = [int(i) for i in a]
# while 1:
#     t = 1
#     if len(d)==1:
#         break
#     d = [int(i) for i in d]
#     for i in d:
#         t*= i
#     d = str(t)
# print(d)

'''a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
t1 = min([a,b,c])
t2 = min([d,e])
print(t1+t2-50)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()
'''
d1 = []
d2 = []

for i in range(9):
    p = list(map(int, input().split()))
    q = max(p)
    d1.append(p)
    d2.append(q)
print(max(d2))
print(d2.index(max(d2))+1, d1[d2.index(max(d2))].index(max(d2))+1)'''


'''d = [[0 for x in range(100)] for y in range(100)]
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    for j in range(100):
        if j==(90-b):
            for k in range(10):
                for l in range(10):
                    d[90-b+k][a+l] = 1
total = 0
for i in d:
    total += i.count(1)
print(total)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''word_list = {'A':'a', 'K':'k', 'M':'m', 'O':'o','T':'t', 'B':'v', 'E':'ye', 'H':'n', 'P':'r', 'C':'s', 'Y':'u', 'X':'h'}
s1 = input()
s2 = ""
for i in s1:
    s2 += word_list[i]
print(s2)'''

'''s = input()
n = int(input())
cnt = 0
total = 0
for i in range(n):
    s2 = input()
    p = []
    for j in range(len(s2)):
        cnt = 0
        if s2[j]==s[0] and not(bool(p)):
            for k in range(len(s)):
                if s[k] == s2[(k+j)%(len(s2))]:
                    cnt +=1
                    # print(s[k], s2[j], cnt)
            if cnt == len(s):
                total+=1
                p = [1]
print(total)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''G = sum(map(int, input().split()))
E = sum(map(int, input().split()))

if G>E:
    print("Gunnar")
elif E>G:
    print("Emma")
else:
    print("Tie")'''

'''pri = int(input())

get1 = pri*0.78
get2 = pri - pri*0.2*0.22
print(int(get1), int(get2))'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''d = []
while 1:
    s = input()
    if s == '-1':
        break
    s = s.split()
    d.append(s)

pa = 0
rList = []
for i in d:
    if i[2] == 'right':
        if i[2] not in rList:
            rList.append(i)
            pa += int(i[0])

wcnt = 0
for i in rList:
    for j in d:
        if j[1] == i[1]:
            # pa += int(j[0])
            if j[2] == 'wrong':
                wcnt += 1

# print(rList)
print(len(rList),pa+wcnt*20)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n = int(input())
f = int(input())

d = []
i = 0
while 1:
    a = str(n-(n%f)-f*i)
    if len(a)<3:
        a = '00000'+a
    # print(a)
    if a[-3] != str(n)[-3]:
        break
    d.append(a[-2:])
    i += 1

i = 0
d1 = []
while 1:
    b = str(n + f - (n%f)+f*i) # 1000+3-1 = 1002
    if len(b)<3:
        b = '00000'+b
    # print(b)
    if b[-3] != str(n)[-3]:
        break
    d1.append(b[-2:])
    i += 1

d = [int(x) for x in d]
d1 = [int(x) for x in d1]
d2 = d+d1
print(f"{min(d2):0>2}")'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n, m = map(int, input().split())
k = list(map(int, input().split()))
t = set()
for i in k:
    a = i
    while a<=n:
        t.add(a)
        a+=i
    # print(t)
print(sum(list(t)))'''

'''n, m = map(int, input().split())

if n <= 1023:
    print('No thanks')
else:
    n -= 1023
    nums = [1,2,4,8,16,32,64,128,256,512]
    d = []
    while m:
        for i in nums[::-1]:
            if m >= i:
                d.append(i)
                m -= i
        print(d)
    for i in d:
        if n == i:
            print('Thanks')
            break
        else:
            print('Impossible')
            break'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n, d = input().split()

cnt = 0
for i in range(1, int(n)+1):
    cnt += str(i).count(d)

print(cnt)'''

'''for i in range(int(input())):
    d = input().split()[::-1]
    print(f"Case #{i+1}: ", end="")
    for j in d:
        print(j, end=" ")'''

'''d = []
for i in range(int(input())):
    n = int(input())
    d.append(n)
d = d[::-1]

total = 0
m = d[0]
for i in range(len(d)):
    if d[i]>m:
        total += 1
        m = d[i]
print(total+1)
'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''t = int(input())
d = [60*5, 60, 10]
p = []
for i in d:
    if t>=i:
        q = t//i
        p.append(t//i)
        t -= q*i
    else:
        p.append(0)
if t%d[2]!=0:
    print(-1)
else:
    print(*p)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''N = int(input())

alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if alist[i] < blist[i]:
        cnt += blist[i] - alist[i]
print(cnt)'''

'''n, m = map(int, input().split())
total = 0
d = []
for i in range(m):
    a, b = map(int, input().split())
    d.append(a)
d = sorted(d)
for i in d[1:]:
    if i < n:
        total += n-i

print(total)'''

'''n = int(input())
lis = list(map(int,input().split()))
total = 0
for i in lis:
    cnt = 0
    for j in range(2, i):
        if i%j==0:
            print(i, j, 0)
            break
        else:
            cnt+=1
    if cnt == i-2:
        total += 1
print(total)'''

'''v = int(input())

print('v'*v)'''

'''s = 'WelcomeToSMUPC'
n = int(input())
print(s[n%14-1])'''


# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''nl = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
d = []
for i in range(int(input())):
    s = input()+" "
    d1 = ''
    for j in range(len(s)):
        if s[j] in nl:
            d1 += s[j]
        else:
            if bool(d1) == True:
                d.append(d1)
            d1 = ''

d = [int(x) for x in d]

for i in sorted(d):
    print(i)'''

"""d = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./"
while True:
    s = input()
    if s == '':
        break
    p = ''
    for i in s:
        if i != " ":
            r = d.index(i)-1
            p += d[r]
        else:
            p+=' '
    print(p)
"""
# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''d = []
for i in range(int(input())):
    s = input()
    if len(s)==3:
        d.append(s)
print(sorted(d)[0])'''
'''d = []
for i in range(7):
    s = input().split()
    s[1] = int(s[1])
    d.append(s)

d = sorted(d ,key=lambda x:x[1], reverse=True)
print(d[0][0])'''

'''n = int(input())+2

for i in range(n):
    if i == 0 or i == n-1:
        print('@'*n)
    else:
        print('@'+' '*(n-2)+'@')'''

# n = int(input())

'''for i in range(n*5):
    if i >= n*4 or i < n:
        print('@'*n*5)
    else:
        print('@'*n)'''

'''for i in range(n*5):
    if i < n:
        print('@'*n*3 + ' '*n + '@'*n)
    elif n<=i<n*4:
        print('@'*n + ' '*n + '@'*n+ ' '*n + '@'*n)
    else:
        print('@'*n + ' '*n + '@'*n*3)'''

# n = int(input())

'''for i in range(n*5):
    if i < n or i >= n*4:
        print('@'*n*5)
    else:
        print('@'*n+' '*((n*5)-(n*2))+'@'*n)'''

'''for i in range(n*5):
    if n*2<=i<n*3 or i>=n*4:
        print('@'*n*5)
    else:
        print('@'*n + ' '*n*3 + '@'*n)'''
# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n = int(input())

for i in range(n*5):
    if n<= i < n*2 or n*3<= i < n*4:
        print('@'*n*5)
    else:
        print('@'*n+' '*n*3+'@'*n)'''

'''n = int(input())

for i in range(n):
    print(' '*(n-i-1)+'*', end="")
    if i > 0:
        print(' '*((1+i*2)-2)+'*')
    else:
        print()'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n, m = map(int, input().split())

n1 = (n+3)//4-1
# n2 = n%4 if n%4!=0 else n%4+4
n2 = (n-1)%4
m1 = (m+3)//4-1
# m2 = m%4 if m%4!=0 else m%4+4
m2 = (m-1)%4
print(n1, m1, n2, m2)
total = max(n1, m1) - min(n1, m1)
total += max(n2, m2) - min(n2, m2)
print(total)'''

'''def pn(r, k):
    for i in range(2, k):
        if r % i == 0:
            if i < k:
                print("BAD", i)
                return
    print("GOOD")
    return'''

'''r, k = map(int, input().split())

pn(r, k)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''t = int(input())
n = list(map(int, input().split()))

score = 0
sl = [0]*t
for i in range(t):
	if n[i] == 1:
		if sl[i-1] >= 1:
			sl[i] = sl[i-1]+1
			score += sl[i]
		else:
			score += 1
			sl[i] = 1
	else:
		sl[i] = 0
		
print(score)'''

'''t = int(input())
for i in range(t):
    q = input()
    n = int(input())
    sum = 0
    for j in range(n):
        a = int(input())
        sum += a
    if sum%n==0:
        print("YES")
    else:
        print("NO")'''

'''d = []
for i in range(7):
    n = int(input())
    if n%2!=0:
        d.append(n)
if bool(d) == False:
    print(-1)
else:
    print(sum(d))
    print(min(d))'''

'''import math

n = int(input())
print(f"{n**2*math.pi:.6f}")
print(f"{n**2*2:.6f}")'''
'''
while 1:
    a, b = input().split()
    if a == b == '0':
        break
    cnt = 0
    carry = 0
    a = list(a)[::-1]; b = list(b)[::-1]
    t = max(len(a), len(b))
    for i in range(t):
        if int(a[i]) + int(b[i]) + carry >= 10:
            cnt+=1
            carry = 1
        else:
            carry = 0
    print(cnt)'''
    
# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''for i in range(int(input())):
    a = int(input())
    for j in range(a):
        for k in range(a):
            if j == 0 or j == a-1 or k == 0 or k == a-1:
                print('#', end="")
            else:
                print('J', end="")
        print()
    print()'''

'''a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if b%d==0:
    q = b//d
else:
    q = b//d+1
if b%d==0:
    w = c//e
else:
    w = c//e+1

print(a-max(q,w))'''

'''a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

for i in [a,b,c]:
    firSec = i[0]*60*60+i[1]*60+i[2]
    lasSec = i[3]*60*60+i[4]*60+i[5]
    s = lasSec - firSec
    s1 = s//3600; s2=(s-s1*3600)//60
    s3 = (s-s1*3600-s2*60)
    print(s1, s2, s3)'''

'''a = list(map(int, input().split()))
x, y, r = map(int, input().split())

for i in a:
    if i == x:
        print(a.index(i)+1)
        a.pop()
if len(a) == 4:
    print(0)'''

'''a = []
for i in range(8):
    s = int(input())
    a.append(s)

b = sorted(a, reverse=True)
print(sum(b[:5]))

d = []
for i in b[:5]:
    d.append(a.index(i)+1)
print(*sorted(d))'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''a, b = map(int, input().split())

if a == 1 :
    a = 2

for i in range(a, b+1):
    cnt = 0
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            cnt = 1
            break
    if cnt==0:
        print(i)
'''

'''a, b = map(int, input().split())

s = a - (a*b/100)
if s>=100:
    print(0)
else:
    print(1)'''

'''total = 0
for i in range(int(input())):
    s = input()
    if int(s[2:])<=90:
        total+=1
print(total)'''
'''d = {136:1000, 142:5000, 148:10000, 154:50000}

total = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    total += d[a]
print(total)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''a, b = map(int, input().split())
c = min(a, b+1)
d = c-1
print(c+d)'''
'''
a,b=map(int, input().split())

print(min(a, b*2)//2)'''

'''d = [500, 0.1, 2000, 0.25]

a = int(input())
b = int(input())
q = []
if a > 20:
    a = 20
for i in range(a//5):
    if i%2==0:
        q.append(b-d[i])
    else:
        q.append(b-int(d[i]*b))

if bool(q)==False:
    print(b)
elif b<b-min(q):
    print(0)
else:
    print(min(q))'''
# print(q)
'''
a = int(input())
print(2**a)'''

'''d = []
for i in range(15):
    s = input()
    d.append(s)

for i in d:
    if 'w' in i:
        print('chunbae')
        break
    elif 'b' in i:
        print('nabi')
        break
    elif 'g' in i:
        print('yeongcheol')
        break'''

'''t = int(input())
n = int(input())
f = list(map(int, input().split()))

if t <= sum(f):
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")'''
'''
for i in range(int(input())):
    y = input()
    n = int(y[-2:])
    y = int(y)+1
    if y%n==0:
        print("Good")
    else:
        print("Bye")'''

'''a = input()

if a[0] == a[-1]=='"':
    if len(a) < 3: 
        print("CE")
    else:
        print(a[1:-1])
else:
    print("CE")'''

'''s = input()
l = input()
a = input()
print(l.count(a))'''

'''d = []
q = ['l', 'p', 'k']

d.append(input())
d.append(input())
d.append(input())

for i in d:
    for j in q:
        if i[0] == j:
            q.remove(i[0])

if bool(q) == False:
    print("GLOBAL")
else:
    print("PONIX")'''

'''a = int(input())

for i in range(a):
    if i == 0:
        print(' '*(a-i-1)+'*')
        continue
    if i == a-1:
        print('*'*(a*2-1))
        continue
    print(' '*(a-i-1)+'*'+' '*(1+(i-1)*2)+'*')'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n = int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'* '*i)'''


'''n = int(input())
for i in range(n):
    m = int(input())
    i = 0
    for j in range(30):
        if i == 1:
            break
        for k in range(30):
            if 2**j+2**k == m:
                print(j, k)
                i = 1
                break
'''

'''n, x = map(int, input().split())

d = []
for i in range(n):
    s, t = map(int, input().split())
    if s+t<=x:
        d.append([s,t])

d.sort(key=lambda x:(x[0], x[1]), reverse=True)
if d:
    print(d[0][0])
else:
    print(-1)'''

'''t = input()
s = input()
print(s[-5:])'''
'''
d = []
for i in range(int(input())):
    d.append(int(input()))
sum = 0
a = int(input())
for i in range(a):
    y = int(input())
    sum += d[y-1]
print(sum)'''

'''print(input().count("DKSH"))'''

"""a, b = map(int, input().split())

'''m = (b-a)/400
print(1/(1+10**m))'''

print(min(a,b)//2)"""
'''
a, b = map(int, input().split())
c = list(map(int, input().split()))

min = c[0]+c[1]
for i in range(a-1):
    if c[i]+c[i+1] <= min:
        min = c[i]+c[i+1]

print(min*b)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''a, b, c = map(int, input().split())
print(max(b, a+c))'''


'''while 1:
    a = input()
    if a == '0':
        break
    cnt = 0
    for i in range(len(a)):
        p = 1
        for j in range(1,(len(a)-i+1)):
            p *= j
        cnt += int(a[i])*p
    print(cnt)'''
'''
import sys
input = lambda: sys.stdin.readline().rstrip()

d = {'BANANA':0, 'STRAWBERRY':0, 'PLUM':0, 'LIME':0}
t = int(input())
for i in range(t):
    a, b = input().split()
    d[a] += int(b)

cnt = 0
for i in d.items():
    if i[1] == 5:
        cnt = 1
        print("YES")
        break
if cnt == 0:
    print("NO")'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''d = []
for i in range(int(input())):
    s = input()
    d.append(s)

pw = ''
for i in d:
    for j in d:
        if i[::-1] == j:
            pw = i
            break

print(len(pw), pw[len(pw)//2])'''

'''n, m = map(int, input().split())

d = {}

for i in range(n):
    a, b, c = input().split(' ', maxsplit=2)
    c = c[:5]
    if c in d:
        d[c] = '?'
    else:
        d[c] = b

for i in range(m):
    s = input()
    if s in d:
        print(d[s])
    else:
        print('!')'''

'''d = []
n = int(input())
for i in range(n):
    d.append(int(input()))

d = d[::-1]
# print(d.index(max(d)))
# print(len(d)-1)

cnt = 0
while d.index(max(d)) != len(d)-1:
    d[d.index(max(d))] -= 1
    d[-1] += 1
    cnt+=1
print(cnt)'''

'''n = int(input())
d = []
for i in range(1, n+1):
    d.append(i)
print(d)

for i in range(len(d)-1):
    print(d[0], end=" ")
    # print(d)
    d.pop(0)
    d.append(d.pop(0))
print(d[0])'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n = int(input())
s = input().split()
d = {}
for i in s:
    d[i] = 0

for i in range(n):
    p = input().split()
    for j in p:
        if j in d:
            d[j] += 1
        else:
            continue
d = sorted(d.items(), key=lambda x:(x[0]))
d = sorted(d, key=lambda x:(x[1]), reverse=True)
for i in d:
    print(i[0], i[1])'''

'''n = int(input())
lis = input().split()
s = set()

for i in lis:
    if i[-6:]=='Cheese':
        s.add(i)

if len(list(s)) >= 4:
    print("yummy")
else:
    print("sad")'''

'''a, b = input().split()
c, d = input().split()

s = set([a, b, c, d])
s = sorted(list(s))

for i in s:
    for j in s:
        print(i, j)'''

'''d = {}
n, m, k = map(int, input().split())
for i in range(n):
    a, b = input().split()
    d[a] = int(b)
cnt = 0
for i in range(k):
    a = input()
    cnt += d[a]
    del d[a]
d = sorted(d.items(), key=lambda x:x[1])
mi = cnt; ma = cnt

for i in range(m-k):
    mi += d[i][1]
    ma += d[-i-1][1]

for i in d[:m-k]:
    mi += i[1]
for i in d[-(m-k):]:
    ma += i[1]
print(mi, ma)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n = int(input())

c = {}
d = {}
e = []
f = {}
for i in range(n):
    a, b = input().split()
    if b in d:
        if b not in f:
            f[b] = 2
        else:
            f[b] += 1
    if b != '-':
        c[a] = b
        d[b] = a'''
# print(d)
# print(f)

'''f = [k for k, v in f.items() if v == 2]

for i in f:
    g = [k for k,v in c.items() if v == i]
    e.append(g)
# print(e)
print(len(e))
if e:
    for i in e:
        print(i[0], i[1])'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''m, m = map(int, input().split())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
print(len(list(a-b))+len(list(b-a)))'''

'''d = {}
for i in range(int(input())):
    a = input()
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1
d = sorted(d.items())
d = sorted(d, key=lambda x:x[1], reverse=True)

print(d[0][0])'''

# w = set()
# h = set()
'''n, m = map(int, input().split())
for i in range(n):
    s = input()
    w.add(s)
for i in range(m):
    s = input()
    h.add(s)
d = sorted(list(w&h))
print(len(d))
for i in d:
    print(i)'''

'''m, m = map(int, input().split())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
print(len(list(a-b)))
if list(a-b):
    print(*sorted(list(a-b)))
'''
# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''o = ['1', '2', '3', '4', '6', '7', '0', '9']
for i in range(int(input())):
    n = int(input())
    d1 = list(map(int, input().split()))
    n = int(input())
    d2 = list(map(int, input().split()))
    n = int(input())
    d3 = list(map(int, input().split()))
    t = set()
    for l in d1:
        for j in d2:
            for k in d3:
                p = l+j+k
                p = str(p)
                cnt = 0
                for i in p:
                    if i in o:
                        break
                    else:
                        cnt += 1
                if cnt==len(p):
                    t.add(p)
    print(len(list(t)))'''

'''import sys
input = lambda: sys.stdin.readline().rstrip()

a1, a2, a3 = map(int, input().split())
c1, c2, c3 = map(int, input().split())

b3 = c3 - a1
b1 = c1 - a3
b2 = c2//a2

print(b1, b2, b3)'''
'''
n = int(input())
while 1:
    a = int(input())
    if a == 0:
        break
    print(f"{a} is", end="")
    print("", end="") if a%n==0 else print(" NOT", end="")
    print(f" a multiple of {n}.")
'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n = int(input())

d1 = 0
d3 = 0
for i in range(1, n+1):
    d1 += i
    d3 += i**3
print(d1)
print(d1**2)
print(d3)'''

'''d = ['Never gonna give you up', 
'Never gonna let you down', 
'Never gonna run around and desert you', 
'Never gonna make you cry', 
'Never gonna say goodbye', 
'Never gonna tell a lie and hurt you', 
'Never gonna stop']

for i in range(int(input())):
    s = input()
    if s not in d:
        print('Yes')
        exit()
print('No')'''


'''for i in range(int(input())):
    s, t = input().split('=')
    if eval(s) == int(t):
        print('correct')
    else:
        print('wrong answer')
'''

'''for i in range(int(input())):
    n = int(input())
    a1 = input().split()
    a2 = input().split()
    b2 = input().split()
    b1 = [0]*n
    d = []
    for i in range(n):
        d.append(a1.index(a2[i]))
    # print(d)
    for i in range(n):
        b1[d[i]] = b2[i]
    print(*b1)
'''

'''def fri(a, b):
    for i in range(1, a+1):
        if a%i==0 and b%i==0:
            print(i, a//i, b//i)


a, b = map(int, input().split())

fri(a, b)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''def mod(a, b, c):
    cnt = 0
    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                if i%j == j%k == k%i:
                    cnt+=1
    print(cnt)


for i in range(int(input())):
    a, b, c = map(int, input().split())
    mod(a, b, c)'''


# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''for i in range(int(input())):
    s = list(input())
    k = 0
    while 1:
        if s == s[::-1]:
            break
        if k == 0:
            s.append(s[k])
        else:
            s.insert(-k, s[k])
        k += 1
    
    for x in s:
        print(x, end="")
    print()'''

'''a, b = input().split()
print(str(int(a[::-1])+int(b[::-1]))[::-1].lstrip('0'))'''


'''def xor(a, b, c):
    if c == 0:
        return a
    a = (a and (not b)) or ((not a) and b)
    c -= 1
    return xor(a, b, c)

a, b, c = map(int, input().split())

# xor(a, b, c)
print(xor(a, b, c))'''

'''def p(x):
    d = ['1','2','3','5','6','8','9','0']
    for j in range(len(str(x))):
        if str(x)[j] in d:
            return
    print(x)
    a = 1
    return a


n = int(input())
for i in range(n, 3, -1):
    a = p(i)
    if a == 1:
        break
'''
'''
t = int(input())
for i in range(t):
    r = input()
    a, b = input().split()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
  '''  

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n = int(input())
s = 0
for i in range(0, n):
    s += n*i+i
print(s)'''

'''n, m = map(int, input().split())

d = []
for i in range(n):
    s = input().split()
    d.append(s)
for i in range(m):
    s = input().split()
    cnt = 0
    for j in d:
        if s[0] == j[0] or s[0] == '-':
            if s[1] == j[1] or s[1] == '-':
                if s[2] == j[2] or s[2] == '-':
                    cnt += 1
    print(cnt)'''

'''p1 = 0
p2 = 0
p3 = 0
A = [[0,1], [0,2], [0,3]]
for i in range(int(input())):
    a, b, c = map(int, input().split())
    p1 += a; p2 += b; p3 += c
    A[0][0] += a**2
    A[1][0] += b**2
    A[2][0] += c**2

A = sorted(A)

if A[2][0] == A[1][0]:
    print(0, max(p1, p2, p3))
else:
    print(A[2][1], max(p1, p2, p3))'''

'''d = sorted(list(map(int, input().split())))
c = int(input())
s = set()
cnt = 0
for i in d:
    for j in d:
        if i<=j and i+j==c:
            if (i, j) not in s:
                print(i, j)
                cnt += 1
                s.add((i, j))
print(cnt)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''d = []
n, m = map(int, input().split())
for i in range(n):
    n = int(input())
    d.append(n)
d = sorted(d)
for i in range(m):
    n = int(input())
    if n in d:
        print(d.index(n))
    else:
        print(-1)'''

'''N = int(input())
stack = []

def push(_) :
    stack.append(_)

def pop() :
    if len(stack) == 0 :
        print(-1)
    else :
        print(stack.pop())

def size() :
    print(len(stack))

def empty() :
    if len(stack) == 0 :
        print(1)
    else :
        print(0)

def top() :
    if len(stack) == 0 :
        print(-1)
    else :
        print(stack[-1])


for i in range(N) :
    inputs = input()
    if not inputs.find(' ') == -1 :
        a, b = inputs.split()
        b = int(b) 
        if a == 'push' :
            push(b)
    else :
        a = inputs
        if a == 'pop' :
            pop()
        elif a == 'size' :
            size()
        elif a == 'empty' :
            empty()
        elif a == 'top' :
            top()'''
'''
n, m = map(int, input().split())
s = set()
for i in range(n):
    p = input()
    s.add(p)
cnt = 0
for i in range(m):
    p = input()
    if p in s:
        cnt += 1
print(cnt)
'''
# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''from collections import deque
queue = deque([])

t = int(input())
for i in range(t):
    s = input()
    if s[:4] == 'push':
        queue.append(s[5:])
    elif s == 'pop':
        if len(queue)>0:
            a = queue.popleft()
            print(a)
        else:
            print(-1)
    elif s == 'size':
        print(len(queue))
    elif s == 'front':
        print(queue[0]) if len(queue)>0 else print(-1)
    elif s == 'back':
        print(queue[-1]) if len(queue)>0 else print(-1)
    elif s == 'empty':
        print(0) if len(queue)>0 else print(1)'''

'''d = []
d1 = []
for i in range(int(input())):
    a, b = map(int, input().split())
    d.append([a, b])
    d1.append(b)

r = []

for i in d:
    cnt = 0
    for j in d:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    r.append(cnt+1)

print(*r)'''

'''n, m = map(int, input().split())
d1 = []
for i in range(n):
    l = list(map(int, input().split()))
    d1.append(l)
m, k = map(int, input().split())
d2 = []
for i in range(m):
    l = list(map(int, input().split()))
    d2.append(l)

res = [[0 for x in range(k)] for x in range(n)]

for i in range(n):
    for j in range(k):
        for h in range(m):
            res[i][j] += d1[i][h] * d2[h][j]

for i in res:
    print(*i)'''

'''n, m = map(int, input().split())
d = []

for i in range(n):
    l = list(map(int, input().split()))
    d.append(l)

sx = []
sy = []
for i in range(n):
    for j in range(m):
        if d[i][j] == 1:
            sx.append(i)
            sy.append(j)
# print(sx, sy)
if sx[1] - sx[0] < 0:
    x = -(sx[1] - sx[0])
else:
    x = sx[1] - sx[0]
if sy[1] - sy[0] < 0:
    y = -(sy[1] - sy[0])
else:
    y = sy[1] - sy[0]
print(x+y)'''

import sys
input = lambda: sys.stdin.readline().rstrip()

'''t = set()
for i in range(int(input())):
    s = input().split()
    if s[0] == 'add':
        t.add(int(s[1]))
    elif s[0] == 'remove':
        t.discard(int(s[1]))
    elif s[0] == 'check':
        if int(s[1]) in t:
            print(1)
        else:
            print(0)
    elif s[0] == 'toggle':
        if int(s[1]) in t:
            t.discard(int(s[1]))
        else:
            t.add(int(s[1]))
    elif s[0] == 'all':
        t = set(range(1, 21))
    elif s[0] == 'empty':
        t = set()'''

'''n, w, h, l = map(int, input().split())
o = (w//l)*(h//l)
print(min(n, o))'''

'''n, m = map(int, input().split())

d = []

for i in range(m):
    b = int(input())
    book_list = list(map(int, input().split()))
    d.append(book_list)


stc = [0]
sum = 1
while sum>0:
    for i in d:
        if i[-1] == stc[-1] + 1:
            stc.append(i[-1])
            print(i.pop())

print(stc)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''d = list(map(int, input().split()))
d.sort()
print(d[0]*d[2])


if max(d[1] - d[0], d[2] - d[1]) // 2 + 1 not in d:
    d[1] = max(d[1] - d[0], d[2] - d[1]) // 2 + 1

print(d)'''
# 0 1 1 0 0 1
# 0 0 1 0 1 0 0 0 

'''a, b, c = input().split()

d = ['+', '-', '*', '//']

for i in d:
    s = a+i+b
    if eval(s) == int(c):
        if i == '//':
            print(a+'/'+b+'='+c)
        else:
            print(s+'='+c)
        exit()

for i in d:
    s = b+i+c
    if eval(s) == int(a):
        if i == '//':
            print(a+'='+b+'/'+c)
        else:
            print(a+'='+s)
        exit()'''

'''def rR(p2):
    if p2 == 'P':
        # c2 += 1
        return 1
    elif p2 == 'S':
        c1 += 1
        return
    else:
        return

def pR(p2):
    if p2 == 'P':
        return
    elif p2 == 'S':
        c2 += 1
        return
    else:
        c1 += 1
        return

def sR(p2):
    if p2 == 'P':
        c1 += 1
        return 1
    elif p2 == 'S':
        return
    else:
        c2 += 1
        return

for _ in range(int(input())):
    c1 = 0; c2 = 0
    for i in range(int(input())):
        a, b = input().split()
        if a == 'R':
            c += rR(b)
        elif a == 'P':
            pR(b)
        else:
            sR(b)

    print(c1, c2)'''

'''while 1:
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1] == a[2] == 0:
        break
    if a[0] == a[1] == a[2]:
        print("Equilateral")
    elif a[0] + a[1] > a[2]:
        if ((a[0] == a[1]) and (a[1] != a[2])) or ((a[0] != a[1]) and (a[1] == a[2])) or ((a[0] == a[2]) and (a[0] != a[1])):
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")'''

# n = int(input())

'''if n%2==0:
    r = round(n/2)
    print((r+1)*(r+1))
else:
    r = n//2+1
    print(r*(r+1))'''

'''a, b, c = map(int, input().split('/'))
if a + c < b or b ==:
    print("hasu")
else:
    print("gosu")'''


# n = int(input())
# d = [0, 0]
# for i in range(n):
#     a, b = map(int, input().split())
#     if a == b:
#         continue
#     elif a > b:
#         d[0] += 1
#     else:
#         d[1] += 1

# print(*d)
# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''for i in range(int(input())):
    s = input()
    res = ""
    for j in range(len(s)):
        if s[j] == 'Z':
            res += 'A'
        else:
            res += chr(ord(s[j])+1)
    print(f"String #{i+1}")
    print(res)
    print()'''

'''v = input()
v = input()

a = v.count("A")
b = v.count("B")
if a == b:
    print("Tie")
elif a > b:
    print("A")
else:
    print("B")'''

'''for i in range(int(input())):
    s = input()
    if s[len(s)//2-1] == s[len(s)//2]:
        print('Do-it')
    else:
        print('Do-it-Not')'''

'''n = input()
p = list(map(int, input().split()))
pset = set(p)
print(len(p)-len(pset))'''

'''a, b = input().split()
a = int(a)
if b == 'miss':
    print(0)
elif b == 'bad':
    print(200*a)
elif b == 'cool':
    print(400*a)
elif b == 'great':
    print(600*a)
else:
    print(1000*a)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()
'''
n = int(input())
a = list(map(int, input().split()))
c = (sum(a)+8*(n-1))
print(c//24, c%24)'''

'''a, b = map(int, input().split())
cnt = 0
for i in range(a):
    for j in range(b):
        if i+j == a and max(i, j) - min(i, j) == b:
            print(max(i, j), min(i, j))
            cnt = 1
if cnt == 0:
    print(-1)'''

'''d = {'Algorithm': 204, 'DataAnalysis':207, 'ArtificialIntelligence':302, 'CyberSecurity':'B101', 'Network':303,
'Startup':501, 'TestStrategy':105}

for i in range(int(input())):
    print(d[input()])'''


'''for i in range(int(input())):
    t = True
    d = input()
    s = []*50
    for j in d:
        if j == '(':
            s.append(j)
        elif j == ')':
            if len(s) == 0:
                print("NO")
                t = False
                break
            else:
                s.pop()
    if t:
        if len(s) == 0:
            print('YES')
        else:
            print("NO")'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''def p(a):
    if a == ')' or a == '(':
        return 0
    elif a == '-' or a == '+':
        return 1
    else : return 2

d = input()
s = []

for idx in d:
    if idx == '(':
        s.append(idx)
    elif idx == ')':
        while len(s) != 0:
            op = s.pop()
            if op == '(':
                break
            else: 
                pass
                print(op, end="")
    elif idx in '+-*/':
        while len(s) != 0:
            op = s[-1]
            if p(idx) <= p(op):
                print(op, end="")
                s.pop()
            else: break
        s.append(idx)

    else:
        print(idx, end="")

while len(s) != 0:
    print(s.pop(), end="")'''

'''a = 5; b = 3

def f(c):
    n = 0
    global a
    a = c
    if n < c:
        n = a + c
    return n

def g(c):
    n = 0
    a = c
    if n <f(c):
        n = a + b
    return n

i = 1
b = g(i)
print("%d" %(a+b+i))'''


# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''from collections import deque

n = int(input())

d = deque(range(1, n+1))
while len(d) != 1:
    d.popleft()
    a = d.popleft()
    d.append(a)

print(d[0])'''

'''while 1:
    s = input()
    if s == ".":
        break
    t = []
    for i in s:
        if i == '(':
            t.append(i)
        elif i == '[':
            t.append(i)
        elif i == ')':
            if len(t) != 0:
                if t[-1] == '(':
                    t.pop()
                else:
                    continue
        elif i == ']':
            if len(t) != 0:
                if t[-1] == '[':
                    t.pop()
                else:
                    continue

    if len(t):
        print('no')
    else:
        print("yes")'''

'''import sys
input = lambda: sys.stdin.readline().rstrip()

s = list(input())
i = 0
while s:
    if s[i] == ' ':
        i += 1
        continue
    elif s[i] == '<':
        t = []
        while s[i] != '>':
            print(s[i])
            i += 1
            t.append(i)
print(t)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''def f(s):
    t = []
    for i in s:
        if (i == '(') or (i == '['):
            t.append(i)
        elif (i == ']') or (i == ')'):
            if len(t) == 0:
                return 'no'
            left = t.pop()
            if ((i == ')') and (left != '(')) or ((i == ']') and (left != '[')):
                return 'no'
            
    if len(t):
        return 'no'
    else:
        return 'yes'
    
while 1:
    s = input()
    if s == ".":
        break
    print(f(s))'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n1, n2 = map(int, input().split())
m = int(input())
o = int(input())
if (n1*o+n2) <= (m*o) and n1 <= m:
    print(1)
else:
    print(0)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''N = int(input())
stack = []

def push(_) :
    stack.append(_)

def pop() :
    if len(stack) == 0 :
        print(-1)
    else :
        print(stack.pop())

def size() :
    print(len(stack))

def empty() :
    if len(stack) == 0 :
        print(1)
    else :
        print(0)

def top() :
    if len(stack) == 0 :
        print(-1)
    else :
        print(stack[-1])


for i in range(N) :
    inputs = input()
    if not inputs.find(' ') == -1 :
        a, b = inputs.split()
        b = int(b)
        if a == '1' :
            push(b)
    else :
        a = inputs
        if a == '2' :
            pop()
        elif a == '3' :
            size()
        elif a == '4' :
            empty()
        elif a == '5' :
            top()'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''n = int(input())
a = list(map(int, input().split()))[::-1]
d = []
for i in range(len(a)):
    cnt = 0
    for j in a[i+1:]:
        if a[i] <= j:
            cnt = 1
            d.append(a[::-1].index(j)+1)
            break
    if cnt == 0:
        d.append(0)
print(*d[::-1])'''

'''n, m, k = map(int, input().split())
print(k//m, k%m)'''

"""for i in range(int(input())):
    d, n, s, p = map(int, input().split())
    if (d+p*n) == (n*s):
        print("does not matter")
    elif (d+p*n) > (n*s):
        print("do not parallelize")
    else:
        print("parallelize")"""


# eye, see
# drop, water
# man, shape, body, black
# vase, bottle

# 눈 인
# 물 병

# 

'''import sys
input = lambda: sys.stdin.readline().rstrip()
'''
'''while 1:
    n = input()
    if n == '0':
        break
    while 1:
        if len(n) == 1:
            print(n)
            break
        new = 0
        for i in n:
            new += int(i)
        n = str(new)'''

# b"as"s po"ta"to "sau"sage "c"heese
# as ta sua c
# castasua
# pastasuace

'''n = int(input())
d = []
d1 = []
for i in range(n):
    m = int(input())
    d1.append(m)
    if i == 0:
        d.append(m)
    elif d[-1] < m:
        d.append(m)

d1 = d1[::-1]
d2 = []
for i in range(n):
    if i == 0:
        d2.append(d1[i])
    elif d2[-1] < d1[i]:
        d2.append(d1[i])
    
print(len(d))
print(len(d2))'''
'''
for i in range(int(input())):
    s = input()
    b = s.count('b')
    b += s.count('B')
    g = s.count('g')
    g += s.count('G')
    print(f"{s} is ", end="")
    if b == g:
        print('NEUTRAL')
    elif b > g:
        print('BADDY')
    else:
        print("GOOD")'''

'''print(str(bin(int(input(),2)*17))[2:])'''

'''d = {1:(12, 1600), 2:(11, 894), 3:(11, 1327), 4:(10, 1311), 5:(9, 1004), 6:(9, 1178),
     7:(9, 1357), 8:(8, 837), 9:(7, 1055), 10:(6, 556), 11:(6, 773)}

print(*d[int(input())])'''

'''d = {}

def pre(n):
    print(n, end="")
    if d[n][0] != '.':
        pre(d[n][0])
    if d[n][1] != '.':
        pre(d[n][1])

def mid(n):
    if d[n][0] != '.':
        mid(d[n][0])
    print(n, end="")
    if d[n][1] != '.':
        mid(d[n][1])

def post(n):
    if d[n][0] != '.':
        post(d[n][0])
    if d[n][1] != '.':
        post(d[n][1])
    print(n, end="")

for i in range(int(input())):
    p, l, r = input().split()
    d[p] = [l, r]

pre('A')
print()
mid('A')
print()
post('A')'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''for i in range(int(input())):
    st = []
    s = input().split()
    for j in s:
        for k in j:
            st.append(k)
        for k in range(len(st)):
            print(st.pop(), end="")
        print(" ", end="")
    print()'''

# AB/C*D*E+
# 0.5*3*4+5=11


# st = []
# s = input()
# for j in s:
#     if j == '<':
#         if len(st)!=0:
#             for k in range(len(st)):
#                 print(st.pop(), end="")
#                 # print(st)
#         else:
#             st.append(j)
#             print(j, end="")
#     elif j == '>':
#         st.pop()
#         print(j, end="")
#     elif j == ' ':
#         for k in range(len(st)):
#             print(st.pop(), end="")
#         print(' ', end="")
#     else:
#         if len(st) != 0:
#             if st[-1] == '<':
#                 print(j, end="")
#                 continue
#         st.append(j)

'''n = int(input())
m = int(input())
print((n-m)//2+m)
print((n-m)//2)'''


'''st = []
s = input()
for i in s:
    if st:
        if i == '>':
            st.pop()
            print(i, end="")
        elif i == '<':
            for j in range(len(st)):
                print(st.pop(), end="")
            st.append(i)
            print(i, end="")
        elif st[-1] == '<':
            print(i, end="")
        elif i == ' ':
            for j in range(len(st)):
                print(st.pop(), end="")
            print(' ', end="")
        else:
            st.append(i)
    else:
        if i == '<':
            print(i, end="")
        st.append(i)

if st:
    for j in range(len(st)):
        print(st.pop(), end="")'''
'''
import sys
input = lambda: sys.stdin.readline().rstrip()
'''
'''while 1:
    m, a, b = map(int, input().split())
    if m == a == b == 0:
        break
    t = round((b - a) * m * 3600 / (a * b))
    h = t // 3600
    t = t % 3600
    m = t // 60
    s = t % 60
    print('%01d:%02d:%02d' % (h, m, s))'''

'''n, m, k = map(int, input().split())
print(m*k+m)'''
'''
for i in range(int(input())):
    s = set()
    n = int(input())
    for j in range(1, n//2+1):
        if n - j != j:
            s.add((j, n-j))
    s = sorted(list(s))
    if s:
        print(f"Pairs for {n}:", end=" ")
        for k in range(len(s)):
            if k != len(s)-1:
                print(*s[k], end=", ")
            else:
                print(*s[k])
    else:
        print(f"Pairs for {n}:")
'''
'''
import sys
input = lambda: sys.stdin.readline().rstrip()

books_list = []
n, m = map(int, input().split())
for i in range(m):
    b = input()
    books = list(map(int, input().split()))
    books_list.append(books)

def f():
    d = [0]
    while 1:
        cnt = 0
        tops = []
        for i in books_list:
            if i:
                tops.append(i.pop())
        for i in tops:
            if d[-1] + 1 == i:
                d.append(i)
                cnt = 1
        # print(d, tops)
        if cnt == 0:
            return "No"
        if len(d) == n+1:
            return "Yes"
    return "No"

print(f())'''


# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''def f():
    n, m = map(int, input().split())
    for i in range(m):
        b = int(input())
        books = list(map(int, input().split()))
        for i in range(b-1):
            if books[i] < books[i+1]:
                return "No"
    return "Yes"
print(f())'''

'''for _ in range(int(input())):
    n = input()
    note1 = set(list(map(int, input().split())))
    m = input()
    note2 = list(map(int, input().split()))
    for i in note2:
        if i in note1:
            print(1)
        else:
            print(0)'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()
 
'''s = input()

for i in range(len(s)):
    if i != 0 and i%10 == 9:
        print(s[i])
    else:
        print(s[i], end="")'''

'''n = int(input())
re = n + 2 * n + n
print(int(input())*4)'''


'''t = []
while 1:
    s = input()
    if s == '=':
        break
    elif s == '+' or s == '-' or s == '/' or s == '*':
        t.append(s)
    else:
        if len(t) == 0:
            t.append(int(s))
        else:
            s = int(s)
            x = t.pop()
            y = t.pop()
            if x == '+':
                t.append(s+y)
            elif x == '-':
                t.append(y-s)
            elif x == '*':
                t.append(y*s)
            else:
                t.append(y//s)

print(t[0])'''

'''n = int(input())
for i in range(n):
    num = int(input())
    if num%2 != 0:
        print("odd")
    else:
        print("even")'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()
'''
while 1:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print(a//b, a%b, "/", b)'''

'''
def heappop(t):
    size = len(t) - 1
    if size == 0: return 0
    p = 1; i = 2
    root = t[1]
    last = t[size] # 마지막 노드
    while i <= size:
        if i < size and t[i] > t[i+1]:
            i += 1
        if t[i] >= last: break
        t[p] = t[i]
        p = i
        i = i * 2
    
    t[p] = last
    t.pop()
    return root


t = [0]
for i in range(int(input())):
    n = int(input())
    if len(t) == 1 and n == 0:
        print(0)
    else:
        if n == 0:
            print(heappop(t))
        else:
            t.append(n)
            i = len(t) - 1 # n이 삽입될 위치
            while i != 1 and n < t[i//2]:
                t[i] = t[i//2]
                i = i//2
            t[i] = n'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

'''a, b, c = map(int, input().split())
if a + b == c: print("correct!")
else: print("wrong!")'''
'''
n = input()
if '9' in n:  print("F")
else: print("S")'''

'''d = {'black':0, 'brown':1, 'red':2, 
     'orange':3, 'yellow':4, 'green':5,
     'blue': 6, 'violet': 7, 'grey': 8, 'white':9}
a = input()
b = input()
c = input()
print(int(str(d[a])+str(d[b]))*int('1'+'0'*d[c]))'''

# import sys
# input = lambda: sys.stdin.readline().rstrip()

# n=input();print(sorted(list(map(int,input().split())))[-1])

'''while 1:
    n = int(input())
    if n == 0:
        break
    sum = 0
    for i in range(1,n+1):
        sum+= i
    print(sum)'''

'''n = int(input())
card_list = set(list(map(int,input().split())))
m = int(input())
sangn_list = list(map(int,input().split()))
for i in sangn_list:
    if i in card_list:
        print(1,end=" ")
    else:
        print(0,end=" ")'''

'''n=input()
s=input()
if 'gori' in s:print("YES")
else:print("NO")'''

'''s = set(input())
if "M" in s and "O" in s and "B" in s and "I" in s and "S" in s:
    print("YES")
else:
    print("NO")'''

'''a, b, c = map(int, input().split())
print((a+1)*(b+1)//(c+1)-1)'''

'''n = int(input())
print(1)
print(n//2)'''

'''n = int(input())
print(n**2)
print(2)'''

'''n = int(input())
print((n**2-n)//2)
print(2)'''
'''
n = int(input())
print((n)**3)
print(3)'''

'''ch = 1
bi = 1
n, a, b = map(int, input().split())
for i in range(n):
    ch += a
    bi += b
    if ch < bi :
        bi, ch = ch, bi
    elif ch == bi:
        bi -= 1
print(ch, bi)'''

'''c=input()
print(input().replace("I", "i").replace("l", "L"))'''
'''
n = int(input())
if n<=32767 and n>=-32768:
    print("short")
elif n<=2147483647 and n>=-2147483648:
    print("int")
else:
    print("long long")'''

import sys
input = lambda: sys.stdin.readline().rstrip()

'''cnt = 0
y = input()
n = input()
for i in n:
    if int(i)%2==0:
        cnt += 1

if cnt > len(n) - cnt:
    print(0)
elif cnt == len(n) - cnt:
    print(-1)
else:
    print(1)'''

'''t = ([([([1,2,3],),],)],)
t[0][0][0][0][0][0] = 5
print(t)

t2 = (1, 2, 3)*100'''

import pandas as pd
s1 = pd.Series([20,21,23])        
s2 = pd.Series(('남','여','남'))   
s3 = pd.Series({'가':'이순신','나':'이영희','다':'김철수'})   #딕셔너리로 생성
print(s1)
print(s2)
print(s3)

print(s1.loc[1])
print(s1.iloc[1])
print(s3['가'])
print(s3.loc['가'])
# print(s3.loc[0])
print(s3.iloc[0])        
print(s3[['가','나','다']])  
print(s3.loc[['가','나','다']])
print(s3.iloc[[0,1,2]])
