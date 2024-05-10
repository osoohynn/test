'''a = [0, 1,2,3]
b = a[:]
a[0] = 8
print(b)'''

'''a, b = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
lst = al+bl
lst.sort(reverse=True)

for i in lst:
    print(i, end=" ")'''

'''to_do = []
while True:
    s = input()
    if s == '끝':
        break
    to_do.append(s)

print(to_do)'''


'''a = [25, 34, 10, 5, 80, 63]
c = sorted(a, reverse=True)
b = []
for i in a:
    b.append(c.index(i)+1)

print(b)'''
'''odd = [1, 3, 5, 7, 9]
cafes = ['star', 'bene', 'yoger', 'friends']
A = [1, 5, 'A', 'CC', 'B']
listInList = [[1, 3, 5, 6, 7], cafes, odd, 1, 3, 'Abc']

a = odd[1:5]
b = cafes[1:]
c = A[:2]
d = listInList[0][1:4] #리스트 내 리스트 접근

print(a)
print(b)
print(c)
print(d)'''

'''list = [25, 36, 8, 53, 24, 56]
print(list[-1])
print(list[-2])
print(list[-3])
print(list[-4])
print(list[-5])
print(list[-6])'''

'''numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

numbers[4] = 100
print(numbers)

numbers[2] = "hello"
print(numbers)

numbers[0] = numbers[9] #인덱스 9를 인덱스 0에 대입
print(numbers)

numbers[8] = ['a', 'b', 'c'] #리스트 전체를 형태 유지하며 대입
print(numbers)'''

'''numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

numbers[8] = ['a', 'b', 'c'] #리스트 전체를 형태 유지하며 대입
print(numbers)

#출력값 numbers = [2, 4, 6, 8, 10, 1, 3, 5, [a, b, c] , 9]'''

'''numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

numbers[2:3] = ['a', 'b', 'c'] #각 요소가 분해되어 대입
print(numbers)

#출력값 numbers = [2, 4, 6, 8, 10, 1, 3, 5, ['a', 'b', 'c'] , 9]'''

'''a = [1, 2, 3, 4, 5, [5,6,7]]
print(len(a))'''

'''a = [10, 20, 30, 40, 50]
del a[3]
print(a)

a.pop(2)
print(a)

a.pop() #아무것도 없으면 -1이 들어감
print(a)'''


'''date1 = [1, 2, 3, 4, 5]
date2 = list(date1)

print("date1은 ", date1)
print("date2은 ", date2)

date1[0] = 10
print("date1 변경 후")

print("date1은 ", date1)
print("date2은 ", date2)

date = '2023-03-30'
date = date.split('0')
print(date)'''