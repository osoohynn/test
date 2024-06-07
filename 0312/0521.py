#sorted는 리스트로 반환하는 함수

'''mart = {'과자': 1500, '아이스크림': 1700, 
'휴지':4800, '고기': 10500, '우유':2600}
print(type(mart.items()))'''

# clear()은 딕셔너리의 모든 요소를 삭제,
# del은 딕셔너리 자체를 삭제

'''mem = {"이진주": 23, "조현아": 20, "김창대": 25, "윤성원": 24}
names = list(mem.keys()) #새로운 리스트 변수에 초기화
print("key와 value를 튜플로", mem.items())
print(mem.get("김익현", "zz")) #get(a,b) a가 있다면 a의 밸류,없다면 b 반환

exist = '김창대' in names #굉장히 직관적인 용법
print(exist)

exist = '조현아' in mem
print(exist)

mem.clear()
print(mem)''' #빈 딕셔너리 출력

'''dic = {'준영':95, '하예':78, '가윤':82, '성희':51, '미연':94}
n = input('어떤 학생의 점수가 궁금한가요?')'''
# print(dic.get(n,'해당 학생이 없습니다.'))
'''if n in dic:
    print(dic[n],'점','입니다')
else:
    print('해당 학생이 없습니다')'''

'''print(dic[n],'점','입니다' if (n in dic) else n)'''
'''
n = set(input())
print(len(n)-1 if ' ' in n else len(n))

print(len(set(input().replace(' ',''))))'''

'''s = {1,2,3,4}
s.add('hello')
print(s)'''

'''def nsum(n):
    if n == 0:
        return 0
    return n + nsum(n-1)

print(nsum(10))'''

'''def fibo(n):
    if n == 1:
        return 0
    if n==2:
        return 1
    return fibo(n-2)+fibo(n-1)

print(fibo(int(input())))'''

'''n = int(input())

a, b = 0, 1

for i in range(n):
  a, b = b, a + b

print(a)'''
