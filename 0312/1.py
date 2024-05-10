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