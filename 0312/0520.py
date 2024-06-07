'''def nsum(n) :
	s = 0
	if n > 0:
		nsum(n-1)
	s += n
	if n == 0:
		return n + nsum(n-1)

n = int(input())
print(nsum(n))
'''
'''data = ['a', 'b', 'c', 'd']
da = 'hello'
print(" ".join(da))'''

'''data = [['010','6733','4534'],['010','6733','4534'],['010','6733','4534'],['010','6733','4534']]

for i in data:
	print('-'.join(i))'''

'''print([max(list(map(int, input().split()))) for i in range(int(input()))])'''

'''t = int(input())
for i in range(t):
	print(''.join(input().split()).find('8'))'''

#자연수 n을 입력받아 1부터 n까지의 정수를 차례로 출력하기

'''def coding(n) :
	if n == 0 :
		return
	coding(n-1)
	print(n)
	
n = int(input())
coding(n)
'''
'''
s=[]
def nsum(n):
	if n==0:
		return sum(s)
	s.append(n)
	nsum(n-1)

n = int(input())
print(sum(s))'''

'''n = int(input())
l1 = set(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

for i in l2:
	if i in l1:
		print(1)
	else:
		print(0)'''

'''a,b,c,d = map(int,input().split())
print(a*b+c*d)'''

# print(input()[::-1])


for i in range(int(input())):print(sum(list(map(int, input().split()))))
