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

a, d, n = map(int, input().split())
y=a
for i in range(a, n):
    y += d
print(y)