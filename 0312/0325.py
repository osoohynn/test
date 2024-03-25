'''a = [1,2,3]
b = a.copy() #a리스트의 주소를 복사
a[2] = "dfsdf"
print(b)'''
'''
print(1 or 0) 
print(0 or 1) 
print(1 or 2)
print(2 or 1)


print(1 and 0)
print(0 and 1)
print(1 and 2)
print(2 and 1)
print(0 and [])
print([] and 0)'''

a, b = map(int, input().split())

print(f"{a/b:.2f}")