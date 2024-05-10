'''a = [1,2,3,4,5]
a[0] = [3]
print(a)'''


'''a = []
a.append([1, 2])
#하나의 리스트를 넣ㅇ는것 ok

a = []
a.append(1,2)
#동시에 두개 x'''

'''city = ["서울", "대전", "대구", "부산"]
sale = [80, 60, 22, 50, 75]

for i in zip(city, sale) :
	print(i)

city = ["서울", "대전", "대구", "부산"]
sale = [80, 60, 22, 50, 75]

for i in enumerate(city) :
    print(i)'''

'''a = [1, 2, 3]
d1, d2, d3 = a #리스트의 요소를 변수에 언팩 가능
print(d1, d2, d3)'''

'''data = [1, 2, 3, 4, 5, 6, 7]

new = [i*2 for i in data if i%2==0]
print(new)'''
'''
data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

new = [i-3 for i in data if i%7==0]
print(new)'''

'''d = []

for i in range(5):
    t = int(input())
    d.append(t)

d.sort()
print(d)
d.reverse()
print(d)'''

