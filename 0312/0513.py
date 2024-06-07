'''def taro(a,b,c):
    d = 0
    r = list(str(a+b+c))
    for i in r:
        d += int(i)
    # if d<22:
    #     return d
    # else:
    #     return d-22
    return d%22

a,b,c = map(int, input().split('.'))
print(taro(a,b,c))'''

'''#각 함수의 pass부분을 수정하여 함수를 완성하자.
def usum(arr):
	s = 0
	for i in arr:
		s += i
	return s
def ucount(arr):
	cnt = 0
	for i in arr:
		cnt += 1
	return cnt
def uaverage(arr):
	# s = 0
	# for i in arr:
	# 	s += i
	# cnt = 0
	# for i in arr:
	# 	cnt += 1
	# return s/cnt
    return usum(arr)/ucount(arr)
def umax(arr):
	m = 0
	for i in arr:
		if i >= m:
			m = i
	return m
def umin(arr):
	m = 1000000000
	for i in arr:
		if i <= m:
			m = i
	return m

arr = list(map(int, input().split()))
# 리스트를 공백으로 구분하여 입력 받음

	
print(usum(arr))
print(ucount(arr))
print(uaverage(arr))
print(umax(arr))
print(umin(arr))
'''

#각 함수의 pass부분을 수정하여 함수를 완성하자.

'''def ucountif(criteria, arr):
    cnt = 0
    if criteria[0]=='>' and criteria[1]=='=':
        for i in arr:
            if i>= int(criteria[2:]):
                cnt += 1
    if criteria[0]=='<' and criteria[1]=='=':
        for i in arr:
            if i<= int(criteria[2:]):
                cnt += 1
    if criteria[0]=='>' and criteria[1]!='=':
        for i in arr:
            if i> int(criteria[1:]):
                cnt += 1
    if criteria[0]=='<' and criteria[1]!='=':
        for i in arr:
            if i< int(criteria[1:]):
                cnt += 1
    return cnt


def urank(a, arr):
    ran = 1
    for i in arr:
        if a<i:
            ran += 1
    return ran
	
arr = list(map(int, input().split()))
criteria= input()
#countif함수에서 사용될 조건을 입력받음(등호 또는 부등호와 숫자가 붙여서 입력된다.)



print(ucountif(criteria, arr))
print(urank(arr[0], arr))
'''

