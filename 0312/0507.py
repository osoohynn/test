'''city = ["서울", "대전", "대구", "부산"]
sale = [80, 60, 22, 50, 75]

for i in zip(city, sale) :
	print(list(i))
#둘 중 더 짧은 요소를 가진 것만큼 돈다.
print()
print(tuple(zip(city, sale)))'''

                    #(=i)
'''print([len(name) for name in nmaes])
print([ x**2 for i in range(10) if 5<x**2 ])
print([x**y for x in range(1,5) for y in range(1,3)])


print([0 for x in range(10)])'''

# 리스트함수

'''a = [0, 1, 2, 3, 4, 5, 6, 7]

for i in reversed(a) : #역순으로 나오지만
	print(i, end="")
print()
print(a) #원래데이터 변경되지 않음
	
print(reversed(a)) #이터레이터
print(a) #원레데이터 변경되지 않음

a=sorted([int(input()) for i in range(5)])
print(a,a[::-1],sep='\n')'''

"""arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''
arr = [[1, 2, 3],
       [4, 5, 6], 
       [7, 8, 9]]
'''

for i in range(3) :
	for j in range(3) :
		print(arr[i][j], end=" ")
	print()
"""
'''arr = [[5,8,10,6,4], [11,20,1,13,2], [7,9,14,22,3]]
for i in range(3):
    for j in range(5):
        print(f'{arr[i][j]:>2}', end="   ")
    print()'''

'''arr1 = [0,0]
arr2 = [0,0]
for i in range(2):
    arr1[i] = list(map(int, input().split()))
for i in range(2):
    arr2[i] = list(map(int, input().split()))
for i in range(2):
    for j in range(4):
        print(arr1[i][j]*arr2[i][j], end=" ")
    print()'''